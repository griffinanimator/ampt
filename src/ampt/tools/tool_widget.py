from PySide import QtGui
from ..core.user_interface import get_maya_main_window


class ToolWidget(QtGui.QMainWindow):

    def __init__(self, title="Untitlted"):
        super(ToolWidget, self).__init__(parent=self._parent)
        self.setWindowTitle(title)
        self.setGeometry(0, 0, 1280, 720)
        self._center()

    @property
    def _parent(self):
        return get_maya_main_window()

    def _center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        x = (screen.width() - self.width()) * 0.5
        y = (screen.width() - self.width()) * 0.25
        self.move(x, y)