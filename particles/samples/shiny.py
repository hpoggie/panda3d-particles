from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData, ConfigVariableSearchPath
from particles import vfx_loader
import colorama

colorama.init()
shinyPath = vfx_loader.loadAssetPath('samples/shiny')
print(colorama.Fore.YELLOW + "[SAMPLE] " + colorama.Fore.RESET +
      "Loaded asset path: " + shinyPath)


class App(ShowBase):
    def __init__(self):
        super().__init__()
        base.enableParticles()
        #set view
        base.disableMouse()
        base.camera.setPos(30.0, -30.0, 10.0)
        base.camera.lookAt((0.0, 0.0, -1.0))

        p = vfx_loader.load('shiny.json')
        p.start(parent=self.render, renderParent=render)


App().run()
