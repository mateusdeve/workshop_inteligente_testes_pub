const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('electronAPI', {
  openClaude: () => ipcRenderer.send('open-claude'),
  checkClaude: () => ipcRenderer.invoke('check-claude'),
  installClaude: () => ipcRenderer.send('install-claude'),
  onClaudeInstallResult: (cb) => ipcRenderer.on('claude-install-result', (_, ok) => cb(ok)),
})
