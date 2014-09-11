import shiboken
from PySide import QtCore, QtGui
from maya.OpenMayaUI import MQtUtil


# def wrap_instance(pointer):
# """
#     :return: pointer -> QObject
#     """
#
#     def get_class(cls_name):
#         cls_attr = getattr(QtGui, cls_name, None)
#         return cls_attr if cls_attr else getattr(QtCore, cls_name, None)
#
#     ptr = long(pointer)
#     q_object = shiboken.wrapInstance(pointer, QtCore.QObject)
#     meta_object = q_object.metaObject()
#     cls = None
#
#     while cls is None:
#         cls = get_class(meta_object.className())
#         meta_object = meta_object.superClass()
#
#     return shiboken.wrapInstance(ptr, cls)


def wrap_instance(ptr, base=None):
    """
    Utility to convert a pointer to a Qt class instance (PySide/PyQt compatible)

    :param ptr: Pointer to QObject in memory
    :type ptr: long or Swig instance
    :param base: (Optional) Base class to wrap with (Defaults to QObject, which should handle anything)
    :type base: QtGui.QWidget
    :return: QWidget or subclass instance
    :rtype: QtGui.QWidget
    """
    if ptr is None:
        return None
    ptr = long(ptr)  #Ensure type
    if globals().has_key('shiboken'):
        if base is None:
            qObj = shiboken.wrapInstance(long(ptr), QtCore.QObject)
            metaObj = qObj.metaObject()
            cls = metaObj.className()
            superCls = metaObj.superClass().className()
            if hasattr(QtGui, cls):
                base = getattr(QtGui, cls)
            elif hasattr(QtGui, superCls):
                base = getattr(QtGui, superCls)
            else:
                base = QtGui.QWidget
        return shiboken.wrapInstance(long(ptr), base)
    # elif globals().has_key('sip'):
    #     base = QtCore.QObject
    #     return sip.wrapinstance(long(ptr), base)
    else:
        return None


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


class Singleton(object):
    def __init__(self):
        globals()[self.__class__.__name__] = self

    def __call__(self):
        return self


class ToolWidget(QtGui.QWidget, Singleton):
    def __init__(self, title="Untitled"):
        super(ToolWidget, self).__init__()
        self.setWindowTitle(title)
        self.setGeometry(0, 0, 1280, 720)
        self._center()

    def _center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        x = (screen.width() - self.width()) * 0.5
        y = (screen.width() - self.width()) * 0.25
        self.move(x, y)


class AnimationLibrary(ToolWidget):
    def __init__(self):
        super(AnimationLibrary, self).__init__()
        self.setWindowTitle("Camel - Animation Library")
        self.show()

test = AnimationLibrary()