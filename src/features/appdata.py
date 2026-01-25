"""
Docstring for applications.appdata

โปรแกรมอ่านและเขียน data ของ metalias
"""

import json
import shutil
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
        self.path = appdir() # Change name to app_path
        self.app_pathdata = PathData(self.path)
        self.appdata_path = appdata_path
        self.appdata_pathdata = PathData(self.appdata_path)

class RuntimeData:
    def __init__(self):
        self.terminal_width = shutil.get_terminal_size().columns