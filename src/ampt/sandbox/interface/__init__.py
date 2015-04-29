# standard libraries
import os

# third party libraries
from PySide import QtCore, QtGui

# internal libraries
from ampt.core.os_utils import module_path, is_dir
from ampt.core.user_interface import load_dock_interface, add_menu
from ampt.tools.widgets.tool_widget import ToolWidget
from ampt.tools.widgets.vertical_button_list import VerticalButtonList


class SandboxInterface(ToolWidget):
    def __init__(self, parent=None):

        self.title = "Sandbox"

        super(SandboxInterface, self).__init__(self.title, parent)

        packages = self.find_packages()
        package_list = VerticalButtonList(self)
        self.setWidget(package_list)
        for package in packages:
            package_module = self.import_package(package)
            package_name = package_module.properties["title"]
            package_button = QtGui.QPushButton(package_name, package_list)
        self.update()

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