"""
Docstring for applications.appdata

โปรแกรมอ่านและเขียน data ของ metalias
"""

import json
from constants import *
from utils.file import *

class Metadata:
    def __init__(self, path: str = ".metalias/internal/metadata.json"):
        self.path = path
        self.data = self.load()

    def load(self):
        with open(str(join(appdir(), self.path)), "r", encoding="utf-8") as f:
            return json.load(f)
        
class AppData:
    def __init__(self, appdata_path: str = join(appdir(), ".metalias")):
        self.app_pathdata = PathData(constants.Path.APP_PATH)
        self.appdata_pathdata = PathData(constants.Path.APPDATA_PATH)

class RuntimeData:
    def __init__(self):
        self.terminal_width = shutil.get_terminal_size().columns