from PySide import QtCore, QtGui


class ToolWidget(QtGui.QDockWidget):
    def __init__(self, title="Untitled", parent=None):
        super(ToolWidget, self).__init__(title, parent)
        layout = QtGui.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch(1)
        self.setLayout(layout)
