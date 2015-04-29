# third party libraries
from PySide import QtCore, QtGui


class VerticalButtonList(QtGui.QWidget):
    def __init__(self, parent=None):
        super(VerticalButtonList, self).__init__(parent)
        self.setMinimumWidth(320)

# Test Script
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    test = VerticalButtonList()
    for i in range(10):
        test.vcontainer.addWidget(QtGui.QPushButton(str(i)))
    test.show()
    sys.exit(app.exec_())