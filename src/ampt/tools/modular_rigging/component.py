# standard libraries
import os
import collections

# internal libraries
from ampt.data.dict_utils import JSONDict

# third party libraries
import pymel.core as pm

MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))
COMPONENTS_PATH = os.path.join(MODULE_PATH, "components").replace("\\", "/")


class Component(object):
    def __init__(self, data, parent=None, children=None):
        self.data = data or dict()
        self.parent = parent
        self.children = children or list()

    @property
    def has_parent(self):
        return True if self.parent else False

    @property
    def has_children(self):
        if self.children:
            if isinstance(self.children, list) or isinstance(self.children, tuple):
                return True if len(self.children) else False
        return False

    @property
    def name(self):
        _name = self.data["name"] or None
        return _name if _name else None

    @property
    def layout(self):
        layout = self.data["layout"] or None
        return layout if layout else None

    @property
    def head(self):
        _head = self.layout["head"] if self.layout else None
        return _head if _head else None

    @property
    def tail(self):
        _tail = self.layout["tail"] if self.layout else None
        return _tail if _tail else None

    @property
    def elements(self):
        container = collections.OrderedDict()
        container["head"] = self.head

        for key, value in sorted(self.layout.iteritems(), key=lambda (k, v): (v, k)):
            if key not in ["head", "tail"]:
                index = value["index"]
                container[key] = value

        container["tail"] = self.tail
        return container

    def dump_data(self, file_path):
        output = JSONDict(file_path)
        output.update(self.data)

    def create_component_node(self):
        for key, value in self.elements.items():
            name = key
            position = value['position']

            transform = pm.nt.Transform(name=name)
            transform.setTranslation(position, 'world')
            node = pm.createNode("AMPT_Component_Control", p=transform, n=name+"_Shape")