# third party libraries
import shiboken
from PySide import QtCore, QtGui
from maya.OpenMayaUI import MQtUtil
import pymel.core as pm


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


def get_q_object_as(cls, element_name):
    """
    :param element_name: str(<maya_element_name>)
    :return: QObject
    """
    pointer = MQtUtil.findControl(element_name)
    if not pointer:
        pointer = MQtUtil.findLayout(element_name)
    if not pointer:
        pointer = MQtUtil.findMenuItem(element_name)
    return shiboken.wrapInstance(pointer, cls)


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


def get_maya_main_window_name():
    return pm.MelGlobals()['gMainWindow']


def reload_interface(parent, cls):
    parent = get_maya_main_window() if not parent else parent

    for child in parent.children():
        child_type = type(child).__name__
        class_type = cls.__name__
        if child_type == class_type:
            child.setParent(None)
            child.destroy()
            cls(parent)


def load_interface(parent, cls):
    parent = get_maya_main_window() if not parent else parent

    for child in parent.children():
        child_type = type(child).__name__
        class_type = cls.__name__
        if child_type == class_type:
            child.setParent(None)
            child.destroy()

    app = cls(parent)
    app.display()


def load_dock_interface(parent, cls):
    parent = get_maya_main_window() if not parent else parent

    for child in parent.children():
        child_type = type(child).__name__
        class_type = cls.__name__
        if child_type == class_type:
            child.setParent(None)
            child.destroy()

    def get_tabbed_dock_widgets():
        docked_controls = [ctl for ctl in parent.children() if isinstance(ctl, QtGui.QDockWidget)]
        tabbed_controls = list()

        # this seems like a very hacky way to find these controls.
        # this process dumps fairly arbitrary lists into a new list
        # using tabifiedDockWidgets()
        for control in docked_controls:
            for shared_control in parent.tabifiedDockWidgets(control):
                if shared_control not in tabbed_controls:
                    tabbed_controls.append(shared_control)
        return tabbed_controls

    obj = cls()  # must pass an instantiated object to addDockWidget
    obj.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
    parent.addDockWidget(QtCore.Qt.RightDockWidgetArea, obj)

    tabbed_dock_controls = get_tabbed_dock_widgets() or None
    if tabbed_dock_controls:
        if obj not in tabbed_dock_controls:
            tabbed_dock_controls.append(obj)

        for i in range(0, len(tabbed_dock_controls) - 1):
            parent.tabifyDockWidget(tabbed_dock_controls[i], tabbed_dock_controls[i+1])


def add_menu(name=None):
    if not name:
        return name

    if pm.menu(name, ex=True):
        pm.deleteUI(name, m=True)
    menu = pm.menu(name, parent=get_maya_main_window_name())

    return get_q_object_as(QtGui.QMenu, menu)


def get_toolbars(q_obj):
    return [child for child in q_obj.children() if isinstance(child, QtGui.QToolBar)] if q_obj.children() else None

    
def get_toolbar(toolbar_name):
    """
    Default Maya Toolbar names: "Status Line", "Shelf", "Help Line", "Command Line", "Range Slider", "Time Slider", "Tool Box"
    """
    toolbars = get_toolbars(get_maya_main_window())
    return [toolbar for toolbar in toolbars if toolbar.windowTitle() == toolbar_name][0]

    
def get_shelf():
    return [child for child in get_toolbar("Shelf").children() if isinstance(child, QtGui.QWidget) and child.objectName() == "MainShelfLayout"][0]
