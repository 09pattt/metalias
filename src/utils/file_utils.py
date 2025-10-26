import pathlib
import os
from pathlib import Path

def cwd(): # Current working directory
    return Path.cwd()

def touch(path: str, exist_ok: bool = False):
    file = Path(str(cwd()))
    file = file / path
    file.resolve()
    file.touch(exist_ok=exist_ok)

def mkdir(path: str, exist_ok: bool = False, parents: bool = False):
    file = Path(str(cwd()))
    file = file / path
    file.resolve()
    file.mkdir(exist_ok=exist_ok, parents=parents)

if __name__ == "__main__":
    while True: # Test command line
        cmd = input(" >>> ").replace(" ", "").lower()
        if cmd == "":
            pass
        elif cmd == "exit":
            break
        elif cmd == "clear":
            os.system("clear")
        elif cmd == "touch":
            file = input(" File : ")
            touch("data/development/" + file)
        elif cmd == "mkdir":
            dir = input(" Directory : ")
            mkdir("data/development/" + dir)
        else:
            print("Unknown : " + cmd)