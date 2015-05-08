# standard libraries
import os
import sys

# third party libraries
import maya.cmds as cmds

MODULE_PATH = os.path.abspath(os.path.dirname(__file__).replace("\\", "/"))
PLUGINS_PATH = os.path.join(MODULE_PATH, "plugins").replace("\\", "/")
SCRIPTS_PATH = os.path.join(MODULE_PATH, "tools/third_party").replace("\\", "/")


def configure_plugins():
    if PLUGINS_PATH not in os.environ["MAYA_PLUG_IN_PATH"]:
        split_path = os.environ["MAYA_PLUG_IN_PATH"].split(";")
        split_path.append(PLUGINS_PATH)
        os.environ["MAYA_PLUG_IN_PATH"] = str(";").join(split_path)


def configure_scripts():
    if os.path.exists(SCRIPTS_PATH):
        if SCRIPTS_PATH not in os.environ["MAYA_SCRIPT_PATH"]:
            split_path = os.environ["MAYA_SCRIPT_PATH"].split(";")
            split_path.append(SCRIPTS_PATH)
            os.environ["MAYA_SCRIPT_PATH"] = str(";").join(split_path)
        if SCRIPTS_PATH not in sys.path:
            sys.path.append(SCRIPTS_PATH)

# configure environment
configure_plugins()
configure_scripts()

# Start Red9 Studio Pack
cmds.evalDeferred("import Red9; Red9.start()")

# Start Epic A.R.T.
cmds.evalDeferred("import Epic;")

# Start the AMPT Sandbox
# cmds.evalDeferred("import ampt.sandbox.interface as sandbox; sandbox.load()")

# Load PyJoint Plugin
# cmds.loadPlugin("py_joint.py")
