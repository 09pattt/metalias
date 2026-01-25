"""
Docstring for applications.states

Contain states class of program

IN CONSIDER:
Is this program a constants? and are constants can be change?

"""

from features.appdata import *

class AppState:
    loaded = None
    encrypted = None
    process_status = None
    terminal_width = RuntimeData().terminal_width

class ProcessState:
    yes = None
    confirmation = None
    exitcode = None

class Keys:
    cryption = None