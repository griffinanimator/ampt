# standard libraries
import os

MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))
COMPONENTS_PATH = os.path.join(MODULE_PATH, "components").replace("\\", "/")


class ComponentManager():
    _component_instances = {}

    def __init__(self):
        pass

    @staticmethod
    def available_components():
        return [component_file for component_file in ComponentManager.find_component_files()]

    @staticmethod
    def find_component_files():
        return [os.path.join(COMPONENTS_PATH, f).replace("\\", "/") for f in os.listdir(COMPONENTS_PATH) if f.endswith("json")]