# standard libraries
import os

# third party libraries
from PySide import QtCore, QtGui

# internal libraries

# application libraries
from ampt.tools.modular_rigging import component_manager
from ampt.tools.modular_rigging.widgets import component_widget

# debug reloads
reload(component_manager)
reload(component_widget)
ComponentManager = component_manager.ComponentManager
ComponentWidget = component_widget.ComponentWidget

MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))


class LayoutSection(QtGui.QWidget):
    def __init__(self, parent=None):
        super(LayoutSection, self).__init__(parent)

        layout = QtGui.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        container = QtGui.QWidget()
        container.setMinimumWidth(320)
        container_layout = QtGui.QVBoxLayout()

        for component_path in ComponentManager.available_components():
            container_layout.addWidget(ComponentWidget(component_path))

        container.setLayout(container_layout)

        scroll_area = QtGui.QScrollArea()
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(0)
        scroll_area.setWidget(container)

        layout.addWidget(scroll_area)

        self.setLayout(layout)

