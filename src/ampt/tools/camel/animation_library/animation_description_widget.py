from PySide import QtGui


class AnimationDescriptionWidget(QtGui.QListWidget):
    def __init__(self, parent=None):
        super(AnimationDescriptionWidget, self).__init__(parent=parent)

        layout = QtGui.QVBoxLayout(self)

        scroll_area = QtGui.QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        self.setLayout(layout)
        self.update()