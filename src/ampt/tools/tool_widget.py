from PySide import QtCore, QtGui


class ToolWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ToolWidget, self).__init__(parent=parent)
        self.setLayout(QtGui.QVBoxLayout())

