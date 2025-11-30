"""
Docstring for src.core.system

Return system info and do system operation.
"""

import os
import sys
import time
from src.utils import file_utils
from src.applications import format

class PathData:
    def __init__(self, path: str):
        self.path = path
        self.size = self.get_size()
        self.is_file = os.path.isfile
        self.is_dir = os.path.isdir

    def get_size(self):
        size = 0
        interval = 0
        for root, dirs, files in os.walk(self.path):
            for file in files:
                try:
                    file_path = os.path.join(root, file)
                    size += os.path.getsize(file_path)
                    bytes, unit = format.bytes(size)
                    interval += 1
                    print("")
                    print(f"\33[32m {interval}. {file} | {os.path.getsize(file_path)} bytes \33[0m")
                    print(f"   -   loaded {bytes} {unit}")
                except FileNotFoundError:
                    pass
        self.size = size
        return size

if __name__ == "__main__":
    path = input("extra path from [/metalias] : ")
    print("start testing")
    res = PathData(file_utils.join(file_utils.appdir(), path))
    print(f"\33[45m\33[37m * FINAL : {res.size} bytes * \33[0m")