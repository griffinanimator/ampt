from PySide import QtCore, QtGui


class AnimationList(QtGui.QWidget):
    def __init__(self, parent=None):
        super(AnimationList, self).__init__(parent=parent)

        self.main_layout = QtGui.QGridLayout(self)

        self.tree_widget = QtGui.QTreeWidget(self)
        self.tree_widget.setColumnCount(1)
        self.tree_widget.insertTopLevelItems(0, self.fbx_categories)
        self.tree_widget.adjustSize()
        self.tree_widget.adjustSize()

        self.file_grid = QtGui.QWidget(self)
        self.file_layout = QtGui.QGridLayout(self.file_grid)

        for i in range(len(self.fbx_files)):
            btn = QtGui.QPushButton("test" + str(i))
            self.file_layout.addWidget(btn, i, 0, i)
            btn.clicked.connect(self.buttonClicked)

        self.scroll = QtGui.QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.scroll.setWidget(self.file_grid)

        self.file_layout.addWidget(self.scroll, 3, 0)
        #self.setLayout(self.grid_widget_layout)
        self.adjustSize()

    def buttonClicked(self):
        title = QtGui.QLabel('Title' + str(self.layout.count()))
        self.layout.addWidget(title)

    @property
    def fbx_categories(self):
        files = []
        for i in range(10):
            files.append(QtGui.QTreeWidgetItem(None, ["category: %s" % i]))
        return files

    @property
    def fbx_files(self):
        files = []
        for i in range(10):
            files.append(QtGui.QTreeWidgetItem(None, ["file: %s" % i]))
        return files

# Test Script
# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     test = AnimationList()
#     test.show()
#     sys.exit(app.exec_())