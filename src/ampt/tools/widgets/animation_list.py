from PySide import QtGui


class AnimationList(QtGui.QWidget):
    def __init__(self, parent = None):
        super(AnimationList, self).__init__(parent=parent)

        main_layout = QtGui.QVBoxLayout()

        self.list = QtGui.QListWidget(self)

        for i in range(10):
            self.list.addItem("Item %s" % (i+1))

        main_layout.addWidget(self.list)