from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData
import vfx_loader


loadPrcFileData('', 'model-path assets')
loadPrcFileData('', 'model-path samples/shiny')


class App(ShowBase):
    def __init__(self):
        super().__init__()
        base.enableParticles()
        #set view
        base.disableMouse()
        base.camera.setPos(30.0, -30.0, 10.0)
        base.camera.lookAt((0.0, 0.0, -1.0))

        p = vfx_loader.load('samples/shiny/shiny.json')
        p.start(parent=self.render, renderParent=render)

App().run()
