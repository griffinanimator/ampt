# standard libraries
import os

# third party libraries
from PySide import QtCore, QtGui

# internal libraries
from ampt.tools.widgets.tool_widget import ToolWidget
from ampt.core.user_interface import load_dock_interface

# application libraries
import widgets.layout_section as layout_section
reload(layout_section)
LayoutSection = layout_section.LayoutSection


class Interface(ToolWidget):

    MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))
    COMPONENTS_PATH = os.path.join(MODULE_PATH, "components").replace("\\", "/")
    TITLE = "Modular Rigging"

    def __init__(self, parent=None):

        super(Interface, self).__init__(self.TITLE, parent)

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

        main_layout.addWidget(header)
        main_layout.addWidget(sections)
        main_widget.setLayout(main_layout)

        self.setWidget(main_widget)


def load():
    try:
        load_dock_interface(None, Interface)
    except Exception as e:
        print e.message
        pass