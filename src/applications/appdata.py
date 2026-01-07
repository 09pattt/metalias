"""
Docstring for applications.appdata

โปรแกรมอ่านและเขียน data ของ metalias
"""

import json
from utils.file import *

class Metadata:
    def __init__(self, path: str = ".metalias/internal/metadata.json"):
        self.path = path
        self.data = self.load()

    def load(self):
        with open(str(join(appdir(), self.path)), "r", encoding="utf-8") as f:
            return json.load(f)
        
class Data:
    def __init__(self, appdata_path: str = join(appdir(), ".metalias")):
        self.path = appdir()
        self.app_pathdata = PathData(self.path)
        self.appdata_path = appdata_path
        self.appdata_pathdata = PathData(self.appdata_path)