from ..tool_widget import ToolWidget
from PySide import QtGui


class AnimationLibrary(ToolWidget):
    def __init__(self):
        super(AnimationLibrary, self).__init__()
        self.setup_interface()
        self.show()

    def setup_interface(self):
        self.setWindowTitle("Camel - Animation Library")
        self.setGeometry(0, 0, 320, 480)
        self.move(self.screen_center)

        QtGui.QHBoxLayout()

    def save(self, *args, **kwargs):
        print "Hello"

AnimationLibrary()