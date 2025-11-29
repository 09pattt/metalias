import shutil
from pathlib import Path

def appdir():
    return Path(__file__).resolve().parent.parent.parent

def datadir():
    return join(appdir(), ".metalias")

def join(*args: str, resolve: bool = True):
    path = Path("")
    for i in range(len(args)):
        tail = Path(args[i])
        path = path / tail
    if resolve: path = path.resolve()
    return path
    
class file_metadata:
    def __init__(self, path: str):
        self.path = path
        self.exists = None
        self.type = None
        self.is_file = None
        self.is_dir = None
        f = Path(path)
        if f.exists():
            self.exists = True
            if f.is_file():
                self.type = "file"
                self.is_file = True
            elif f.is_dir():
                self.type = "dir"
                self.is_dir = True
            else:
                pass
        else:
            self.exists = False

def mkfile(path: str, exist_ok: bool = False):
    file = Path(path).resolve()
    file.touch(exist_ok=exist_ok)

def rmfile(path: str):
    f = Path(path)
    if f.exists():
        f.unlink()

def mkdir(path: str, exist_ok: bool = False, parents: bool = True):
    file = Path(path).resolve()
    try:
        file.mkdir(exist_ok=exist_ok, parents=parents)
    except FileExistsError:
        print(f"\33[37m\33[41m * FileExistError * \33[0m \33[33m : Directory at path \33[35m>>>{file}<<<\33[33m already existed.\33[0m")

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