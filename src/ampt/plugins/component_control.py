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

aBase = OpenMaya.MObject()


class RigNode(OpenMayaMPx.MPxLocatorNode):
    size = OpenMaya.MObject()

    def __init__(self):
        OpenMayaMPx.MPxLocatorNode.__init__(self)

    def compute(self, plug, dataBlock):
        return OpenMaya.kUnknownParameter


    # Define how the rigNode will draw.
    def draw(self, view, path, style, status):
        thisNode = self.thisMObject()

        plug = OpenMaya.MPlug(thisNode, self.size)

        sizeVal = plug.asMDistance()

        multiplier = sizeVal.asCentimeters()


        view.beginGL()

        glFT.glEnable(OpenMayaRender.MGL_ALPHA)
        glFT.glEnable(OpenMayaRender.MGL_BLEND)

        radius = 1

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

        PI = math.pi
        segx = 16
        segy = 16
        slX = 1
        slY = 1
        slZ = 1
        trX = 0
        trY = 0
        trZ = 0
        for i in xrange(segx):
            lat0 = PI * (-0.5 + float(i) / segx)
            z0  = math.sin(lat0)
            zr0 = math.cos(lat0)
            lat1 = PI * (-0.5 + float(i+1) / segx)
            z1 = math.sin(lat1)
            zr1 = math.cos(lat1)
            glFT.glBegin(OpenMayaRender.MGL_QUAD_STRIP)
            glFT.glColor4f(1, 1, 1, 0.25)
            for j in xrange(segy+1):
                lng = 2 * PI * float(j) / segy
                x = math.cos(lng)
                y = math.sin(lng)
                glFT.glVertex3f(x*slX* zr0 * radius+trX, y*slY * zr0 * radius+trY, z0*slZ * radius+trZ)
                glFT.glVertex3f(x*slX* zr1 * radius+trX, y*slY * zr1 * radius+trY, z1*slZ * radius+trZ)
            glFT.glEnd()

        glFT.glDisable(OpenMayaRender.MGL_ALPHA)
        glFT.glDisable(OpenMayaRender.MGL_BLEND)

        view.endGL()

        # glFT.glColor3f(1, 0, 0)
        # glFT.glBegin(OpenMayaRender.MGL_TRIANGLES)
        # glFT.glVertex3f(-0.4, 0.0, 0.0)
        # glFT.glVertex3f(-0.2, 0.0, 0.2)
        # glFT.glVertex3f(-0.2, 0.0, -0.2)
        # glFT.glEnd()
        #
        # glFT.glColor3f(1, 0, 0)
        # glFT.glBegin(OpenMayaRender.MGL_TRIANGLES)
        # glFT.glVertex3f(0.4, 0.0, 0.0)
        # glFT.glVertex3f(0.2, 0.0, 0.2)
        # glFT.glVertex3f(0.2, 0.0, -0.2)
        # glFT.glEnd()
        #
        # glFT.glColor3f(1, 0, 0)
        # glFT.glBegin(OpenMayaRender.MGL_TRIANGLES)
        # glFT.glVertex3f(-0.4, 0.0, 0.0)
        # glFT.glVertex3f(-0.2, 0.2, 0.0)
        # glFT.glVertex3f(-0.2, -0.2, -0.0)
        # glFT.glEnd()
        #
        # glFT.glColor3f(1, 0, 0)
        # glFT.glBegin(OpenMayaRender.MGL_TRIANGLES)
        # glFT.glVertex3f(0.4, 0.0, 0.0)
        # glFT.glVertex3f(0.2, 0.2, 0.0)
        # glFT.glVertex3f(0.2, -0.2, -0.0)
        # glFT.glEnd()
        #
        # # cmds.createNode('RG_Part')
        #
        #
        # # Y Axis
        # glFT.glColor3f(0, 1, 0)
        # glFT.glBegin(OpenMayaRender.MGL_TRIANGLES)
        # glFT.glVertex3f(-0.2, 0.2, 0.0)
        # glFT.glVertex3f(0.0, 0.4, 0.0)
        # glFT.glVertex3f(0.2, 0.2, 0.0)
        # glFT.glEnd()
        #
        # glFT.glColor3f(0, 1, 0)
        # glFT.glBegin(OpenMayaRender.MGL_TRIANGLES)
        # glFT.glVertex3f(-0.2, -0.2, 0.0)
        # glFT.glVertex3f(0.0, -0.4, 0.0)
        # glFT.glVertex3f(0.2, -0.2, 0.0)
        # glFT.glEnd()
        #
        # glFT.glColor3f(0, 1, 0)
        # glFT.glBegin(OpenMayaRender.MGL_TRIANGLES)
        # glFT.glVertex3f(0.0, 0.2, -0.2)
        # glFT.glVertex3f(0.0, 0.4, 0.0)
        # glFT.glVertex3f(0.0, 0.2, 0.2)
        # glFT.glEnd()
        #
        # glFT.glColor3f(0, 1, 0)
        # glFT.glBegin(OpenMayaRender.MGL_TRIANGLES)
        # glFT.glVertex3f(0.0, -0.2, -0.2)
        # glFT.glVertex3f(0.0, -0.4, 0.0)
        # glFT.glVertex3f(0.0, -0.2, 0.2)
        # glFT.glEnd()
        #
        #
        #
        # # Z Axis
        # glFT.glColor3f(0, 0, 1)
        # glFT.glBegin(OpenMayaRender.MGL_TRIANGLES)
        # glFT.glVertex3f(-0.2, 0.0, 0.2)
        # glFT.glVertex3f(0.0, 0.0, 0.4)
        # glFT.glVertex3f(0.2, 0.0, 0.2)
        # glFT.glEnd()
        #
        # glFT.glColor3f(0, 0, 1)
        # glFT.glBegin(OpenMayaRender.MGL_TRIANGLES)
        # glFT.glVertex3f(-0.2, 0.0, -0.2)
        # glFT.glVertex3f(0.0, 0.0, -0.4)
        # glFT.glVertex3f(0.2, 0.0, -0.2)
        # glFT.glEnd()
        #
        # glFT.glColor3f(0, 0, 1)
        # glFT.glBegin(OpenMayaRender.MGL_TRIANGLES)
        # glFT.glVertex3f(0.0, -0.2, 0.2)
        # glFT.glVertex3f(0.0, 0.0, 0.4)
        # glFT.glVertex3f(0.0, 0.2, 0.2)
        # glFT.glEnd()
        #
        # glFT.glColor3f(0, 0, 1)
        # glFT.glBegin(OpenMayaRender.MGL_TRIANGLES)
        # glFT.glVertex3f(0.0, -0.2, -0.2)
        # glFT.glVertex3f(0.0, 0.0, -0.4)
        # glFT.glVertex3f(0.0, 0.2, -0.2)
        # glFT.glEnd()

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
    return OpenMayaMPx.asMPxPtr(RigNode())


def nodeInitializer():
    unitFn = OpenMaya.MFnUnitAttribute()
    RigNode.size = unitFn.create("size", "in", OpenMaya.MFnUnitAttribute.kDistance)
    unitFn.setDefault(1.0)
    RigNode.addAttribute(RigNode.size)


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
