from PySide import QtGui


class AnimationThumbGridWidget(QtGui.QListWidget):
    def __init__(self, parent=None):
        super(AnimationThumbGridWidget, self).__init__(parent=parent)

        layout = QtGui.QGridLayout(self)

        scroll_area = QtGui.QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        self.setLayout(layout)
        self.update()