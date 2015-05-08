# standard libraries
import os
import sys

# third party libraries
import maya.cmds as cmds

# internal libraries
from core.filesystem import get_module_path, clean_path
from core.setup import add_script_path, add_plugin_path

# declare environment paths
MODULE_PATH = get_module_path(__file__)
PLUGINS_PATH = clean_path(os.path.join(MODULE_PATH, "plugins"))
SCRIPTS_PATH = clean_path(os.path.join(MODULE_PATH, "tools/third_party"))

# configure environment
add_plugin_path(PLUGINS_PATH)
add_script_path(SCRIPTS_PATH)

cmds.evalDeferred("import ampt.post_startup")