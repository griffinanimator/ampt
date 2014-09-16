from PySide import QtCore, QtGui


def fill_tree(item, value):
    item.setExpanded(True)
    if type(value) is dict:
        for key, val in sorted(value.iteritems()):
            child = QtGui.QTreeWidgetItem()
            child.setText(0, unicode(key))
            item.addChild(child)
            fill_tree(child, val)
    elif type(value) is list:
        for val in value:
            child = QtGui.QTreeWidgetItem()
            item.addChild(child)
            if type(val) is dict:
                child.setText(0, '[dict]')
                fill_tree(child, val)
            elif type(val) is list:
                child.setText(0, '[list]')
                fill_tree(child, val)
            else:
                child.setText(0, unicode(val))
            child.setExpanded(True)
    else:
        child = QtGui.QTreeWidgetItem()
        child.setText(0, unicode(value))
        item.addChild(child)


class AnimationCategoryWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(AnimationCategoryWidget, self).__init__(parent=parent)

        layout = QtGui.QVBoxLayout(self)
        self.tree = QtGui.QTreeWidget(self)

        self.tree.setHeaderHidden(True)
        self.tree.adjustSize()

        layout.addWidget(self.tree)

        self.setLayout(layout)
        self.update()

    def set_data(self, data):
        self.update_data(data)
        self.update()

    def update_data(self, data):
        self.tree.clear()
        fill_tree(self.tree.invisibleRootItem(), data)