const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('setup', {
  start:            (dir) => ipcRenderer.send('setup:start', dir),
  openPanel:        ()    => ipcRenderer.send('setup:open-panel'),
  chooseFolder:     ()    => ipcRenderer.invoke('choose-folder'),
  getDefaultFolder: ()    => ipcRenderer.invoke('get-default-folder'),
  onProgress:       (cb)  => ipcRenderer.on('setup:progress', (_, d) => cb(d)),
  onDone:           (cb)  => ipcRenderer.on('setup:done', () => cb()),
  onError:          (cb)  => ipcRenderer.on('setup:error', (_, msg) => cb(msg))
})
