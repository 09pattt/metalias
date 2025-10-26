#import _internal.utils
#import _internal.command
import sys
import questionary
import subprocess
from applications import setup
from utils import file_utils

if not setup.setup(): sys.exit("setup process error")

a = questionary.press_any_key_to_continue().ask()