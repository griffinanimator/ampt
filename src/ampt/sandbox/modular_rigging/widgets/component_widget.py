# standard libraries
import os

# third party libraries
from PySide import QtCore, QtGui

MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))
SANDBOX_PATH = os.path.abspath(os.path.split(MODULE_PATH)[0]).replace("\\", "/")


class ComponentWidget(QtGui.QPushButton):
    def __init__(self, module, parent=None):
        super(ComponentWidget, self).__init__(parent)

        button_layout = QtGui.QHBoxLayout()
        button_layout.setContentsMargins(5, 2, 5, 2)
        button_layout.setAlignment(QtCore.Qt.AlignLeft)

        self.setMinimumHeight(40)

        pixmap = QtGui.QPixmap(SANDBOX_PATH + "/icons/" + module.properties["icon"])
        label_icon = QtGui.QLabel(self)
        label_icon.setFixedSize(QtCore.QSize(32, 32))
        label_icon.setScaledContents(1)
        label_icon.setPixmap(pixmap)
        label_icon.setAlignment(QtCore.Qt.AlignCenter)

        label_text = QtGui.QLabel(module.properties["title"])
        label_text.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))

        self.clicked.connect(module.load)

        button_layout.addWidget(label_icon)
        button_layout.addWidget(label_text)

        self.setLayout(button_layout)