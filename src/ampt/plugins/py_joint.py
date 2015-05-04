# standard libraries
import sys

# third party libraries
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

# node properties
py_joint_name = "PyJoint"
py_joint_id = OpenMaya.MTypeId(0x87635)


class PyJointNode(OpenMayaMPx.MPxTransform):
    def __init__(self):
        OpenMayaMPx.MPxTransform.__init__(self)

    def compute(self, plug, dataBlock):
        return OpenMaya.kUnknownParameter

    @staticmethod
    def creator():
        return OpenMayaMPx.asMPxPtr(PyJointNode())

    @staticmethod
    def initializer():
        n_attr = OpenMaya.MFnNumericAttribute()

        PyJointNode.color = n_attr.createColor("color", "c")
        n_attr.setDefault( 0.1, 0.1, 0.8 );
        n_attr.setKeyable(True);
        n_attr.setReadable(True);
        n_attr.setWritable(True);
        n_attr.setStorable(True);

        PyJointNode.addAttribute(PyJointNode.Color)


def initializePlugin(m_object):
    try:
        m_plugin = OpenMayaMPx.MFnPlugin(m_object, "3devartist", "0.0.1", "Any")

        m_plugin.registerNode(py_joint_name, py_joint_id,
                              PyJointNode.creator, PyJointNode.initializer,
                              OpenMayaMPx.MPxTransform.kDependNode)
    except:
        sys.stderr.write("Failed to register node: %s" % py_joint_name)
        raise


def uninitializePlugin(m_object):
    try:
        m_plugin = OpenMayaMPx.MFnPlugin(m_object)
        m_plugin.deregisterNode(py_joint_id)
    except:
        sys.stderr.write("Failed to deregister node: %s" % py_joint_name)
        raise    