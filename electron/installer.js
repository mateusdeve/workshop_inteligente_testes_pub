const { spawn } = require('child_process')
const path = require('path')
const os = require('os')
const fs = require('fs')

const INSTALL_DIR = path.join(os.homedir(), 'Documents', 'workshop-ia')
const REPO_URL = 'https://github.com/engdailyapp-rlv/workshop_inteligente.git'

function run(cmd, args, opts = {}) {
  return new Promise((resolve, reject) => {
    const proc = spawn(cmd, args, { stdio: 'pipe', ...opts })
    proc.on('close', code => (code === 0 ? resolve() : reject(new Error(`${cmd} saiu com código ${code}`))))
    proc.on('error', reject)
  })
}

async function install(send) {
  const isMac = process.platform === 'darwin'

  let brewBin = '/opt/homebrew/bin'
  if (!fs.existsSync(`${brewBin}/brew`)) brewBin = '/usr/local/bin'
  const brewExe = `${brewBin}/brew`

  const env = { ...process.env, PATH: `${brewBin}:/usr/local/bin:/usr/bin:/bin` }

  if (isMac) {
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
  }

  send(5, 'Baixando o Workshop IA...', 72)
  const git = fs.existsSync(`${brewBin}/git`) ? `${brewBin}/git` : 'git'
  if (fs.existsSync(path.join(INSTALL_DIR, '.git'))) {
    await run(git, ['-C', INSTALL_DIR, 'pull', 'origin', 'poc'], { env })
  } else {
    await run(git, ['clone', '-b', 'poc', REPO_URL, INSTALL_DIR], { env })
  }

  send(6, 'Instalando dependências do painel...', 90)
  const npm = fs.existsSync(`${brewBin}/npm`) ? `${brewBin}/npm` : 'npm'
  await run(npm, ['install'], { cwd: INSTALL_DIR, env })

  fs.writeFileSync(path.join(INSTALL_DIR, '.installed'), new Date().toISOString())
  send(7, 'Tudo pronto!', 100)
}

module.exports = { install, INSTALL_DIR }
