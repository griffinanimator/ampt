# standard libraries
import os

# third party libraries
from PySide import QtCore, QtGui

# internal libraries
from ampt.core.os_utils import get_files

# application libraries
from ampt.sandbox.modular_rigging.widgets.component_widget import ComponentWidget


class LayoutSection(QtGui.QWidget):
    MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))
    COMPONENTS_PATH = os.path.join(MODULE_PATH, "components").replace("\\", "/")

    def __init__(self, parent=None):
        super(LayoutSection, self).__init__(parent)

        layout = QtGui.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        container = QtGui.QWidget()
        container.setMinimumWidth(320)
        container_layout = QtGui.QVBoxLayout()

        search_widget = QtGui.QWidget()
        search_layout = QtGui.QHBoxLayout()

        # search_label = QtGui.QLabel("Search: ")
        # search_entry = QtGui.QLineEdit()
        # search_button = QtGui.QPushButton()

        # search_layout.addWidget(search_label)
        # search_layout.addWidget(search_entry)
        # search_layout.addWidget(search_button)

        # search_widget.setLayout(search_layout)

        container_layout.addWidget(search_widget)

        for component in self.components:
            base_module_name = str(".").join(__name__.split(".")[:-2])
            module_name = str(".").join([base_module_name, "components", component])
            module = __import__(module_name, {}, {}, [component])
            if hasattr(module, "properties"):
                container_layout.addWidget(ComponentWidget(module))

        container.setLayout(container_layout)

        scroll_area = QtGui.QScrollArea()
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(0)
        scroll_area.setWidget(container)

        layout.addWidget(scroll_area)

        self.setLayout(layout)

    @property
    def components(self):
        return [os.path.split(f)[-1:][0].split(".")[0] for f in get_files(COMPONENTS_PATH, "py")]