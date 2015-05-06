# internal libraries
from ampt.core.user_interface import load_dock_interface

# application libraries
from interface import Interface


def load():
    try:
        load_dock_interface(None, Interface)
    except Exception as e:
        print e.message
        pass