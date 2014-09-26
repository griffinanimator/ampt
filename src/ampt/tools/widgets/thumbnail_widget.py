from PySide import QtGui


class ThumbnailWidget(QtGui.QListWidget):
    def __init__(self, parent=None):
        super(ThumbnailWidget, self).__init__(parent=parent)

        layout = QtGui.QGridLayout(self)

        scroll_area = QtGui.QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        self.setLayout(layout)
        self.update()

# Test Script
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    test = ThumbnailWidget()
    test.show()
    sys.exit(app.exec_())