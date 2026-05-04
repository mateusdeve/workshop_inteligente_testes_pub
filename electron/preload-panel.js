const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('electronAPI', {
  openClaude: () => ipcRenderer.send('open-claude'),
  checkClaude: () => ipcRenderer.invoke('check-claude'),
  openDownloadClaude: () => ipcRenderer.send('open-download-claude'),
})
