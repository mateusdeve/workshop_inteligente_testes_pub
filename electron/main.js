const { app, BrowserWindow, ipcMain, shell } = require('electron')
const path = require('path')
const os = require('os')
const fs = require('fs')
const vm = require('vm')
const { exec, spawn } = require('child_process')
const { install, INSTALL_DIR } = require('./installer')

function getPanelPath() {
  if (!app.isPackaged) return path.join(__dirname, '..', 'painel', 'index.html')
  return path.join(INSTALL_DIR, 'painel', 'index.html')
}

function isInstalled() {
  if (!app.isPackaged) return fs.existsSync(path.join(__dirname, '..', 'painel', 'index.html'))
  return fs.existsSync(path.join(INSTALL_DIR, '.installed'))
}

function getRepoDir() {
  return app.isPackaged ? INSTALL_DIR : path.join(__dirname, '..')
}

let mainWindow = null

// Detecta Claude no Windows via MSIX (Get-AppxPackage) ou Squirrel legado
function isClaudeInstalledWin() {
  return new Promise(resolve => {
    // MSIX: verifica pelo pacote instalado (funciona mesmo sem acesso a Program Files\WindowsApps)
    exec(
      'powershell -NoProfile -ExecutionPolicy Bypass -Command "if (Get-AppxPackage -Name \'*Claude*\' -ErrorAction SilentlyContinue) { exit 0 } else { exit 1 }"',
      { timeout: 8000 },
      (err) => {
        if (!err) { resolve(true); return }

        // Fallback Squirrel legado: subpastas app-x.y.z
        const local = path.join(os.homedir(), 'AppData', 'Local')
        const squirrelRoots = [path.join(local, 'AnthropicClaude'), path.join(local, 'Claude')]
        for (const root of squirrelRoots) {
          if (!fs.existsSync(root)) continue
          try {
            const appDirs = fs.readdirSync(root).filter(e => e.startsWith('app-'))
            for (const dir of appDirs) {
              if (fs.existsSync(path.join(root, dir, 'Claude.exe'))) { resolve(true); return }
            }
            if (fs.existsSync(path.join(root, 'Claude.exe'))) { resolve(true); return }
          } catch {}
        }

        resolve(false)
      }
    )
  })
}

function isClaudeInstalled() {
  if (process.platform === 'darwin') {
    return Promise.resolve([
      '/Applications/Claude.app',
      path.join(os.homedir(), 'Applications', 'Claude.app'),
    ].some(p => fs.existsSync(p)))
  }
  if (process.platform === 'win32') return isClaudeInstalledWin()
  return Promise.resolve(false)
}

function silentPull(callback) {
  exec(`git -C "${getRepoDir()}" pull origin main`, { timeout: 20000 }, (err, stdout) => {
    const updated = !err && stdout && !stdout.trim().endsWith('Already up to date.')
    callback(updated)
  })
}


function injectUpdateToast(win) {
  win.webContents.executeJavaScript(`
    (function() {
      const t = document.createElement('div');
      t.style.cssText = [
        'position:fixed','bottom:20px','left:50%','transform:translateX(-50%)',
        'z-index:99999','background:rgba(52,211,153,0.1)',
        'border:1px solid rgba(52,211,153,0.35)','border-radius:20px',
        'padding:7px 18px','color:#34d399','font-size:12px','font-weight:600',
        'font-family:-apple-system,sans-serif','backdrop-filter:blur(8px)',
        'transition:opacity 0.5s','pointer-events:none'
      ].join(';');
      t.textContent = '✓ Workshop IA atualizado';
      document.body.appendChild(t);
      setTimeout(() => { t.style.opacity='0'; }, 3000);
      setTimeout(() => t.remove(), 3600);
    })();
  `).catch(() => {})
}

let _manifestWatcher = null
let _manifestDebounce = null

function watchManifest() {
  if (_manifestWatcher) return
  const dir = path.join(getRepoDir(), 'meus-produtos')

  function tryWatch() {
    if (!fs.existsSync(dir)) { setTimeout(tryWatch, 3000); return }
    try {
      _manifestWatcher = fs.watch(dir, (_, filename) => {
        if (filename !== 'index.js') return
        clearTimeout(_manifestDebounce)
        _manifestDebounce = setTimeout(() => {
          if (mainWindow) mainWindow.webContents.send('manifest-changed')
        }, 300)
      })
    } catch { setTimeout(tryWatch, 3000) }
  }

  tryWatch()
}

let _painelWatcher = null
let _painelDebounce = null

function watchPainel(filePath) {
  if (_painelWatcher) { try { _painelWatcher.close() } catch {} _painelWatcher = null }
  if (!filePath) return
  const dir = path.dirname(filePath)
  const base = path.basename(filePath)
  function tryWatch() {
    if (!fs.existsSync(dir)) { setTimeout(tryWatch, 3000); return }
    try {
      _painelWatcher = fs.watch(dir, (_, filename) => {
        if (filename !== base) return
        clearTimeout(_painelDebounce)
        _painelDebounce = setTimeout(() => {
          if (mainWindow) mainWindow.webContents.send('painel-changed')
        }, 400)
      })
    } catch { setTimeout(tryWatch, 3000) }
  }
  tryWatch()
}

ipcMain.on('set-painel-watch', (_, filePath) => watchPainel(filePath))

function createPanelWindow() {
  mainWindow = new BrowserWindow({
    width: 1280,
    height: 800,
    minWidth: 900,
    minHeight: 600,
    title: 'Workshop IA',
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      webSecurity: false,
      preload: path.join(__dirname, 'preload-panel.js')
    }
  })
  mainWindow.loadFile(getPanelPath())
  mainWindow.setMenuBarVisibility(false)

  mainWindow.webContents.on('did-finish-load', () => {
    watchManifest()
    silentPull((updated) => {
      if (updated && mainWindow) injectUpdateToast(mainWindow)
    })
  })
}

function createSetupWindow() {
  mainWindow = new BrowserWindow({
    width: 540,
    height: 520,
    resizable: false,
    title: 'Workshop IA — Configuração',
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js')
    }
  })
  mainWindow.loadFile(path.join(__dirname, 'setup.html'))
  mainWindow.setMenuBarVisibility(false)
}

ipcMain.handle('check-claude', () => isClaudeInstalled())

ipcMain.handle('get-manifest', () => {
  const manifestPath = path.join(getRepoDir(), 'meus-produtos', 'index.js')
  try {
    const code = fs.readFileSync(manifestPath, 'utf8')
    const ctx = { window: {} }
    vm.createContext(ctx)
    vm.runInContext(code, ctx)
    return ctx.window.MEUS_PRODUTOS || null
  } catch {
    return null
  }
})

ipcMain.handle('get-product-path', (_, relUrl) => {
  return path.join(getRepoDir(), 'meus-produtos', relUrl)
})

ipcMain.on('open-download-claude', () => {
  shell.openExternal('https://claude.ai/download')
})

ipcMain.on('setup:start', async () => {
  try {
    await install((step, msg, pct) => {
      if (mainWindow) mainWindow.webContents.send('setup:progress', { step, msg, pct })
    })
    if (mainWindow) mainWindow.webContents.send('setup:done')
  } catch (err) {
    if (mainWindow) mainWindow.webContents.send('setup:error', err.message)
  }
})

ipcMain.on('setup:open-panel', () => {
  if (mainWindow) mainWindow.close()
  createPanelWindow()
})

ipcMain.on('open-claude', () => {
  const dir = getRepoDir()

  if (process.platform === 'darwin') {
    // Open Claude with the project dir, then click the Code tab via AppleScript
    const script = `
tell application "Claude"
  activate
end tell
do shell script "open -a Claude \\"${dir.replace(/"/g, '\\"')}\\""
delay 0.8
tell application "System Events"
  tell process "Claude"
    try
      set allBtns to every button of window 1
      repeat with b in allBtns
        if name of b contains "Code" then click b
      end repeat
    on error
      try
        repeat with grp in groups of window 1
          try
            set b to first button whose name contains "Code" of grp
            click b
            exit repeat
          end try
        end repeat
      end try
    end try
  end tell
end tell`
    const tmpFile = path.join(os.tmpdir(), 'workshop-ia-claude.scpt')
    fs.writeFileSync(tmpFile, script, 'utf8')
    exec(`/usr/bin/osascript "${tmpFile}"`, (err) => {
      if (err) exec(`open -a "Claude" "${dir}"`)
    })

  } else if (process.platform === 'win32') {
    exec('explorer.exe "shell:AppsFolder\\Claude_pzs8sxrjxfjjc!App"', (err) => {
      if (err) shell.openExternal('https://claude.ai/download')
    })
  }
})

function launch() {
  if (isInstalled()) createPanelWindow()
  else createSetupWindow()
}

app.whenReady().then(() => {
  launch()
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) launch()
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit()
})
