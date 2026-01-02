"""
Docstring for src.applications.command

จัดการดำเนินการใดๆ ตามคำสั่ง cli.py เป็นตัวกลางระหว่าง function ใดๆ
-แปลงค่าจาก CLI ให้นำไปใช้ต่อในส่วนต่างๆได้
"""

from applications.page import Prompter
from applications.metadata import ImportData
from utils.file import *

def version():
    page = Prompter()
    page.add_message(f"{ImportData()['program']} {ImportData()['version']}").generate()

def menu():
    print(" - MENU - ")


def info(option: str = "index"):
    if option == "index":
        page = Prompter()
        page.add_table(IndexPage=[
                f"Program : {ImportData()['program']}",
                f"Version : {ImportData()['version']}",
                f"Version number : {ImportData()['version_number']}",
                f"Path : {str(appdir())}"
            ]).generate()

def setting():
    print(" - SETTING - ")