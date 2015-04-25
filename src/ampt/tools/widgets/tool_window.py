from PySide import QtCore, QtGui


class ToolWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):

        super(ToolWindow, self).__init__(parent=parent)
        self.title = "Untitled"
        self.dimensions = QtCore.QRect(0, 0, 1280, 720)

    def set_menus(self):
        self.menuBar().addMenu(QtGui.QMenu("File"))

    def update_status(self, msg):
        self.statusBar().showMessage(msg)

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


# Test Script
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    test = ToolWindow()
    test.display()
    sys.exit(app.exec_())