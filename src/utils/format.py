"""
Docstring for src.utils.formatter
"""

class Transform:
    def __init__(self, raw):
        self.raw = raw

    def bytes(self):
        bytes = int(self.raw)
        for unit in ["B", "KB", "MB", "GB", "TB"]:
            if bytes < 1000:
                return round(bytes, 2), unit
            bytes = bytes / 1000
        return round(bytes, 2), "PB"