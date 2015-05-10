# standard libraries
import os

# internal libraries
from ampt.data.dict_utils import JSONDict

# third party libraries
import pymel.core as pm

MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))
COMPONENTS_PATH = os.path.join(MODULE_PATH, "components").replace("\\", "/")


class Component(object):
    def __init__(self, file_path, parent=None, child=None):
        self.__dict__.update(JSONDict(file_path))
        self.joints = list()

    def layout_joints(self):
        for name, position in self.layout["controls"].iteritems():
            pm.select(clear=True)
            self.joints.append(pm.nt.Joint(name=name, position=position))
            pm.select(clear=True)

    def info(self):
        print self.summary
        print self.layout['controls']