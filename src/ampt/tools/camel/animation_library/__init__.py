#import internal libraries
from ampt.data.dict_utils import directory_to_dict
from ampt.tools.widgets.tool_window import ToolWindow
from animation_category_widget import AnimationCategoryWidget
from animation_thumb_grid_widget import AnimationThumbGridWidget
from animation_description_widget import AnimationDescriptionWidget

#import third party libraries
from PySide import QtCore, QtGui
from PySide.QtCore import Signal


class Controller(QtGui.QWidget):
    selection_changed = Signal(list)


class AnimationLibrary(ToolWindow):

    def __init__(self, parent=None):
        super(AnimationLibrary, self).__init__(parent=parent)

        self.title = "Animation Library"
        self.dimensions = QtCore.QRect(0, 0, 980, 480)

        container = QtGui.QWidget(self)
        layout = QtGui.QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        container.setLayout(layout)

        category_widget = AnimationCategoryWidget()
        category_widget.setMinimumWidth(200)
        category_widget.setMaximumWidth(400)
        category_widget.setMinimumHeight(self.height())
        # category_widget.set_data(directory_to_dict("D:\\development\\"))
        category_widget.set_data({"item%s"%i:i for i in range(10)})
        layout.addWidget(category_widget)

        thumb_grid_widget = AnimationThumbGridWidget()
        thumb_grid_widget.setMinimumWidth(500)
        thumb_grid_widget.setMaximumWidth(65000)
        thumb_grid_widget.setMinimumHeight(self.height())

        layout.addWidget(thumb_grid_widget)

        description_widget = AnimationDescriptionWidget()
        description_widget.setMinimumWidth(330)
        description_widget.setMaximumWidth(500)
        description_widget.setMinimumHeight(self.height())
        layout.addWidget(description_widget)

        self.controller = Controller()
        self.controller.selection_changed.connect(self.update_status_bar)

        self.setCentralWidget(container)
        container.update()

    def update_status_bar(self, _selection):
        msg = ""
        if not _selection:
            msg = "Nothing Selected"
        elif len(_selection) == 1:
            msg = "%s selected." % _selection[0]
        else:
            msg = "%s objects selected." % len(_selection)
        self.statusBar().showMessage(msg)


# Maya Script
# import sys
# sys.path.append("D:\\development\\code\\python\\projects\\ampt\\src")
#
# from ampt.tools.camel.animation_library import AnimationLibrary
# from ampt.core.user_interface import get_maya_main_window
#
# maya_main_window = get_maya_main_window()
# for i in maya_main_window.children():
#     cls = type(i).__name__
#     if cls == "AnimationLibrary":
#         i.setParent(None)
#         i.destroy()
#
# animation_library = AnimationLibrary()
# animation_library.display()
#
# import maya.OpenMaya as OpenMaya
# import pymel.core as pm
#
# def emit_selection_changed(_):

# Test Script
if __name__ == "__main__":
    import sys
    import random
    app = QtGui.QApplication(sys.argv)
    test = AnimationLibrary()
    test.display()
    sys.exit(app.exec_())