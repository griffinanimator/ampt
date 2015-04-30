# standard libraries
import os

# third party libraries
from PySide import QtCore, QtGui

MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))


class ComponentWidget(QtGui.QPushButton):
    def __init__(self, parent=None, **properties):
        super(ComponentWidget, self).__init__(parent)

        button_layout = QtGui.QHBoxLayout()
        button_layout.setContentsMargins(2, 2, 2, 2)
        button_layout.setAlignment(QtCore.Qt.AlignLeft)

        self.setMinimumHeight(72)

        pixmap = QtGui.QPixmap(MODULE_PATH + "/icons/" + properties["icon"])
        label_icon = QtGui.QLabel(self)
        label_icon.setFixedSize(QtCore.QSize(64, 64))
        label_icon.setScaledContents(1)
        label_icon.setPixmap(pixmap)
        label_icon.setAlignment(QtCore.Qt.AlignCenter)
        label_text = QtGui.QLabel(properties["title"])
        label_text.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))

        button_layout.addWidget(label_icon)
        button_layout.addWidget(label_text)

        self.setLayout(button_layout)