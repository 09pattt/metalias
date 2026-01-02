"""
Docstring for applications.metadata

โปรแกรมอ่านเขียนและส่งต่อข้อมูล metadata
"""

import json
from utils.file import *

def ImportData():
    with open(str(join(appdir(), ".metalias/internal/metadata.mtt2")), "r", encoding="utf-8") as f:
        return json.load(f)