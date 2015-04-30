properties = {"title": "Modular Rigging System", "is_debug": True}

# third party libraries
from PySide import QtCore, QtGui

# internal libraries
from ampt.tools.widgets.tool_widget import ToolWidget
from ampt.core.user_interface import load_dock_interface

# application libraries
from layout_section import LayoutSection


class ModularRigginSystem(ToolWidget):
    def __init__(self, parent=None):

        self.title = properties["title"]

        super(ModularRigginSystem, self).__init__(self.title, parent)

        # header
        header = QtGui.QWidget()
        header_layout = QtGui.QHBoxLayout()
        header_layout.setAlignment(QtCore.Qt.AlignCenter)
        label_text = QtGui.QLabel(self.title)
        label_text.setFont(QtGui.QFont("Arial", 18, QtGui.QFont.Bold))
        header_layout.addWidget(label_text)
        header.setLayout(header_layout)

        # main widget
        main_layout = QtGui.QVBoxLayout()
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_widget = QtGui.QWidget()

        sections = QtGui.QTabWidget()
        sections.addTab(LayoutSection(), "Layout")
        sections.addTab(QtGui.QWidget(), "Weighting")
        sections.addTab(QtGui.QWidget(), "Build")

        main_layout.addWidget(header)
        main_layout.addWidget(sections)
        main_widget.setLayout(main_layout)

        self.setWidget(main_widget)


def load():
    try:
        load_dock_interface(None, ModularRigginSystem)
    except Exception as e:
        print e.message
        pass