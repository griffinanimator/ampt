class Component():
    def __init__(self, parent=None, child=None):
        self.state = {}
        self.parent = parent
        self.child = child