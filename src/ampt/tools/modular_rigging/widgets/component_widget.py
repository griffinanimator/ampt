# standard libraries
import os

# third party libraries
from PySide import QtCore, QtGui

# internal libraries
from ampt.data.dict_utils import JSONDict

# application libraries
from ampt.tools.modular_rigging import component

# debug reloads
reload(component)
Component = component.Component

MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))
ICONS_PATH = os.path.join(os.path.split(MODULE_PATH)[0], 'icons')


class ComponentWidget(QtGui.QPushButton):
    def __init__(self, component_path, parent=None):
        super(ComponentWidget, self).__init__(parent)

        component_data = JSONDict(component_path)

        button_layout = QtGui.QHBoxLayout()
        button_layout.setContentsMargins(5, 2, 5, 2)
        button_layout.setAlignment(QtCore.Qt.AlignLeft)

        self.setMinimumHeight(40)

        pixmap = QtGui.QPixmap(os.path.join(ICONS_PATH, component_data.icon))
        label_icon = QtGui.QLabel(self)
        label_icon.setFixedSize(QtCore.QSize(32, 32))
        label_icon.setScaledContents(1)
        label_icon.setPixmap(pixmap)
        label_icon.setAlignment(QtCore.Qt.AlignCenter)

        label_text = QtGui.QLabel(component_data.title)
        label_text.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))

        def install():
            component_object = Component(component_data)
            component_object.install()

        self.clicked.connect(install)

        button_layout.addWidget(label_icon)
        button_layout.addWidget(label_text)

        self.setLayout(button_layout)