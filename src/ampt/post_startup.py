# main session
import __main__

# third party libraries
import maya.cmds as cmds

# internal libraries
from core.settings import Settings

# maya preference settings
# if you manage settings from here, you may consider this hard-coding the setting
__main__.settings = Settings()

# Load PyJoint Plugin
cmds.loadPlugin("py_joint.py")

# Start Red9 Studio Pack
cmds.evalDeferred("import Red9; Red9.start()")

# Start the AMPT Sandbox
# cmds.evalDeferred("import ampt.sandbox.interface as sandbox; sandbox.load()")
