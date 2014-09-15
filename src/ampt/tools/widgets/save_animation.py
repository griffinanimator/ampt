from PySide import QtGui


class SaveAnimation(QtGui.QWidget):
    def __init__(self, parent=None):
        super(SaveAnimation, self).__init__(parent=parent)


        layout = QtGui.QGridLayout()

        input_label = QtGui.QLabel("Animation Name")
        input_field = QtGui.QLineEdit(self)
        button = QtGui.QPushButton("Save", self)

        layout.addWidget(input_label, 0, 0)
        layout.addWidget(input_field, 1, 0)
        layout.addWidget(button, 1, 2)

        self.setLayout(layout)
        self.adjustSize()
