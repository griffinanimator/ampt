# standard libraries
import os

# internal libraries
from ampt.data.dict_utils import JSONDict

MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))
COMPONENTS_PATH = os.path.join(MODULE_PATH, "components").replace("\\", "/")


class Component(object):
    def __init__(self, file_path, parent=None, child=None):
        self.__dict__.update(JSONDict(file_path))

    def info(self):
        print self.summary