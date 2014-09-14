#import internal libraries
from ..tool_window import ToolWindow
from ..tool_widget import ToolWidget

#import third party libraries
from PySide import QtCore, QtGui


class AnimationLibrary(ToolWindow):
    def __init__(self):
        super(AnimationLibrary, self).__init__()

        def create_menu_bar():
            menu_bar = QtGui.QMenuBar()
            file_menu = QtGui.QMenu("&File", self)
            exit_action = file_menu.addAction("E&xit")
            menu_bar.addMenu(file_menu)
            return menu_bar

        def create_save_animation_widget():
            widget = ToolWidget(self)
            button = QtGui.QPushButton(self, "Save")
            layout = QtGui.QHBoxLayout()
            layout.setGeometry(20, 20, self.width(), self.height())
            layout.addStretch(1)
            layout.addWidget(button)
            widget.setLayout(layout)
            return widget

        self.menu_bar = create_menu_bar()

        self.save_animation_widget = create_save_animation_widget()

        self.main_layout = QtGui.QVBoxLayout()
        self.main_layout.addStretch(1)
        self.main_layout.addWidget(self.save_animation_widget)

        self.setMenuBar(self.menu_bar)
        self.setLayout(self.main_layout)

    def display(self):
        self.setWindowTitle("Camel - Animation Library")
        self.setGeometry(0, 0, 320, 480)
        self.move(self.screen_center)
        self.show()


animation_library = AnimationLibrary()
animation_library.display()