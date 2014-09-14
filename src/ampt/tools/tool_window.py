from PySide import QtCore, QtGui
from ..core.user_interface import get_maya_main_window


class ToolWindow(QtGui.QMainWindow):
    def __init__(self, title="Untitled"):
        maya_main_window = get_maya_main_window()

        def flush():
            for i in maya_main_window.children():
                cls = type(i).__name__
                if cls == self.__class__.__name__:
                    i.setParent(None)
                    i.destroy()

        def build():
            super(ToolWindow, self).__init__(parent=maya_main_window)
            self.title = title
            self.dimensions = QtCore.QRect(0, 0, 1280, 720)

        flush()
        build()

    def display(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, 1280, 720)
        self.move(self.screen_center)


    @property
    def screen_center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        x = (screen.width() - self.width()) * 0.5
        y = (screen.width() - self.width()) * 0.25
        return QtCore.QPoint(x, y)