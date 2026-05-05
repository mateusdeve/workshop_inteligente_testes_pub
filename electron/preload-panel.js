const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('electronAPI', {
  openClaude: () => ipcRenderer.send('open-claude'),
  checkClaude: () => ipcRenderer.invoke('check-claude'),
  openDownloadClaude: () => ipcRenderer.send('open-download-claude'),
  getManifest: () => ipcRenderer.invoke('get-manifest'),
  getProductPath: (relUrl) => ipcRenderer.invoke('get-product-path', relUrl),
  onManifestChanged: (cb) => ipcRenderer.on('manifest-changed', cb),
  onPainelChanged: (cb) => ipcRenderer.on('painel-changed', cb),
  setPanelWatch: (filePath) => ipcRenderer.send('set-painel-watch', filePath),
})
