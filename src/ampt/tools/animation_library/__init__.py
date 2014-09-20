from ampt.core.user_interface import get_maya_main_window
from ampt.tools.content_library import ContentLibrary

import maya.OpenMaya as OpenMaya
import pymel.core as pm


class AnimationLibrary(ContentLibrary):
    def __init__(self, parent=None):
        super(AnimationLibrary, self).__init__(parent=parent)


def load():
    try:
        maya_main_window = get_maya_main_window()

        for i in maya_main_window.children():
            cls = type(i).__name__
            if cls == "AnimationLibrary":
                i.setParent(None)
                i.destroy()

        animation_library = AnimationLibrary(maya_main_window)

        def on_selection_changed(_):
            animation_library.selection_changed.emit(pm.selected(type="transform"))
            animation_library.outliner.set_current_item(pm.selected(type="transform"))

        OpenMaya.MEventMessage.addEventCallback("SelectionChanged", on_selection_changed)

        animation_library.category_widget.set_data(pm.ls(dag=True))
        animation_library.display()

    except Exception as e:
        print e.message
        pass
