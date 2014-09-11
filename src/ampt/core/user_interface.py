import shiboken
from PySide import QtCore, QtGui
from maya.OpenMayaUI import MQtUtil


def wrap_instance(pointer):
    """
    :return: pointer -> QObject
    """

    def get_class(cls_name):
        cls_attr = getattr(QtGui, cls_name, None)
        return cls_attr if cls_attr else getattr(QtCore, cls_name, None)

    ptr = long(pointer)
    q_object = shiboken.wrapInstance(pointer, QtCore.QObject)
    meta_object = q_object.metaObject()
    cls = None

    while cls is None:
        cls = get_class(meta_object.className())
        meta_object = meta_object.superClass()

    return shiboken.wrapInstance(ptr, cls)


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

    window = wrap_instance(pointer)
    assert isinstance(window, QtGui.QMainWindow)

    return window