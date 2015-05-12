# standard libraries
import sys

# third party libraries
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaRender as OpenMayaRender

# properties
node_name = "component_contol_sphere"
node_id = OpenMaya.MTypeId(0x87635)

# gl objects
gl_renderer = OpenMayaRender.MHardwareRenderer.theRenderer()
gl_function_table = gl_renderer.glFunctionTable()


def gl_clear():
    gl_function_table.glClearDepth(0.0)
    gl_function_table.glDepthFunc(OpenMayaRender.MGL_ALWAYS)


# plugin class
class ComponentControlSphere(OpenMayaMPx.MPxNode):
    in_transform_root = OpenMaya.MObject()
    out_transform_root = OpenMaya.MObject()

    def __init__(self):
        super(ComponentControlSphere, self).__init__()

    # OVERRIDE
    def compute(self, plug, data_block):
        pass


def creator():
    return OpenMayaMPx.asMPxPtr(ComponentControlSphere())


def initializer():
    pass

def initializePlugin(mobject):
    try:
        mplugin = OpenMayaMPx.MFnPlugin(mobject, "Michael Trainor", "0.0.1", "Any")
        mplugin.registerNode(node_name, node_id, creator, initializer,
                             OpenMayaMPx.MPxNode.kDependNode)
    except:
        sys.stderr.write("Failed to register node: %s" % node_name)
        raise


def uninitializePlugin(mobject):
    try:
        mplugin = OpenMayaMPx.MFnPlugin(mobject)
        mplugin.deregisterNode(node_id)
    except:
        sys.stderr.write("Failed to deregister node: %s" % node_name)
        raise    