const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('setup', {
  start:      ()   => ipcRenderer.send('setup:start'),
  openPanel:  ()   => ipcRenderer.send('setup:open-panel'),
  onProgress: (cb) => ipcRenderer.on('setup:progress', (_, d) => cb(d)),
  onDone:     (cb) => ipcRenderer.on('setup:done', () => cb()),
  onError:    (cb) => ipcRenderer.on('setup:error', (_, msg) => cb(msg))
})
