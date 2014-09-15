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
        self.dimensions = QtCore.QRect(0, 0, 980, 480)

        self.main_layout = QtGui.QHBoxLayout(self)

        self.animation_list = AnimationList(self)


        self.setLayout(self.main_layout)


animation_library = AnimationLibrary()
animation_library.display()

# Maya Script
"""
import sys
sys.path.append("D:\\development\\code\\python\\projects\\ampt\\src")

import ampt.tools.widgets.tool_window as tool_window
import ampt.tools.widgets.save_animation as save_animation
import ampt.tools.widgets.animation_list as animation_list
reload(animation_list)
reload(save_animation)
reload(tool_window)

import ampt.tools.camel.animation_library as animation_library
reload(animation_library)
"""