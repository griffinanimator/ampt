# third party libraries
from PySide import QtCore, QtGui


class VerticalButtonList(QtGui.QWidget):
    def __init__(self, parent=None):
        super(VerticalButtonList, self).__init__(parent)
        layout = QtGui.QVBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignTop)
        layout.setContentsMargins(10, 5, 10, 5)
        self.setLayout(layout)
        self.setMinimumWidth(320)

# Test Script
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    test = VerticalButtonList()
    for i in range(10):
        test.layout().addWidget(QtGui.QPushButton(str(i)))
    test.show()
    sys.exit(app.exec_())