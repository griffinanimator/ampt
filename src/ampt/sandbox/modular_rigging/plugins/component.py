# # standard libraries
# import os
#
# # internal libraries
# from ampt.data.dict_utils import JSONDict
#
# # third party libraries
# import pymel.core as pm
#
# MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))
# COMPONENTS_PATH = os.path.join(MODULE_PATH, "components").replace("\\", "/")
#
#
# class Component(object):
#     def __init__(self, file_path, parent=None, child=None):
#         self.__dict__.update(JSONDict(file_path))
#         self.joints = list()
#
#     def layout_joints(self):
#         for name, position in self.layout["controls"].iteritems():
#             pm.select(clear=True)
#             self.joints.append(pm.nt.Joint(name=name, position=position))
#             pm.select(clear=True)
#
#     def info(self):
#         print self.summary
#         print self.layout['controls']

# standard libraries
import sys

# third party libraries
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

# node properties
node_name = "mr_component"
node_id = OpenMaya.MTypeId(0x87636)


class MRComponentNode(OpenMayaMPx.MPxLocatorNode):
    def __init__(self):
        OpenMayaMPx.MPxTransform.__init__(self)

    def compute(self, plug, dataBlock):
        return OpenMaya.kUnknownParameter

    @staticmethod
    def creator():
        return OpenMayaMPx.asMPxPtr(MRComponentNode())

    @staticmethod
    def initializer():
        n_attr = OpenMaya.MFnNumericAttribute()

        MRComponentNode.color = n_attr.createColor("color", "c")
        n_attr.setDefault( 0.1, 0.1, 0.8 );
        n_attr.setKeyable(True);
        n_attr.setReadable(True);
        n_attr.setWritable(True);
        n_attr.setStorable(True);

        MRComponentNode.addAttribute(MRComponentNode.color)


def initializePlugin(m_object):
    try:
        m_plugin = OpenMayaMPx.MFnPlugin(m_object, "3devartist", "0.0.1", "Any")

        m_plugin.registerNode(node_name, node_id,
                              MRComponentNode.creator, MRComponentNode.initializer,
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