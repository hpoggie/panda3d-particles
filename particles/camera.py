from panda3d.core import TransformState, LMatrix4f
from direct.task import Task


class CameraControls:
    def __init__(self, mouseWatcherNode, camera):
        self.initialPos = camera.getPos()
        self.target = (0.0, 0.0, -1.0)

        self.camera = camera
        self.mouseWatcherNode = mouseWatcherNode

        self.rotating = False

    def onMouse3Down(self):
        self.rotating = True

    def onMouse3Up(self):
        self.rotating = False

    def rotateTask(self, task):
        if self.rotating and self.mouseWatcherNode.hasMouse():
            mpos = self.mouseWatcherNode.getMouse()
            matrix = TransformState.makeHpr((-mpos.x * 100, mpos.y * 100, 0)).mat
            newPos = matrix.xformPoint(self.initialPos)

            self.camera.setPos(newPos)
            self.camera.lookAt(self.target)

        return Task.cont


def enableCameraControls(base):
    controls = CameraControls(base.mouseWatcherNode, base.camera)
    base.accept('mouse3', controls.onMouse3Down, [])
    base.accept('mouse3-up', controls.onMouse3Up, [])
    base.taskMgr.add(controls.rotateTask, 'RotateTask')
