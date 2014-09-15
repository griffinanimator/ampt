#import internal libraries
from ampt.tools.widgets.tool_window import ToolWindow
from animation_category_widget import AnimationCategoryWidget
from animation_thumb_grid_widget import AnimationThumbGridWidget
from animation_description_widget import AnimationDescriptionWidget

#import third party libraries
from PySide import QtCore, QtGui


class AnimationLibrary(ToolWindow):
    def __init__(self):
        super(AnimationLibrary, self).__init__()

        self.title = "Animation Library"
        self.dimensions = QtCore.QRect(0, 0, 980, 480)

        container = QtGui.QWidget(self)
        layout = QtGui.QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        container.setLayout(layout)

        category_widget = AnimationCategoryWidget()
        category_widget.setMinimumWidth(200)
        category_widget.setMaximumWidth(200)
        category_widget.setMinimumHeight(self.height())
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

        self.setCentralWidget(container)
        container.update()

# Maya Script
# import sys
# sys.path.append("D:\\development\\code\\python\\projects\\ampt\\src")
#
# import ampt.tools.widgets.tool_window as tool_window
# import ampt.tools.widgets.save_animation as save_animation
# import ampt.tools.widgets.animation_list as animation_list
# reload(animation_list)
# reload(save_animation)
# reload(tool_window)
#
# import ampt.tools.camel.animation_library as animation_library
# reload(animation_library)

# Test Script
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    test = AnimationLibrary()
    test.display()
    sys.exit(app.exec_())