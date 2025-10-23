#import _internal.utils
#import _internal.command
import setup
import sys
import questionary
import subprocess

if not setup.setup(): sys.exit("setup process error")

a = questionary.press_any_key_to_continue().ask()