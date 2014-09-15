from PySide import QtCore, QtGui


class ToolWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):

        super(ToolWindow, self).__init__(parent=parent)
        self.title = "Untitled"
        self.dimensions = QtCore.QRect(0, 0, 1280, 720)

    def display(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.dimensions)
        self.move(self.screen_center)
        self.show()

    @property
    def screen_center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        x = (screen.width() - self.width()) * 0.5
        y = (screen.width() - self.width()) * 0.25
        return QtCore.QPoint(x, y)


# Maya Code
# maya_main_window = get_maya_main_window()
#
# def flush():
#     for i in maya_main_window.children():
#         cls = type(i).__name__
#         if cls == self.__class__.__name__:
#             i.setParent(None)
#             i.destroy()

# Test Script
# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     test = ToolWindow()
#     test.display()
#     sys.exit(app.exec_())