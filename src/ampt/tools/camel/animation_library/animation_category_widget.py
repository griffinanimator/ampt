from PySide import QtGui


class AnimationCategoryWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(AnimationCategoryWidget, self).__init__(parent=parent)

        layout = QtGui.QVBoxLayout(self)

        tree = QtGui.QTreeWidget(self)
        tree.setColumnCount(1)

        items = []

        for i in range(10):
            items.append(QtGui.QTreeWidgetItem(["item: %s" % i]))

        tree.insertTopLevelItems(0, items)
        tree.adjustSize()

        layout.addWidget(tree)

        self.setLayout(layout)
        self.update()