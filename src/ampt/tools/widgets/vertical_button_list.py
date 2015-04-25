# third party libraries
from PySide import QtGui


class VerticalButtonList(QtGui.QWidget):
    def __init__(self, parent=None):
        super(VerticalButtonList, self).__init__(parent)

        self.layout = QtGui.QVBoxLayout(self)
        self.buttons = list()

        self.setLayout(self.layout)
        self.update()

    def add_button(self, label="ButtonName"):
        self.buttons.append(QtGui.QPushButton(label))
        self.update_buttons()

    def update_buttons(self):
        for button in self.buttons:
            self.layout.addWidget(button)
            self.update()


# Test Script
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    test = VerticalButtonList()
    test.add_button("MyButton")
    test.show()
    sys.exit(app.exec_())