const { spawn } = require('child_process')
const path = require('path')
const os = require('os')
const fs = require('fs')

const DEFAULT_INSTALL_DIR = path.join(os.homedir(), 'Documents', 'workshop-ia')
const REPO_URL = 'https://github.com/engdailyapp-rlv/workshop_inteligente.git'

function run(cmd, args, opts = {}) {
  return new Promise((resolve, reject) => {
    const proc = spawn(cmd, args, { stdio: 'pipe', ...opts })
    proc.on('close', code => (code === 0 ? resolve() : reject(new Error(`${cmd} saiu com código ${code}`))))
    proc.on('error', reject)
  })
}

// ─── Windows helpers ──────────────────────────────────────────────────────────

function runPs(script) {
  return run('powershell.exe', ['-NoProfile', '-ExecutionPolicy', 'Bypass', '-Command', script])
}

function hasWinget() {
  return new Promise(resolve => {
    const proc = spawn('winget', ['--version'], { stdio: 'pipe' })
    proc.on('close', code => resolve(code === 0))
    proc.on('error', () => resolve(false))
  })
}

function hasChoco() {
  const local = path.join(os.homedir(), 'AppData', 'Local', 'Chocolatey', 'bin', 'choco.exe')
  if (fs.existsSync(local)) return local
  const system = 'C:\\ProgramData\\chocolatey\\bin\\choco.exe'
  if (fs.existsSync(system)) return system
  return null
}

// PATH isn't updated in the running process after winget/choco installs,
// so we probe known locations and fall back to the bare command name.
function resolveWinGit() {
  const candidates = [
    'C:\\Program Files\\Git\\cmd\\git.exe',
    'C:\\Program Files (x86)\\Git\\cmd\\git.exe',
    path.join(os.homedir(), 'AppData', 'Local', 'Programs', 'Git', 'cmd', 'git.exe'),
  ]
  return candidates.find(p => fs.existsSync(p)) || 'git'
}

function resolveWinNpm() {
  const candidates = [
    'C:\\Program Files\\nodejs\\npm.cmd',
    path.join(os.homedir(), 'AppData', 'Roaming', 'npm', 'npm.cmd'),
  ]
  return candidates.find(p => fs.existsSync(p)) || 'npm'
}

// .cmd files cannot be spawned directly — must go through cmd /c
function runNpm(npmPath, args, opts = {}) {
  if (npmPath.endsWith('.cmd')) {
    return run('cmd.exe', ['/c', npmPath, ...args], opts)
  }
  return run(npmPath, args, opts)
}

async function installWindows(send) {
  const winget = await hasWinget()

  if (winget) {
    send(1, 'Verificando gerenciador de pacotes (winget)...', 8)

    send(2, 'Instalando Python 3...', 22)
    await run('winget', [
      'install', '--id', 'Python.Python.3.12',
      '--accept-source-agreements', '--accept-package-agreements',
      '--silent', '--scope', 'user',
    ]).catch(() => {})

    send(3, 'Instalando Git...', 40)
    await run('winget', [
      'install', '--id', 'Git.Git',
      '--accept-source-agreements', '--accept-package-agreements',
      '--silent',
    ]).catch(() => {})

    send(4, 'Instalando Node.js...', 58)
    await run('winget', [
      'install', '--id', 'OpenJS.NodeJS.LTS',
      '--accept-source-agreements', '--accept-package-agreements',
      '--silent',
    ]).catch(() => {})

    return
  }

  // Fallback: Chocolatey
  let chocoExe = hasChoco()
  if (!chocoExe) {
    send(1, 'Instalando Chocolatey...', 8)
    await runPs(
      `Set-ExecutionPolicy Bypass -Scope Process -Force; ` +
      `[System.Net.ServicePointManager]::SecurityProtocol = ` +
      `[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; ` +
      `iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))`
    )
    chocoExe = hasChoco() || 'choco'
  } else {
    send(1, 'Chocolatey já instalado.', 8)
  }

  send(2, 'Instalando Python 3, Git e Node.js...', 50)
  await run(chocoExe, ['install', 'python3', 'git', 'nodejs-lts', '-y', '--no-progress']).catch(() => {})
}

// ─── Main entry ───────────────────────────────────────────────────────────────

async function install(send, destDir = DEFAULT_INSTALL_DIR) {
  const isMac = process.platform === 'darwin'
  const isWin = process.platform === 'win32'

  if (isMac) {
    let brewBin = '/opt/homebrew/bin'
    if (!fs.existsSync(`${brewBin}/brew`)) brewBin = '/usr/local/bin'
    const brewExe = `${brewBin}/brew`
    const env = { ...process.env, PATH: `${brewBin}:/usr/local/bin:/usr/bin:/bin` }

    if (!fs.existsSync(brewExe)) {
      send(1, 'Instalando Homebrew...', 8)
      await run('/bin/bash', ['-c',
        'NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
      ])
      brewBin = fs.existsSync('/opt/homebrew/bin/brew') ? '/opt/homebrew/bin' : '/usr/local/bin'
      env.PATH = `${brewBin}:/usr/local/bin:/usr/bin:/bin`
    } else {
      send(1, 'Homebrew já instalado.', 8)
    }

    send(2, 'Instalando Python 3...', 25)
    await run(`${brewBin}/brew`, ['install', 'python3'], { env }).catch(() => {})

    send(3, 'Instalando Git...', 42)
    await run(`${brewBin}/brew`, ['install', 'git'], { env }).catch(() => {})

    send(4, 'Instalando Node.js...', 58)
    await run(`${brewBin}/brew`, ['install', 'node'], { env }).catch(() => {})

    send(5, 'Baixando o Workshop IA...', 72)
    const git = fs.existsSync(`${brewBin}/git`) ? `${brewBin}/git` : 'git'
    if (fs.existsSync(path.join(destDir, '.git'))) {
      await run(git, ['-C', destDir, 'pull', 'origin', 'main'], { env })
    } else {
      await run(git, ['clone', '-b', 'main', REPO_URL, destDir], { env })
    }

    send(6, 'Instalando dependências do painel...', 90)
    const npm = fs.existsSync(`${brewBin}/npm`) ? `${brewBin}/npm` : 'npm'
    await run(npm, ['install'], { cwd: destDir, env })

    send(7, 'Removendo restrições de segurança...', 95)
    await run('xattr', ['-rd', 'com.apple.quarantine', destDir], { env }).catch(() => {})

  } else if (isWin) {
    await installWindows(send)

    const git = resolveWinGit()
    const npm = resolveWinNpm()

    send(5, 'Baixando o Workshop IA...', 72)
    if (fs.existsSync(path.join(destDir, '.git'))) {
      await run(git, ['-C', destDir, 'pull', 'origin', 'main'])
    } else {
      await run(git, ['clone', '-b', 'main', REPO_URL, destDir])
    }

    send(6, 'Instalando dependências do painel...', 90)
    await runNpm(npm, ['install'], { cwd: destDir })
  }

  fs.writeFileSync(path.join(destDir, '.installed'), new Date().toISOString())
  send(7, 'Tudo pronto!', 100)
}

module.exports = { install, DEFAULT_INSTALL_DIR }
