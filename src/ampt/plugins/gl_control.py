# standard libraries
import sys

# third party libraries
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

# node properties
node_name = "gl_control"
node_id = OpenMaya.MTypeId(0x87635)


class GLControl(OpenMayaMPx.MPxLocatorNode):
    def __init__(self):
        OpenMayaMPx.MPxTransform.__init__(self)

    def compute(self, plug, dataBlock):
        return OpenMaya.kUnknownParameter

    @staticmethod
    def creator():
        return OpenMayaMPx.asMPxPtr(GLControl())

    @staticmethod
    def initializer():
        n_attr = OpenMaya.MFnNumericAttribute()

        GLControl.color = n_attr.createColor("color", "c")
        n_attr.setDefault( 0.1, 0.1, 0.8 );
        n_attr.setKeyable(True);
        n_attr.setReadable(True);
        n_attr.setWritable(True);
        n_attr.setStorable(True);

        GLControl.addAttribute(GLControl.color)


def initializePlugin(m_object):
    try:
        m_plugin = OpenMayaMPx.MFnPlugin(m_object, "3devartist", "0.0.1", "Any")

        m_plugin.registerNode(node_name, node_id,
                              GLControl.creator, GLControl.initializer,
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