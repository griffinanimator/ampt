# standard libraries
import os

# internal libraries
from ampt.data.dict_utils import JSONDict

MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))
COMPONENTS_PATH = os.path.join(MODULE_PATH, "components").replace("\\", "/")


class Component(JSONDict):
    def __init__(self, name="Untitled", parent=None, child=None):
        file_name = name + ".json"
        file_path = os.path.join(COMPONENTS_PATH, file_name).replace("\\", "/")
        super(Component, self).__init__(file_path)
        self.state = {}
        self.parent = parent
        self.child = child