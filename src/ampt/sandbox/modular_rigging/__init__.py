properties = {"title": "Modular Rigging", "is_debug": True}

# third party libraries
from PySide import QtCore, QtGui

# internal libraries
from ampt.tools.widgets.tool_widget import ToolWidget
from ampt.core.user_interface import load_dock_interface

# application libraries
from widgets.layout_section import LayoutSection
from widgets.weighting_section import WeightingSection


class ModularRigging(ToolWidget):
    def __init__(self, parent=None):

        self.title = properties["title"]

        super(ModularRigging, self).__init__(self.title, parent)

        # main widget
        main_layout = QtGui.QVBoxLayout()
        main_layout.setContentsMargins(5, 5, 5, 5)

        menu = QtGui.QMenuBar()
        file_menu = menu.addMenu("File")
        edit_menu = menu.addMenu("Edit")
        main_layout.addWidget(menu)

        main_widget = QtGui.QWidget()

        # header
        header = QtGui.QWidget()
        header_layout = QtGui.QHBoxLayout()
        header_layout.setAlignment(QtCore.Qt.AlignCenter)
        label_text = QtGui.QLabel(self.title)
        label_text.setFont(QtGui.QFont("Arial", 18, QtGui.QFont.Bold))
        header_layout.addWidget(label_text)
        header.setLayout(header_layout)


        sections = QtGui.QTabWidget()
        sections.addTab(LayoutSection(), "Layout")
        sections.addTab(WeightingSection(), "Weighting")
        sections.addTab(QtGui.QWidget(), "Build")

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