# standard libraries
import os

# application libraries
from component import Component

MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))
COMPONENTS_PATH = os.path.join(MODULE_PATH, "components").replace("\\", "/")


class ComponentManager():
    def __init__(self):
        self.components = self.load_components()

    def load_components(self):
        return [Component(component_file) for component_file in self.find_component_files()]

    @staticmethod
    def find_component_files():
        return [os.path.join(COMPONENTS_PATH, f).replace("\\", "/") for f in os.listdir(COMPONENTS_PATH) if f.endswith("json")]
