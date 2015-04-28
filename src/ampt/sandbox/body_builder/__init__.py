properties = {"title": "Body Builder", "is_debug": True}

# internal libraries
from ampt.tools.widgets.tool_window import ToolWindow
from ampt.core.user_interface import load_interface


class BodyBuilder(ToolWindow):
    def __init__(self, parent=None):
        super(BodyBuilder, self).__init__(parent)

        print "Hello Body Builder!"


def load():
    try:
        load_interface(None, BodyBuilder)
    except Exception as e:
        print e.message
        pass