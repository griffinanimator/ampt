#import internal libraries
import ampt.tools.widgets.content_outliner as content_outliner
reload(content_outliner)

from ampt.tools.widgets.tool_window import ToolWindow
from ampt.tools.widgets.content_outliner import ContentOutlinerWidget
from ampt.tools.widgets.content_thumbnails import ContentThumbnailsWidget
from ampt.tools.widgets.content_description import ContentDescriptionWidget

#import third party libraries
from PySide import QtCore, QtGui
Signal = QtCore.Signal


class ContentLibrary(ToolWindow):

    selection_changed = Signal(list)

    def __init__(self, parent=None):
        super(ContentLibrary, self).__init__(parent=parent)

        self.title = "Content Library"
        self.status_bar_msg = "Ready"

        container = QtGui.QWidget(self)
        layout = QtGui.QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        container.setLayout(layout)

        self.outliner = ContentOutlinerWidget()
        self.outliner.setMinimumWidth(200)
        self.outliner.setMaximumWidth(400)
        self.outliner.setMinimumHeight(self.height())
        layout.addWidget(self.outliner)

        thumbnails = ContentThumbnailsWidget()
        thumbnails.setMinimumWidth(500)
        thumbnails.setMaximumWidth(65000)
        thumbnails.setMinimumHeight(self.height())

        layout.addWidget(thumbnails)

        description = ContentDescriptionWidget()
        description.setMinimumWidth(330)
        description.setMaximumWidth(500)
        description.setMinimumHeight(self.height())
        layout.addWidget(description)

        self.setCentralWidget(container)

        self.update_status_bar()
        container.update()

    def update_status_bar(self):
        self.statusBar().showMessage(self.status_bar_msg)


# Test Script
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    test = ContentLibrary()
    test.display()
    sys.exit(app.exec_())