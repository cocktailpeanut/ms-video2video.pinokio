const os = require('os')
const fs = require('fs')
const path = require("path")
const exists = async p => !!(await fs.promises.stat(p).catch(e => false));
module.exports = {
  title: "ModelScope Video2Video (Nvidia GPU only)",
  icon: "icon.png",
  description: "enhance the resolution and spatiotemporal continuity of text-generated videos and image-generated videos",
  menu: async (kernel) => {
    let installed = await exists(path.resolve(__dirname, "env"))
    if (installed) {
      let session = (await kernel.loader.load(path.resolve(__dirname, "session.json"))).resolved
      return [{
        when: "start.json",
        on: `<i class='fa-solid fa-spin fa-circle-notch'></i> Running`,
        type: "label",
      }, {
        when: "start.json",
        off: "<i class='fa-solid fa-power-off'></i> Start",
        href: "start.json?fullscreen=true&run=true",
      }, {
        when: "start.json",
        on: "<i class='fa-solid fa-rocket'></i> Open UI",
        href: (session && session.url ? session.url : "http://127.0.0.1:7860"),
        target: "_blank"
      }, {
        when: "start.json",
        on: "<i class='fa-solid fa-desktop'></i> Server",
        href: "start.json?fullscreen=true"
      }]
    } else {
      return [{
        html: '<i class="fa-solid fa-plug"></i> Install',
        href: "install.json?run=true&fullscreen=true"
      }]
    }
  }
}

