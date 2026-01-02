from src.utils.file import *
from src.utils import format

if __name__ == "__main__":
    destination = input("\33[33m Path : \33[0mmetalias/")
    f = PathData(join(appdir(), destination)).get_size()
    print(f"RAW : {f} bytes")
    quantity, unit = format.Transform(f).bytes()
    print(f"TRANSFORMED : {quantity} {unit}")