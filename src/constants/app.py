"""
Docstring for constants.app
"""

from utils.file import *


class Path:
    APP_PATH = appdir()
    APPDATA_RPATH = '.metalias'
    APPDATA_PATH = join_app_path(APPDATA_RPATH)