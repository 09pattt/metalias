#import _internal.utils
#import _internal.command
import _internal.core.setup as setup
import sys
import questionary
import subprocess
from _internal.utils import path

if not setup.setup(): sys.exit("setup process error")

a = questionary.press_any_key_to_continue().ask()

print(path.pwd())