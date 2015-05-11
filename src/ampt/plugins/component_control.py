# standard libraries
import math
import sys

# third party libraries
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaRender as OpenMayaRender
import maya.OpenMayaUI as OpenMayaUI

# properties
node_name = "component_contol_sphere"
node_id = OpenMaya.MTypeId(0x87635)

# gl objects
gl_renderer = OpenMayaRender.MHardwareRenderer.theRenderer()
gl_function_table = gl_renderer.glFunctionTable()


def gl_clear():
    gl_function_table.glClearDepth(0.0)
    gl_function_table.glDepthFunc(OpenMayaRender.MGL_ALWAYS)


class ComponentControlSphere(OpenMayaMPx.MPxLocatorNode):
    def __init__(self):
        OpenMayaMPx.MPxLocatorNode.__init__(self)

    def compute(self, plug, dataBlock):
        return OpenMaya.kUnknownParameter

    def draw(self, view, path, style, status):
        thisNode = self.thisMObject()
        fnThisNode = OpenMaya.MFnDependencyNode(thisNode)
        trX = OpenMaya.MPlug(thisNode, self.localPositionX).asFloat()
        trY = OpenMaya.MPlug(thisNode, self.localPositionY).asFloat()
        trZ = OpenMaya.MPlug(thisNode, self.localPositionZ).asFloat()
        slX = OpenMaya.MPlug(thisNode, self.localScaleX).asFloat()
        slY = OpenMaya.MPlug(thisNode, self.localScaleY).asFloat()
        slZ = OpenMaya.MPlug(thisNode, self.localScaleZ).asFloat()
        a = OpenMaya.MPlug(thisNode, fnThisNode.attribute("transparency")).asFloat()
        r = OpenMaya.MPlug(thisNode, fnThisNode.attribute("colorR")).asFloat()
        g = OpenMaya.MPlug(thisNode, fnThisNode.attribute("colorG")).asFloat()
        b = OpenMaya.MPlug(thisNode, fnThisNode.attribute("colorB")).asFloat()
        dt = OpenMaya.MPlug(thisNode, fnThisNode.attribute("drawType")).asInt()
        segx = OpenMaya.MPlug(thisNode, fnThisNode.attribute("segmentX")).asInt()
        segy = OpenMaya.MPlug(thisNode, fnThisNode.attribute("segmentY")).asInt()
        rad = OpenMaya.MPlug(thisNode, fnThisNode.attribute("radius")).asFloat()
        lw = OpenMaya.MPlug(thisNode, fnThisNode.attribute("lineWidth")).asInt()
        dro = OpenMaya.MPlug(thisNode, fnThisNode.attribute("drawOver")).asInt()

        a =1.0
        r = 1.0
        g = 1.0
        b = 1.0

        def draw_sphere(self):
            PI = math.pi
            for i in xrange(segx):
                lat0 = PI * (-0.5 + float(i) / segx)
                z0 = math.sin(lat0)
                zr0 = math.cos(lat0)
                lat1 = PI * (-0.5 + float(i + 1) / segx)
                z1 = math.sin(lat1)
                zr1 = math.cos(lat1)
                gl_function_table.glBegin(OpenMayaRender.MGL_QUAD_STRIP)
                for j in xrange(segy + 1):
                    lng = 2 * PI * float(j) / segy
                    x = math.cos(lng)
                    y = math.sin(lng)
                    gl_function_table.glVertex3f(x * slX * zr0 * rad + trX, y * slY * zr0 * rad + trY, z0 * slZ * rad + trZ)
                    gl_function_table.glVertex3f(x * slX * zr1 * rad + trX, y * slY * zr1 * rad + trY, z1 * slZ * rad + trZ)
                gl_function_table.glEnd()

        def draw_shaded(self):
            gl_function_table.glPolygonMode(OpenMayaRender.MGL_FRONT_AND_BACK, OpenMayaRender.MGL_FLAT)

        def draw_wireframe(self):
            gl_function_table.glPolygonMode(OpenMayaRender.MGL_FRONT_AND_BACK, OpenMayaRender.MGL_LINE)
            gl_function_table.glLineWidth(lw)

        gl_function_table.glPushAttrib(OpenMayaRender.MGL_ALL_ATTRIB_BITS)
        view.beginGL()
        if dro == 1:
            gl_clear()

        f = draw_shaded
        if style not in [OpenMayaUI.M3dView.kFlatShaded, OpenMayaUI.M3dView.kGouraudShaded]:
            f = draw_wireframe
        if dt == 1:
            f = draw_shaded
        elif dt == 0:
            f = draw_wireframe
        gl_function_table.glEnable(OpenMayaRender.MGL_BLEND)
        gl_function_table.glBlendFunc(OpenMayaRender.MGL_SRC_ALPHA, OpenMayaRender.MGL_ONE_MINUS_SRC_ALPHA)
        f(self)
        draw_sphere(self)
        f(self)
        view.endGL()
        gl_function_table.glPopAttrib()


def creator():
    return OpenMayaMPx.asMPxPtr(ComponentControlSphere())


def initializer():
    nAttr = OpenMaya.MFnNumericAttribute()

    ComponentControlSphere.aSegX = nAttr.create("segmentX", "segX", OpenMaya.MFnNumericData.kInt)
    nAttr.setDefault(16)
    nAttr.setMin(2)
    nAttr.setKeyable(1)
    nAttr.setReadable(1)
    nAttr.setWritable(1)
    nAttr.setStorable(1)

    ComponentControlSphere.aSegY = nAttr.create("segmentY", "segY", OpenMaya.MFnNumericData.kInt)
    nAttr.setDefault(16)
    nAttr.setMin(2)
    nAttr.setKeyable(1)
    nAttr.setReadable(1)
    nAttr.setWritable(1)
    nAttr.setStorable(1)

    ComponentControlSphere.aRad = nAttr.create("radius", "rad", OpenMaya.MFnNumericData.kFloat)
    nAttr.setDefault(1.0)
    nAttr.setKeyable(1)
    nAttr.setReadable(1)
    nAttr.setWritable(1)
    nAttr.setStorable(1)

    ComponentControlSphere.addAttribute(ComponentControlSphere.aSegX)
    ComponentControlSphere.addAttribute(ComponentControlSphere.aSegY)
    ComponentControlSphere.addAttribute(ComponentControlSphere.aRad)


def initializePlugin(mobject):
    try:
        mplugin = OpenMayaMPx.MFnPlugin(mobject, "Michael Trainor", "0.0.1", "Any")
        mplugin.registerNode(node_name, node_id, creator, initializer,
                             OpenMayaMPx.MPxNode.kLocatorNode)
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