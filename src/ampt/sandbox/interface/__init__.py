# standard libraries
import os

# third party libraries
from PySide import QtCore, QtGui

# internal libraries
from ampt.core.os_utils import module_path, is_dir
from ampt.core.user_interface import load_dock_interface, add_menu
from ampt.tools.widgets.tool_widget import ToolWidget
from ampt.tools.widgets.vertical_button_list import VerticalButtonList

MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))


class SandboxInterface(ToolWidget):
    def __init__(self, parent=None):

        self.title = "Sandbox"

        super(SandboxInterface, self).__init__(self.title, parent)

        # header
        header = QtGui.QWidget()
        header_layout = QtGui.QHBoxLayout()
        header_layout.setAlignment(QtCore.Qt.AlignCenter)
        pixmap = QtGui.QPixmap(MODULE_PATH+"/sandbox.png")
        label_icon = QtGui.QLabel(self)
        label_icon.setFixedSize(QtCore.QSize(128, 86))
        label_icon.setScaledContents(1)
        label_icon.setPixmap(pixmap)
        label_icon.setAlignment(QtCore.Qt.AlignCenter)
        label_text = QtGui.QLabel("Sandbox")
        label_text.setFont(QtGui.QFont( "Arial", 18, QtGui.QFont.Bold))
        header_layout.addWidget(label_icon)
        header_layout.addWidget(label_text)
        header.setLayout(header_layout)

        # build data and tool widget
        packages = self.find_packages()
        package_list = VerticalButtonList(self)

        # add widgets
        package_list.layout().addWidget(header)
        for package in packages:
            # import the package module to access properties dict()
            # this module obj drops out of scope after this loop completes
            package_module = self.import_package(package)
            # only add packages that are marked for debug
            if package_module.properties["is_debug"]:
                package_name = package_module.properties["title"]
                # build the package button and add to the package list layout
                package_button = QtGui.QPushButton(package_name, package_list)
                package_button.clicked.connect(package_module.load)  # callback
                package_list.layout().addWidget(package_button)

        # set the tool widget
        self.setWidget(package_list)

    @staticmethod
    def find_packages():
        root_split = os.path.split(module_path(__file__))[0].split('/')[:-1]
        root = str('/').join(root_split)
        packages = [i for i in os.listdir(root) if is_dir(root, i) and i != "interface"]
        return packages

    @staticmethod
    def import_package(package_name):
        module_name = "ampt.sandbox." + package_name
        module = __import__(module_name, {}, {}, [package_name])
        reload(module)  # DEBUG_HACK
        return module


def load():
    try:
        load_dock_interface(None, SandboxInterface)
    except Exception as e:
        print e.message
        pass