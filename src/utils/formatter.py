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

class Sorting:
    def __init__(self, data:list):
        self.data = data
    def sort_data(self) -> list:
        return sorted(self.data, key=str.casefold)
    def sort_list(self, index:int) -> list:
        return sorted(self.data, key=lambda x: x[index].casefold())
    def sort_dict(self, dict_key:str) -> list:
        return sorted(self.data, key=lambda x: x[dict_key].casefold())