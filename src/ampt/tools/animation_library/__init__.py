from ampt.core.user_interface import load_interface
from ampt.tools.content_library import ContentLibrary

import maya.OpenMaya as OpenMaya
import pymel.core as pm

from PySide import QtCore


class AnimationLibrary(ContentLibrary):
    def __init__(self, parent=None):
        super(AnimationLibrary, self).__init__(parent=parent)

        self.title = "Animation Library"
        self.outliner.set_data(pm.ls(dag=True))
        self.set_selection_callback()

    def set_selection_callback(self):
        def callback(_):
            selected_obj = pm.selected(type="transform")
            selected_item = self.outliner.tree.findItems(selected_obj[0].name(), QtCore.Qt.MatchExactly)[0]
            self.selection_changed.emit(selected_obj)
            self.outliner.set_current_item(selected_item)

        OpenMaya.MEventMessage.addEventCallback("SelectionChanged", callback)


def load():
    try:
        load_interface(None, AnimationLibrary)
    except Exception as e:
        print e.message
        pass
