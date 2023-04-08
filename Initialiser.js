const { app, BrowserWindow } = require('electron');
const { join } = require('path');

const createWindow = () => {
  const win = new BrowserWindow({
    minwidth: 800,
    minheight: 600,
    titleBarStyle: 'hidden',
    webPreferences: {
        preload: join(__dirname, 'ipcFunctions.js'),
    },
  });

  win.loadFile('./frontend/dashboard.html');
};

app.whenReady().then(() => {
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});