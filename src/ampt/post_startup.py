# third party libraries
import maya.cmds as cmds

# internal libraries
from core.settings import Settings

# maya preference settings
settings = Settings()
# settings["units"] = "meter"

# Load PyJoint Plugin
cmds.loadPlugin("py_joint.py")

# Start Red9 Studio Pack
cmds.evalDeferred("import Red9; Red9.start()")

# Start the AMPT Sandbox
# cmds.evalDeferred("import ampt.sandbox.interface as sandbox; sandbox.load()")
