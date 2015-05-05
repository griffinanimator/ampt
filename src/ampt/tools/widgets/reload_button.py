# standard libraries
import os

# third party libraries
from PySide import QtCore, QtGui

MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))


class ReloadButton(QtGui.QPushButton):
    def __init__(self, parent=None):
        super(ReloadButton, self).__init__(parent)

        button_layout = QtGui.QHBoxLayout()
        button_layout.setContentsMargins(2, 2, 2, 2)
        # button_layout.setAlignment(QtCore.Qt.AlignLeft)

        self.setMinimumWidth(24)
        self.setMaximumWidth(24)
        self.setMinimumHeight(24)
        self.setMaximumHeight(24)

        pixmap = QtGui.QPixmap(MODULE_PATH + "/images/reload.png")
        label_icon = QtGui.QLabel(self)
        label_icon.setFixedSize(QtCore.QSize(22, 22))
        label_icon.setScaledContents(1)
        label_icon.setPixmap(pixmap)
        label_icon.setAlignment(QtCore.Qt.AlignCenter)

        button_layout.addWidget(label_icon)

        self.setLayout(button_layout)