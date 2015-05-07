# standard libraries
import os

# third party libraries
import pymel.core as pm

MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))
PLUGINS_PATH = os.path.join(MODULE_PATH, "plugins").replace("\\", "/")


def configure_plugins():
    if PLUGINS_PATH not in os.environ["MAYA_PLUG_IN_PATH"]:
        split_path = os.environ["MAYA_PLUG_IN_PATH"].split(";")
        split_path.append(PLUGINS_PATH)
        os.environ["MAYA_PLUG_IN_PATH"] = str(";").join(split_path)

    # REFRESH PLUGIN LIST


def load_plugins():

    def is_loaded(p):
        return True if pm.pluginInfo(p, q=True, l=True) else False

    available_plugins = pm.pluginInfo(q=True, listPlugins=True)
    available_plugin_paths = [pm.pluginInfo(plug, q=True, p=True) for plug in available_plugins]
    loaded_plugins = [plug for plug in available_plugins if is_loaded(plug)]

    # ARE MINE LOADED
    # NO - LOAD THEM
    # YES - UNLOAD and LOAD THEM

    plugins = [os.path.join(PLUGINS_PATH, f) for f in os.listdir()]