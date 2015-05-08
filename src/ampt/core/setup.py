# standard libraries
import os
import sys


def add_plugin_path(path):
    if path not in os.environ["MAYA_PLUG_IN_PATH"]:
        split_path = os.environ["MAYA_PLUG_IN_PATH"].split(";")
        split_path.append(path)
        os.environ["MAYA_PLUG_IN_PATH"] = str(";").join(split_path)


def add_script_path(path):
    if os.path.exists(path):
        if path not in os.environ["MAYA_SCRIPT_PATH"]:
            split_path = os.environ["MAYA_SCRIPT_PATH"].split(";")
            split_path.append(path)
            os.environ["MAYA_SCRIPT_PATH"] = str(";").join(split_path)
        if path not in sys.path:
            sys.path.append(path)
