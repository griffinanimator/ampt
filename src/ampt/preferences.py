# main session
import __main__

# third party libraries
import maya.cmds as cmds

# internal libraries
from core.settings import Settings

# maya preference settings as Singleton
# if you manage settings from here, you may consider this hard-coding the setting
__main__.settings = Settings()

# Load AMPT interface
cmds.evalDeferred("import ampt.interface")