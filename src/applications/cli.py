"""
Docstring for src.applications.cli

รอรับคำสั่งเป็นอย่างแรกก่อนจะออกคำสั่งที่ command.py ต่อ
"""

import argparse
from applications.router import process

def index():
    parser = argparse.ArgumentParser(
        prog="metalias",
        description="CLI tools to handle alias command, custom scripts."
    )

    parser.add_argument(
        "-l", "--log",
        action="store_true",
        help="Enable logging in process"
    )

    parser.add_argument(
        "-v", "--version",
        action="store_true",
        help="Show program version and exit"
    )

    parser.add_argument(
        "-y", "--yes",
        action="store_true",
        help="Force next decision to Confirm"
    )

    subparsers = parser.add_subparsers( # primary command {menu, info}
        dest="command",
        help="Primary command"
    )

    subparsers.add_parser( # add menu to primary command as subparsers
        "menu",
        help="Open menu index page"
    )

    info_parser = subparsers.add_parser( # add info to primary command as subparsers
        "info",
        help="Show up program informations"
    )

    info_parser.add_argument(
        "-a", "--all",
        action="store_true",
        help="Show all informations"
    )

    info_subparsers = info_parser.add_subparsers(
        dest="info_option",
        help="Choose option for show up informations"
    )

    info_subparsers.add_parser(
        "index",
        help="Show up informations index page"
    )

    info_subparsers.add_parser(
        "status",
        help="Show up stagement status page"
    )

    info_subparsers.add_parser(
        "credit",
        help="Show up credit page. Development, maintainer, owner"
    )

    info_parser.set_defaults(info_option="index")

    parser.set_defaults(command="menu")

    # Attach to router

    args = parser.parse_args()