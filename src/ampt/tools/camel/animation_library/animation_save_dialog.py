from PySide import QtGui


class SaveAnimationDialog(QtGui.QWidget):
    def __init__(self, parent=None):
        super(SaveAnimationDialog, self).__init__(parent=parent)

        layout = QtGui.QGridLayout()

        input_label = QtGui.QLabel("Animation Name")
        input_field = QtGui.QLineEdit(self)
        button = QtGui.QPushButton("Save", self)

        layout.addWidget(input_label, 0, 0)
        layout.addWidget(input_field, 1, 0)
        layout.addWidget(button, 1, 2)

        self.setLayout(layout)
        self.adjustSize()

# Test Script
# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     test = SaveAnimationDialog()
#     test.show()
#     sys.exit(app.exec_())