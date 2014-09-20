import shiboken
import pymel.core as pm
from PySide import QtCore, QtGui
from maya.OpenMayaUI import MQtUtil
import maya.OpenMaya as om


def wrap_instance(pointer, base_class=None):
    ptr = long(pointer)
    qObj = shiboken.wrapInstance(long(ptr), QtCore.QObject)
    metaObj = qObj.metaObject()
    cls = metaObj.className()
    superCls = metaObj.superClass().className()

    if hasattr(QtGui, cls):
        base = getattr(QtGui, cls)
    if hasattr(QtGui, superCls):
        base = getattr(QtGui, superCls)

    base = QtGui.QWidget if not base_class else base_class
    return shiboken.wrapInstance(long(ptr), base)


def get_q_object(element_name):
    """
    :param element_name: str(<maya_element_name>)
    :return: QObject
    """
    pointer = MQtUtil.findControl(element_name)
    if not pointer:
        pointer = MQtUtil.findLayout(element_name)
    if not pointer:
        pointer = MQtUtil.findMenuItem(element_name)
    return shiboken.wrapInstance(pointer, QtCore.QObject)


def get_maya_main_window():
    """
    :return: OpenMayaUI.MQtUtil.mainWindow() -> QMainWindow
    """
    pointer = MQtUtil.mainWindow()
    if pointer is None:
        raise RuntimeError('Maya main window not found.')

    window = wrap_instance(pointer, QtGui.QMainWindow)
    assert isinstance(window, QtGui.QMainWindow)

    return window

# Available Maya Callbacks
"""
ActiveViewChanged
ChannelBoxLabelSelected
ColorIndexChanged
CurveRGBColorChanged
DagObjectCreated
DisplayColorChanged
DisplayPreferenceChanged
DisplayRGBColorChanged
DragRelease
MenuModeChanged
ModelPanelSetFocus
NameChanged
NewSceneOpened
PostSceneRead
PostSceneSegmentChanged
PostToolChanged
PreFileNewOrOpened
RebuildUIValues
RecentCommandChanged
Redo
SceneImported
SceneOpened
SceneSaved
SceneSegmentChanged
SelectModeChanged
SelectPreferenceChanged
SelectPriorityChanged
SelectTypeChanged
SelectionChanged
SequencerActiveShotChanged
SetModified
ToolChanged
ToolDirtyChanged
Undo
angularToleranceChanged
angularUnitChanged
animLayerAnimationChanged
animLayerBaseLockChanged
animLayerGhostChanged
animLayerLockChanged
animLayerRebuild
animLayerRefresh
axisAtOriginChanged
cameraChange
cameraDisplayAttributesChange
constructionHistoryChanged
currentContainerChange
currentSoundNodeChanged
deleteAll
displayLayerAdded
displayLayerChange
displayLayerDeleted
displayLayerManagerChange
displayLayerVisibilityChanged
glFrameTrigger
gridDisplayChanged
idle
idleHigh
interactionStyleChanged
lightLinkingChanged
lightLinkingChangedNonSG
linearToleranceChanged
linearUnitChanged
modelEditorChanged
nurbsCurveRebuildPrefsChanged
nurbsToPolygonsPrefsChanged
nurbsToSubdivPrefsChanged
passContributionMapChange
playbackRangeChanged
playbackRangeSliderChanged
quitApplication
renderLayerChange
renderLayerManagerChange
renderPassChange
renderPassSetChange
renderPassSetMembershipChange
selectionPipelineChanged
snapModeChanged
softSelectOptionsChanged
start3dPaintTool
startColorPerVertexTool
stop3dPaintTool
stopColorPerVertexTool
symmetricModellingOptionsChanged
threadCountChanged
timeChanged
timeUnitChanged
workspaceChanged
"""