# # standard libraries
# import os
#
# # application libraries
# from ampt.sandbox.modular_rigging.plugins.component import Component
#
# MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))
# COMPONENTS_PATH = os.path.join(MODULE_PATH, "components").replace("\\", "/")
#
#
# class ComponentManager():
#     def __init__(self):
#         self.components = self.load_components()
#
#     def load_components(self):
#         return [Component(component_file) for component_file in self.find_component_files()]
#
#
#
#     @staticmethod
#     def find_component_files():
#         return [os.path.join(COMPONENTS_PATH, f).replace("\\", "/") for f in os.listdir(COMPONENTS_PATH) if f.endswith("json")]

# standard libraries
import sys

# third party libraries
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

# node properties
node_name = "mr_component_manager"
node_id = OpenMaya.MTypeId(0x87636)


class MRComponentManagerNode(OpenMayaMPx.MPxLocatorNode):
    def __init__(self):
        OpenMayaMPx.MPxTransform.__init__(self)

    def compute(self, plug, dataBlock):
        return OpenMaya.kUnknownParameter

    @staticmethod
    def creator():
        return OpenMayaMPx.asMPxPtr(MRComponentManagerNode())

    @staticmethod
    def initializer():
        n_attr = OpenMaya.MFnNumericAttribute()

        MRComponentManagerNode.color = n_attr.createColor("color", "c")
        n_attr.setDefault( 0.1, 0.1, 0.8 );
        n_attr.setKeyable(True);
        n_attr.setReadable(True);
        n_attr.setWritable(True);
        n_attr.setStorable(True);

        MRComponentManagerNode.addAttribute(MRComponentManagerNode.color)


def initializePlugin(m_object):
    try:
        m_plugin = OpenMayaMPx.MFnPlugin(m_object, "3devartist", "0.0.1", "Any")

        m_plugin.registerNode(node_name, node_id,
                              MRComponentManagerNode.creator, MRComponentManagerNode.initializer,
                              OpenMayaMPx.MPxTransform.kDependNode)
    except:
        sys.stderr.write("Failed to register node: %s" % node_name)
        raise


def uninitializePlugin(m_object):
    try:
        m_plugin = OpenMayaMPx.MFnPlugin(m_object)
        m_plugin.deregisterNode(node_id)
    except:
        sys.stderr.write("Failed to deregister node: %s" % node_name)
        raise