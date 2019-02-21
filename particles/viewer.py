from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData, ConfigVariableSearchPath
from particles import vfx_loader
import colorama
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str)
args = parser.parse_args()

colorama.init()
#shinyPath = vfx_loader.loadAssetPath(os.getcwd())
shinyPath = os.getcwd()
loadPrcFileData('', 'model-path ' + shinyPath)
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

        p = vfx_loader.load(args.f)
        p.start(parent=self.render, renderParent=render)


App().run()
