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
        return ("head", _head) if _head else None

    @property
    def tail(self):
        _tail = self.layout["tail"] if self.layout else None
        return ("tail", _tail) if _tail else None

    @property
    def elements(self):
        _elements = collections.OrderedDict()
        if self.head and self.tail:
            for key, value in self.layout.iteritems():
                if key not in ["head", "tail"]:
                    index = value["index"]
                    print "foo: ", index
                    _elements[index+1] = (key, value)
        _elements[0] = self.head
        _elements[len(_elements) + 1] = self.tail
        return _elements

    def dump_data(self, file_path):
        output = JSONDict(file_path)
        output.update(self.data)

    def create_component_node(self):
        print self.elements

