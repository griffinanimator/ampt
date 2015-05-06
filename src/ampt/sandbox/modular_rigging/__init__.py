# standard libraries
import os

# third party libraries
import pymel.core as pm

# application libraries
from interface import load

properties = {"title": "Modular Rigging", "is_debug": True}

MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))
PLUGINS_PATH = os.path.join(MODULE_PATH, "plugins").replace("\\", "/")


def load_plugins():

    def is_loaded(p):
        return True if pm.pluginInfo(p, q=True, l=True) else False

    loaded_plugins = [plug for plug in pm.pluginInfo(q=True, listPlugins=True) if is_loaded(plug)]
    modular_rigging_plugin_paths = [os.path.join(PLUGINS_PATH, f).replace("\\", "/") for f in os.listdir(PLUGINS_PATH)]

    loaded_paths = [pm.pluginOnfo(plug, q=True, p=True) for plug in loaded_plugins]

    for plugged in loaded_paths:
        pm.unloadPlugin(plugged)

    unloaded_paths = [f for f in modular_rigging_plugin_paths if f not in loaded_paths]

    for unplugged in unloaded_paths:
        pm.loadPlugin(unplugged)