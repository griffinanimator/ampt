# standard libraries
import os

# third party libraries
from PySide import QtGui

# application libraries

MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))
SANDBOX_PATH = os.path.abspath(os.path.split(MODULE_PATH)[0]).replace("\\", "/")
COMPONENTS_PATH = os.path.join(SANDBOX_PATH, "components").replace("\\", "/")


class BuildingSection(QtGui.QWidget):
    def __init__(self, parent=None):
        super(BuildingSection, self).__init__(parent)

        layout = QtGui.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)