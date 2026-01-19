"""
Docstring for src.applications.cli

รอรับคำสั่งเป็นอย่างแรกก่อนจะออกคำสั่งที่ command.py ต่อ
"""

import argparse
import sys
from features import log
from applications import process

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


    # Execution

    args = parser.parse_args()

    if args.version:
        process.version()
        sys.exit(0)

    if args.yes:
        pass

    if args.log:
        print("\33[43m\33[30m * PROCESS DATA * \33[0m")
        log.VarPair("args.command", args.command)
        log.VarPair("args.info_option", args.info_option)

    if args.command == "menu":
        process.menu()

    elif args.command == "info":
        if args.info_option == "index":
            process.info()
        else:
            log.Log("Have no any condition support for this parser").error()

    elif args.command == "setting":
        if args.setting_option == "index":
            process.setting()
        else:
            log.Log("Have no any condition support for this parser").error()
    
    else:
        log.Log("Have no any condition support for this parser").error()