"""
Docstring for src.applications.command

จัดการดำเนินการใดๆ ตามคำสั่ง cli.py เป็นตัวกลางระหว่าง function ใดๆ
-แปลงค่าจาก CLI ให้นำไปใช้ต่อในส่วนต่างๆได้
"""

from features.page import Prompter
from features.appdata import Metadata
from utils.file import *

def version():
    page = Prompter()
    metadata = Metadata()
    page.add_message(f"{metadata.data['program']} {metadata.data['version']}").generate()

def menu():
    page = Prompter()
    page.add_table(metalias=[
        f"metalias -h     open program manual page",
        f"metalias -v     show installed program version",
        f"metalias -a     activate primary preset",
        f"metalias -d     deactivate preset"
    ]).generate()

def info(option: str = "index"):
    if option == "index":
        page = Prompter()
        metadata = Metadata()
        page.add_table(IndexPage=[
                f"Program : {metadata.data['program']}",
                f"Version : {metadata.data['version']}",
                f"Version number : {metadata.data['version_number']}",
                f"Path : {str(appdir())}"
            ]).generate()

def setting():
    print(" - SETTING - ")