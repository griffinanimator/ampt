# standard libraries
import os

# third party libraries
import maya.cmds as cmds

# internal libraries
from filesystem import get_module_path, clean_path
from ..data.dict_utils import JSONDict

MODULE_PATH = get_module_path(__file__)
AMPT_PATH = os.path.split(MODULE_PATH)[0]
SETTINGS_PATH = clean_path(os.path.join(AMPT_PATH, "settings.json"))


class Settings(JSONDict):

    DEFAULT_UNIT = "cm"

    def __init__(self):
        super(Settings, self).__init__(fp=SETTINGS_PATH)

        self.units = self.DEFAULT_UNIT

    #OVERRIDE
    def __setitem__(self, key, value):
        super(Settings, self).__setitem__(key, value)
        if key == "units":
            cmds.currentUnit(linear=value)

        self.__update_json__()
