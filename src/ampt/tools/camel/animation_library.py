#import internal libraries
from ampt.tools.widgets.tool_window import ToolWindow
from ampt.tools.widgets.save_animation import SaveAnimation
from ampt.tools.widgets.animation_list import AnimationList

#import third party libraries
from PySide import QtCore, QtGui


class AnimationLibrary(ToolWindow):
    def __init__(self):
        super(AnimationLibrary, self).__init__()

        self.title = "Animation Library"
        self.dimensions = QtCore.QRect(0, 0, 320, 480)

        self.main_layout = QtGui.QVBoxLayout(self)

        self.save_animation_widget = SaveAnimation(self)
        self.animation_list_widget = AnimationList(self)

        self.main_layout.addWidget(self.save_animation_widget)
        self.main_layout.addWidget(self.animation_list_widget)

        self.setLayout(self.main_layout)


animation_library = AnimationLibrary()
animation_library.display()