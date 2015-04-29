from PySide import QtCore, QtGui


class ToolWidget(QtGui.QDockWidget):
    def __init__(self, title="Untitled", parent=None):
        super(ToolWidget, self).__init__(title, parent)
