properties = {"title": "Modular Rigging", "is_debug": True}

# standard libraries
import os

# third party libraries
from PySide import QtCore, QtGui

# internal libraries
from ampt.tools.widgets.tool_widget import ToolWidget
from ampt.tools.widgets.reload_button import ReloadButton
from ampt.core.user_interface import load_dock_interface

# application libraries
from widgets.layout_section import LayoutSection
from widgets.weighting_section import WeightingSection


class ModularRigging(ToolWidget):

    MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))
    SANDBOX_PATH = os.path.abspath(os.path.split(MODULE_PATH)[0]).replace("\\", "/")
    COMPONENTS_PATH = os.path.join(SANDBOX_PATH, "components").replace("\\", "/")

    def __init__(self, parent=None):

        self.title = properties["title"]

        super(ModularRigging, self).__init__(self.title, parent)

        # main widget
        main_layout = QtGui.QVBoxLayout()
        main_layout.setContentsMargins(5, 5, 5, 5)

        menu = QtGui.QMenuBar()
        file_menu = menu.addMenu("File")
        edit_menu = menu.addMenu("Edit")
        help_menu = menu.addMenu("Help")
        main_layout.addWidget(menu)

        main_widget = QtGui.QWidget()

        # header
        header = QtGui.QWidget()
        header_layout = QtGui.QHBoxLayout()
        header_layout.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        header.setLayout(header_layout)

        # tabbed sections
        sections = QtGui.QTabWidget()
        sections.addTab(LayoutSection(self), "Layout")
        # sections.addTab(WeightingSection(self), "Weighting")
        # sections.addTab(QtGui.QWidget(self), "Build")

        main_layout.addWidget(header)
        main_layout.addWidget(sections)
        main_widget.setLayout(main_layout)

        self.setWidget(main_widget)


def load():
    try:
        load_dock_interface(None, ModularRigging)
    except Exception as e:
        print e.message
        pass