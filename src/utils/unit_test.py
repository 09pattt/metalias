from src.utils import file_utils
import os

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
            file_utils.mkfile(file_utils.join(file_utils.appdir(), metadata["destination"], file))
        elif cmd == "rmfile":
            file = input(" File : ")
            file_utils.rmfile(file_utils.join(file_utils.appdir(), metadata["destination"], file))
        elif cmd == "mkdir":
            dirname = input(" Directory : ")
            file_utils.mkdir(file_utils.join(file_utils.appdir(), metadata["destination"], dirname))
        elif cmd == "rmdir":
            dirname = input(" Directory : ")
            file_utils.rmdir(file_utils.join(file_utils.appdir(), metadata["destination"], dirname))
        elif cmd == "lsdir":
            dirname = input(" Directory : ")
            file_utils.lsdir(file_utils.join(file_utils.appdir(), metadata["destination"], dirname))
        elif cmd == "scan":
            dirname = input(" Directory : ")
            file_utils.scan(file_utils.join(file_utils.appdir(), metadata["destination"], dirname))
        elif cmd == "test":
            file_utils.join()
        else:
            print("Unknown : " + cmd)