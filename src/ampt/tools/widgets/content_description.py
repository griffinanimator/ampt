from PySide import QtGui


class ContentDescriptionWidget(QtGui.QListWidget):
    def __init__(self, parent=None):
        super(ContentDescriptionWidget, self).__init__(parent=parent)

        layout = QtGui.QVBoxLayout(self)

        scroll_area = QtGui.QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        self.setLayout(layout)
        self.update()

# Test Script
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    test = ContentDescriptionWidget()
    test.show()
    sys.exit(app.exec_())