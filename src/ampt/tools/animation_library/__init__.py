from ampt.core.user_interface import load_interface
from ampt.tools.widgets.content_library import ContentLibrary

import maya.OpenMaya as OpenMaya
import pymel.core as pm

from PySide import QtCore, QtGui


class AnimationLibrary(ContentLibrary):
    def __init__(self, parent=None):
        super(AnimationLibrary, self).__init__(parent=parent)

        self.title = "Animation Library"
        self.outliner.set_data(pm.ls(dag=True))
        self.build_description_widget()
        self.set_selection_callback()
        self.set_dag_callback()

    def build_description_widget(self):
        widget = self.description
        layout = widget.layout()

        item_icon_layout = QtGui.QHBoxLayout(widget)
        item_icon_widget = QtGui.QLabel("Nothing Selected...")
        item_icon_layout.addWidget(item_icon_widget)

        layout.addChildLayout(item_icon_layout)

    def set_selection_callback(self):

        def om_callback(_):

            def selected_item():
                tree_item = self.outliner.tree.currentItem()
                return tree_item.text(0) if tree_item else None

            def selected_obj():
                selected = pm.selected(type="transform") or None
                return selected[0].name() if selected else selected

            _item = selected_item()
            _obj = selected_obj()

            if _obj:
                result = tree_item = self.outliner.tree.findItems(_obj, QtCore.Qt.MatchExactly)[0]
                self.selection_changed.emit(selected_obj)
                self.outliner.set_current_item(result)
            elif _item:
                pm.select(_item, r=True)
            else:
                pm.select(clear=True)

        OpenMaya.MEventMessage.addEventCallback("SelectionChanged", om_callback)

        def qt_callback(*args, **kwargs):
            item = self.outliner.tree.currentItem().text(0)
            if item:
                pm.select(item, r=True)
                self.update_status("%s Selected" % item)
            else:
                pm.select(clear=True)
                self.update_status("Ready")

        self.outliner.tree.itemSelectionChanged.connect(qt_callback)

        init_selection = pm.ls(sl=True)
        pm.select(init_selection, r=True)

    def set_dag_callback(self):

        def om_callback(_):
            self.outliner.set_data(pm.ls(dag=True))
            self.outliner.update_data(pm.ls(dag=True))

        OpenMaya.MEventMessage.addEventCallback("DagObjectCreated", om_callback)


def load():
    try:
        load_interface(None, AnimationLibrary)
    except Exception as e:
        print e.message
        pass
