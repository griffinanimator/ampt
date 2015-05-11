# standard libraries
import os

# internal libraries
from ampt.data.dict_utils import JSONDict

# third party libraries
import pymel.core as pm

MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))
COMPONENTS_PATH = os.path.join(MODULE_PATH, "components").replace("\\", "/")


class Component(object):
    def __init__(self, data, parent=None, child=None):
        self.data = data

    def install(self):
        print "fuck"
        for name, position in self.data["layout"]["controls"].iteritems():

            # create component nodes
            pm.select(clear=True)
            component_node = pm.createNode("component_contol_sphere", name = name+"_component")
            pm.select(clear=True)