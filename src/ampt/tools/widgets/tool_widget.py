from PySide import QtCore, QtGui


class ToolWidget(QtGui.QDockWidget):
    def __init__(self, parent=None):
        self.title = "Untitled"
        self.dimensions = QtCore.QRect(0, 0, 1280, 720)
        super(ToolWidget, self).__init__(self.title, parent=parent)
        self.setObjectName(self.title)

    def display(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.dimensions)