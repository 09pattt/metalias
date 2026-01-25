"""
Docstring for src.applications.command

ดำเนินการแยกส่วนแล้วเรียกใช้ฟังก์ชันแยกทีตามสิ่งที่ cli.py โยนมาให้

REFACTOR REQUIRED:
เอาโค้ด function การทำงานย้ายไปไว้ใน page เพราะมันไม่เกี่ยวจ้า

"""

import sys
from features.page import Prompter
from features.appdata import Metadata
from applications.states import *
from utils.file import *
from systems.exception import *

def process(args):
        if args.version:
            process.version()
            sys.exit(0)

        if args.yes:
            pass

        if args.command == "menu":
            process.menu()

        elif args.command == "info":
            if args.info_option == "index":
                process.info()
            else:
                raise AppError()

        elif args.command == "setting":
            if args.setting_option == "index":
                process.setting()
            else:
                raise AppError()

        else:
            raise AppError()

def version():
    page = Prompter()
    metadata = Metadata()
    page.add_text(f"{metadata.data['program']} {metadata.data['version']}").generate()

def menu():
    page = Prompter()
    page.add_column(list=[
            f"metalias -h ",
            f"metalias -v ",
            f"metalias -a ",
            f"metalias -d "
        ], header="Command") \
        .add_column(list=[
            f"open program manual page",
            f"show installed program version",
            f"activate primary preset",
            f"deactivate current preset"
        ], header="Usage").close_table().generate()

def info(option: str = "index"):
    if option == "index":
        page = Prompter()
        metadata = Metadata()
        content = [
            {'head':'Program', 'value':metadata.data['program']},
            {'head':'Version', 'value':metadata.data['version']},
            {'head':'Version number', 'value':metadata.data['version_number']},
            {'head':'Path', 'value':str(appdir())}
        ]
        page.add_column(list=[item['head'] for item in content], header='Index') \
            .add_column(list=[item['value'] for item in content], header='Data').close_table().generate()

def setting():
    pass