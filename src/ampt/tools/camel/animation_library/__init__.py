#import internal libraries
from ampt.tools.widgets.tool_window import ToolWindow

import animation_category_widget as acw
reload(acw)
from animation_category_widget import AnimationCategoryWidget

from animation_thumb_grid_widget import AnimationThumbGridWidget
from animation_description_widget import AnimationDescriptionWidget

#import third party libraries
from PySide import QtCore, QtGui
Signal = QtCore.Signal


class AnimationLibrary(ToolWindow):

    selection_changed = Signal(list)

    def __init__(self, parent=None):
        super(AnimationLibrary, self).__init__(parent=parent)

        self.title = "Animation Library"
        self.dimensions = QtCore.QRect(0, 0, 980, 480)

        container = QtGui.QWidget(self)
        layout = QtGui.QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        container.setLayout(layout)

        self.category_widget = AnimationCategoryWidget()
        self.category_widget.setMinimumWidth(200)
        self.category_widget.setMaximumWidth(400)
        self.category_widget.setMinimumHeight(self.height())
        layout.addWidget(self.category_widget)

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

        self.selection_changed.connect(self.update_status_bar)
        self.selection_changed.connect(self.set_category_selection)

        self.setCentralWidget(container)

        self.update_status_bar([])
        container.update()

    def update_status_bar(self, _selection):
        if not _selection:
            msg = "Nothing Selected"
        elif len(_selection) == 1:
            msg = "%s selected." % _selection[0]
        else:
            msg = "%s objects selected." % len(_selection)
        self.statusBar().showMessage(msg)

    def set_categories(self, data):
        if len(data):
            self.category_widget.set_data(data)
        else:
            self.category_widget.set_data([])

    def set_category_selection(self, _item):
        self.category_widget.tree.setCurrentItem(_item)


# Maya Script
def load():
    try:
        from ampt.core.user_interface import get_maya_main_window
        import maya.OpenMaya as om
        import pymel.core as pm

        maya_main_window = get_maya_main_window()

        for i in maya_main_window.children():
            cls = type(i).__name__
            if cls == "AnimationLibrary":
                i.setParent(None)
                i.destroy()

        application = AnimationLibrary(maya_main_window)

        def on_selection_changed(_):
            application.selection_changed.emit(pm.selected(type="transform"))
            application.category_widget.set_current_item(pm.selected(type="transform"))

        om.MEventMessage.addEventCallback('SelectionChanged', on_selection_changed)

        application.category_widget.set_data(pm.ls(dag=True))

        application.display()

    except Exception as e:
        print e.message()
        pass

# Test Script
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    test = AnimationLibrary()
    test.display()
    sys.exit(app.exec_())