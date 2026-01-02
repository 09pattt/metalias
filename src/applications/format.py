"""
โปรแกรมสำหรับการแปลง format ของ Metalias ให้ไปอยู่ใน format อื่น เพื่อให้จัดเก็บหรือนำมาใช้ได้
"""

def bytes(bytes: int):
    """transform bytes units to simplified form"""
    for unit in ["B", "KB", "MG", "GB", "TB"]:
        if bytes < 1000:
            return round(bytes, 2), unit
        bytes = bytes / 1000
    return round(bytes, 2), "PB"

class Transform:
    def __init__(self, raw):
        self.raw = raw

    def bytes(self):
        for unit in ["B", "KB", "MG", "GB", "TB"]:
            if bytes < 1000:
                return round(bytes, 2), unit
            bytes = bytes / 1000
        return round(bytes, 2), "PB"