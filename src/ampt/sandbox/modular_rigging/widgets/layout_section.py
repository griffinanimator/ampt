# standard libraries
import os

# third party libraries
from PySide import QtCore, QtGui

# internal libraries
from ampt.core.filesystem import get_files

# application libraries
from ..component_manager import ComponentManager
from ..widgets.component_widget import ComponentWidget

MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))


class LayoutSection(QtGui.QWidget):
    def __init__(self, parent=None):
        super(LayoutSection, self).__init__(parent)

        self.component_manager = ComponentManager()

        layout = QtGui.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        container = QtGui.QWidget()
        container.setMinimumWidth(320)
        container_layout = QtGui.QVBoxLayout()

        for component in self.component_manager.components:
            container_layout.addWidget(ComponentWidget(component))

        container.setLayout(container_layout)

        scroll_area = QtGui.QScrollArea()
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(0)
        scroll_area.setWidget(container)

        layout.addWidget(scroll_area)

        self.setLayout(layout)

