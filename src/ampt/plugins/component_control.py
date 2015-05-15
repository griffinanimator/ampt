# standard libraries
import math
import sys

# third party libraries
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaRender as OpenMayaRender

# properties
node_type_name = "AMPT_Component_Control"
node_type_id = OpenMaya.MTypeId(0x00000006)

# renderer objects
glRenderer = OpenMayaRender.MHardwareRenderer.theRenderer()
glFT = glRenderer.glFunctionTable()


class ComponentControl(OpenMayaMPx.MPxLocatorNode):
    def __init__(self):
        super(ComponentControl, self).__init__()

    # OVERRIDE
    def compute(self, plug, dataBlock):
        return OpenMaya.kUnknownParameter

    #OVERRIDE
    def draw(self, view, path, style, status):
        radius = 0.5

        view.beginGL()

        glFT.glEnable(OpenMayaRender.MGL_ALPHA)
        glFT.glEnable(OpenMayaRender.MGL_BLEND)

        glFT.glBegin(OpenMayaRender.MGL_TRIANGLE_FAN)
        glFT.glColor4f(0, 0, 1, 0.5)
        glFT.glVertex3f(0.0, 0.0, 0.0)
        for i in xrange(0, 360):
            x = math.cos(math.radians(i)) * radius
            y = math.sin(math.radians(i)) * radius
            z = 0.0
            glFT.glVertex3f(x, y, z)
        glFT.glEnd()

        glFT.glBegin(OpenMayaRender.MGL_TRIANGLE_FAN)
        glFT.glColor4f(1, 0, 0, 0.5)
        glFT.glVertex3f(0.0, 0.0, 0.0)
        for i in xrange(0, 360):
            x = 0.0
            y = math.sin(math.radians(i)) * radius
            z = math.cos(math.radians(i)) * radius
            glFT.glVertex3f(x, y, z)
        glFT.glEnd()

        glFT.glBegin(OpenMayaRender.MGL_TRIANGLE_FAN)
        glFT.glColor4f(0, 1, 0, 0.5)
        glFT.glVertex3f(0.0, 0.0, 0.0)
        for i in xrange(0, 360):
            x = math.cos(math.radians(i)) * radius
            y = 0.0
            z = math.sin(math.radians(i)) * radius
            glFT.glVertex3f(x, y, z)
        glFT.glEnd()

        for i in xrange(32):
            lat0 = math.pi * (-0.5 + float(i) / 32)
            z0 = math.sin(lat0)
            zr0 = math.cos(lat0)
            lat1 = math.pi * (-0.5 + float(i + 1) / 32)
            z1 = math.sin(lat1)
            zr1 = math.cos(lat1)
            glFT.glBegin(OpenMayaRender.MGL_QUAD_STRIP)
            glFT.glColor4f(1, 1, 1, 0.5)
            for j in xrange(32 + 1):
                lng = 2 * math.pi * float(j) / 32
                x = math.cos(lng)
                y = math.sin(lng)
                glFT.glVertex3f(x * zr0 * radius, y * zr0 * radius, z0 * radius)
                glFT.glVertex3f(x * zr1 * radius, y * zr1 * radius, z1 * radius)
            glFT.glEnd()

        glFT.glDisable(OpenMayaRender.MGL_ALPHA)
        glFT.glDisable(OpenMayaRender.MGL_BLEND)

        view.endGL()

        glFT.glBegin( OpenMayaRender.MGL_TRIANGLES );
        glFT.glColor3f( 1, 0, 0 )
        glFT.glVertex3f( 0, 1, 0 )
        glFT.glColor3f( 0, 1, 0 )
        glFT.glVertex3f( -1, -1, 1 )
        glFT.glColor3f( 0, 0, 1 )
        glFT.glVertex3f( 1, -1, 1);

        glFT.glColor3f( 1, 0, 0 )
        glFT.glVertex3f( 0, 1, 0);
        glFT.glColor3f( 0, 1, 0 )
        glFT.glVertex3f( -1, -1, 1);
        glFT.glColor3f( 0, 0, 1 )
        glFT.glVertex3f( 0, -1, -1);

        glFT.glColor3f( 1, 0, 0 )
        glFT.glVertex3f( 0, 1, 0)
        glFT.glColor3f( 0, 1, 0 )
        glFT.glVertex3f( 0, -1, -1)
        glFT.glColor3f( 0, 0, 1 )
        glFT.glVertex3f( 1, -1, 1)


        glFT.glColor3f( 1, 0, 0 )
        glFT.glVertex3f( -1, -1, 1)
        glFT.glColor3f( 0, 1, 0 )
        glFT.glVertex3f( 0, -1, -1)
        glFT.glColor3f( 0, 0, 1 )
        glFT.glVertex3f( 1, -1, 1)

        glFT.glEnd();

    def isBounded(self):
        return True

    def boundingBox(self):
        thisNode = self.thisMObject()
        plug = OpenMaya.MPlug(thisNode, self.size)

        sizeVal = plug.asMDistance()

        multiplier = sizeVal.asCentimeters()

        corner1 = OpenMaya.MPoint(-0.5, 0.0, 0.5)
        corner2 = OpenMaya.MPoint(0.5, 0.0, -0.5)

        corner1 = corner1 * multiplier
        corner2 = corner2 * multiplier

        bbox = OpenMaya.MBoundingBox(corner1, corner2)
        return bbox


def nodeCreator():
    return OpenMayaMPx.asMPxPtr(ComponentControl())


def nodeInitializer():
    unitFn = OpenMaya.MFnUnitAttribute()
    ComponentControl.size = unitFn.create("size", "in", OpenMaya.MFnUnitAttribute.kDistance)
    unitFn.setDefault(1.0)
    ComponentControl.addAttribute(ComponentControl.size)


def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.registerNode(node_type_name, node_type_id, nodeCreator, nodeInitializer,
                             OpenMayaMPx.MPxNode.kLocatorNode)
    except:
        sys.stderr.write("Failed to register node: %s" % node_type_name)
        raise


def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode(node_type_id)
    except:
        sys.stderr.write("Failed to deregister node: %s" % node_type_name)
        raise
