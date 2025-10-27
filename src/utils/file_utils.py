import pathlib
import os
import shutil
from pathlib import Path

def appdir():
    return Path(__file__).resolve().parent.parent.parent

def join(*args, resolve: bool = True):
    path = Path("")
    for i in range(len(args)):
        tail = Path(args[i])
        path = path / tail
    if resolve: path = path.resolve()
    return path

def mkfile(path: str, exist_ok: bool = False):
    file = Path(path).resolve()
    file.touch(exist_ok=exist_ok)

def rmfile(path: str):
    f = Path(path)
    if f.exists():
        f.unlink()

def mkdir(path: str, exist_ok: bool = False, parents: bool = True):
    file = Path(path).resolve()
    file.mkdir(exist_ok=exist_ok, parents=parents)

def rmdir(path: str):
    d = Path(path)
    if d.exists():
        shutil.rmtree(path)

def lsdir(path: str):
    d = Path(path)
    if d.exists():
        for item in d.iterdir():
            print(item)

def scan(path: str, filter: str = "*"):
    d = Path(path)
    if d.exists():
        for item in d.rglob(filter):
            print(item)

if __name__ == "__main__":
    metadata = {
        "destination": "data/development/"
    }
    while True: # Test command line
        cmd = input(" >>> ").replace(" ", "").lower()
        if cmd == "":
            pass
        elif cmd == "exit":
            break
        elif cmd == "clear":
            os.system("clear")
        elif cmd == "mkfile":
            file = input(" File : ")
            mkfile(join(appdir(), metadata["destination"], file))
        elif cmd == "rmfile":
            file = input(" File : ")
            rmfile(join(appdir(), metadata["destination"], file))
        elif cmd == "mkdir":
            dirname = input(" Directory : ")
            mkdir(join(appdir(), metadata["destination"], dirname))
        elif cmd == "rmdir":
            dirname = input(" Directory : ")
            rmdir(join(appdir(), metadata["destination"], dirname))
        elif cmd == "lsdir":
            dirname = input(" Directory : ")
            lsdir(join(appdir(), metadata["destination"], dirname))
        elif cmd == "scan":
            dirname = input(" Directory : ")
            scan(join(appdir(), metadata["destination"], dirname))
        elif cmd == "test":
            pass
        else:
            print("Unknown : " + cmd)