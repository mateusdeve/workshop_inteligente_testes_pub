const { app, BrowserWindow, ipcMain, shell } = require('electron')
const path = require('path')
const os = require('os')
const fs = require('fs')
const vm = require('vm')
const { exec } = require('child_process')
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

function isClaudeInstalled() {
  if (process.platform === 'darwin') {
    return [
      '/Applications/Claude.app',
      path.join(os.homedir(), 'Applications', 'Claude.app'),
    ].some(p => fs.existsSync(p))
  }
  if (process.platform === 'win32') {
    return [
      path.join(os.homedir(), 'AppData', 'Local', 'AnthropicClaude', 'claude.exe'),
      path.join(os.homedir(), 'AppData', 'Local', 'Programs', 'Claude', 'Claude.exe'),
      'C:\\Program Files\\Anthropic\\Claude\\Claude.exe',
    ].some(p => fs.existsSync(p))
  }
  return false
}

function silentPull(callback) {
  exec(`git -C "${getRepoDir()}" pull origin poc`, { timeout: 20000 }, (err, stdout) => {
    const updated = !err && stdout && !stdout.trim().endsWith('Already up to date.')
    callback(updated)
  })
}

function injectClaudeButton(win) {
  win.webContents.executeJavaScript(`
    (function() {
      if (document.getElementById('__claude-btn')) return;
      const btn = document.createElement('button');
      btn.id = '__claude-btn';
      btn.innerHTML = '⚡ Abrir Claude';
      btn.style.cssText = [
        'position:fixed','top:14px','right:14px','z-index:99999',
        'background:rgba(20,20,30,0.88)','backdrop-filter:blur(10px)',
        'border:1px solid rgba(124,58,237,0.45)','border-radius:20px',
        'padding:6px 14px','color:#c4b5fd','font-size:12px','font-weight:600',
        'cursor:pointer','transition:all 0.15s',
        'font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif',
        'box-shadow:0 2px 12px rgba(124,58,237,0.2)','letter-spacing:0.02em'
      ].join(';');
      btn.onmouseover = () => { btn.style.background='rgba(124,58,237,0.82)'; btn.style.color='#fff'; };
      btn.onmouseout  = () => { btn.style.background='rgba(20,20,30,0.88)';   btn.style.color='#c4b5fd'; };
      btn.onclick = () => window.electronAPI && window.electronAPI.openClaude();
      document.body.appendChild(btn);
    })();
  `).catch(() => {})
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
    injectClaudeButton(mainWindow)
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
  if (process.platform === 'darwin') {
    const macPaths = [
      '/Applications/Claude.app',
      path.join(os.homedir(), 'Applications', 'Claude.app'),
      '/Applications/Claude AI.app',
      path.join(os.homedir(), 'Applications', 'Claude AI.app')
    ]
    const found = macPaths.find(p => fs.existsSync(p))
    if (found) {
      exec(`open "${found}"`, (err) => {
        if (err) shell.openExternal('https://claude.ai/download')
      })
    } else {
      exec('open -a "Claude"', (err) => {
        if (err) exec('open -a "Claude AI"', (err2) => {
          if (err2) shell.openExternal('https://claude.ai/download')
        })
      })
    }
  } else if (process.platform === 'win32') {
    const winPaths = [
      path.join(os.homedir(), 'AppData', 'Local', 'AnthropicClaude', 'claude.exe'),
      path.join(os.homedir(), 'AppData', 'Local', 'Programs', 'Claude', 'Claude.exe'),
      'C:\\Program Files\\Anthropic\\Claude\\Claude.exe',
      'C:\\Program Files (x86)\\Anthropic\\Claude\\Claude.exe'
    ]
    const found = winPaths.find(p => fs.existsSync(p))
    if (found) {
      exec(`"${found}"`, (err) => {
        if (err) shell.openExternal('https://claude.ai/download')
      })
    } else {
      exec('start "" "Claude"', (err) => {
        if (err) shell.openExternal('https://claude.ai/download')
      })
    }
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
