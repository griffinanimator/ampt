# standard libraries
import os

# third party libraries
from PySide import QtCore, QtGui

# internal libraries
from ampt.core.os_utils import module_path, is_dir
from ampt.core.user_interface import load_interface
from ampt.tools.widgets.tool_window import ToolWindow
from ampt.tools.widgets.vertical_button_list import VerticalButtonList


class SandboxInterface(ToolWindow):
    def __init__(self, parent=None):
        super(SandboxInterface, self).__init__(parent)

        self.title = "Sandbox"
        self.dimensions = QtCore.QRect(0, 0, 320, 480)
        self.setLayout(QtGui.QHBoxLayout(self))
        self.packages = self.find_packages()

        self.package_list = VerticalButtonList(self)
        self.layout().addWidget(self.package_list)

        self.display_packages()

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

    def display_packages(self):
        if len(self.packages):
            for package in self.packages:
                module = self.import_package(package)
                if not module.properties["is_debug"]:
                    continue
                else:
                    self.package_list.add_button(module.properties["title"])
                    self.update()


def load():
    try:
        load_interface(None, SandboxInterface)
    except Exception as e:
        print e.message
        pass


# Test Script
if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    test = SandboxInterface()
    test.display()
    sys.exit(app.exec_())