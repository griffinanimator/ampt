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
    DEFAULT_AXIS = "y"

    def __init__(self, file_path=None):

        if not file_path:
            file_path = SETTINGS_PATH

        super(Settings, self).__init__(fp=file_path)

        if "units" in self:
            cmds.currentUnit(linear=self.units)
        else:
            self.units = self.DEFAULT_UNIT

        if "up_axis" in self:
            cmds.upAxis(ax=self.up_axis, rv=True)
        else:
            self.up_axis = self.DEFAULT_AXIS

    #OVERRIDE
    def __setitem__(self, key, value):
        super(Settings, self).__setitem__(key, value)

        if key == "units":
            cmds.currentUnit(linear=value)

        if key == "up_axis":
            cmds.upAxis(ax=value, rv=True)

        self.__update_json__()
