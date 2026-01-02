"""
Docstring for src.utils.time

เอาออกด้วย tool นี้จะไม่ใช้ utils.time
"""

import time

class Time:
    def __init__(self):
        self.hour = None
        self.minute = None
        self.second = None
        self.milisecond = None
        self.day = None
        self.month = None
        self.year = None
        self.load()
    def load(self):
        self.weekday = None
        self.monthname = self.getmonthname()
    def dict(self):
        return {"hour":self.hour,
                "minute":self.minute,
                "second":self.second,
                "milisecond":self.milisecond,
                "day":self.day,
                "month":self.month,
                "year":self.year,
                "weekday":self.weekday,
                "monthname":self.monthname}
    def getmonthname(self):
        i = 1
        for name in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
            if i == self.month:
                return name
            else:
                i += 1
    def adjust(self, dict):
        self.hour = dict["hour"]
        self.minute = dict["minute"]
        self.second = dict["second"]
        self.milisecond = dict["milisecond"]
        self.day = dict["day"]
        self.month = dict["month"]
        self.year = dict["year"]

if __name__ == "__main__":
    a = Time()
    dict = a.dict()
    dict["month"] = 9
    a.adjust(dict)
    a.load()
    print(a.monthname)