import sys
import json
import importlib.metadata
import subprocess
from src.utils import file as futils

def setup(verbose: bool = False, requirement: str = None, json_path: str = None):

    """
    Assign config properties, handling class import/return data.
    """

    if json_path == None:
        json_path = futils.join(futils.appdir(), "template.json")
        if verbose: print(json_path)

    if requirement == None:
        requirement = futils.join(futils.appdir(), "requirements.txt")
        if verbose: print(requirement)

    config = {
        "json": json_path,
        "verbose": verbose,
        "requirement": requirement
    }

    with open(json_path, "r", encoding="utf-8") as f:
        template = json.load(f)
        env_files = template["env_files"]
        for i in range(len(env_files)):
            data = futils.PathData(futils.join(futils.appdir(), env_files[i]["path"]))
            
            if verbose:
                print(f"\33[30m\33[42m CHECKED FOR \"{data.path}\" \33[0m")
                print(f"exists: {data.exists}")
                print(f"type: {data.type}")
                print(f"is_file: {data.is_file}")
                print(f"is_dir: {data.is_dir}")

            if data.exists:
                if verbose: print(f"\33[32mfile at {data.path} exists \33[0m")
                if data.type == env_files[i]["type"]:
                    if verbose: print(f"\33[32mfile exists with correct type: PASSED\33[0m")
                else:
                    raise RuntimeError(f"{data.path} already exists with incorrect type")
            elif not data.exists:
                if verbose : print(f"\33[31mfile at {data.path} not found \33[0m")

                if env_files[i]["type"] == "file":
                    if verbose: print(f"RUNNING CREATE FILE AT {data.path}")
                    futils.mkfile(path=env_files[i]["path"])
                    res = futils.PathData(futils.join(futils.appdir(), env_files[i]["path"]))
                    if res.exists and res.is_file and verbose:
                        print(f"\33[32mCreated file : {env_files[i]["path"]}\33[0m")

                if env_files[i]["type"] == "dir":
                    if verbose: print(f"RUNNING CREATE DIRECTORY AT {data.path}")
                    futils.mkdir(path=env_files[i]["path"])
                    res = futils.PathData(futils.join(futils.appdir(), env_files[i]["path"]))
                    if res.exists and res.is_dir and verbose:
                        print(f"\33[32mCreated directory : {env_files[i]["path"]}\33[0m")
            else:
                raise RuntimeError("Unexpected value from data.exists")
            

    missing = check_requirements(verbose=config["verbose"], template=config["requirement"])
    
    if missing:
        for i in range(len(missing)):
            install_package(package=missing[i]["package_name"], version=missing[i]["req_version"])
        if check_requirements(verbose=True, template=config["requirement"]):
            return False

def check_requirements(verbose: bool, template: str):
    missing = []
    passed = 0
    interval = 0
    
    with open(template) as req:
        for line in req:
            package_name, req_version = line_split(line)
            if not package_name:
                continue
            interval = interval + 1
            result, cur_version = check_package(package_name=package_name, version=req_version, verbose=verbose)
            if not result:
                missing.append({"package_name": package_name, "req_version": req_version, "cur_version": cur_version})
            else:
                passed = passed + 1
    if verbose:
        print("")
        print("\33[43m\33[30m Results: \33[0m")
        print(f"\33[32m{passed}/{interval} package passed\33[0m")
        if missing:
            print(f"\33[31m{len(missing)} package missing or incorrect version\33[0m")
            print("\33[33mPackage incompatible, to corrective action:\33[0m")
            for i in range(0, len(missing)):
                if missing[i]["cur_version"]:
                    print(f'\33[33m - INCOMPATIBLE PACKAGE: \33[35m{missing[i]["package_name"]} \33[33mVERSION: \33[31m{missing[i]["cur_version"]} \33[0m>>> \33[32m{missing[i]["req_version"]}\33[0m')
                else:
                    print(f'\33[33m - MISSING PACKAGE: \33[35m{missing[i]["package_name"]} \33[33mVERSION: \33[35m{missing[i]["req_version"]}\33[0m')
    return missing

def line_split(line: str):
    line = line.strip().replace(" ", "") # erase all blank between line

    if not line or line.startswith("#"): # if line is blank or comment line return nothing
        return None, None

    if "==" in line:
        return line.split("==", 1)
    
    return line, None # if line has no specified version

def check_package(package_name: str, version = None, verbose = False):
    if verbose: print(f"RUNNING CHECK FOR: \33[35m{package_name}\33[0m")
    try:
        installed_version = importlib.metadata.version(package_name)
        if version and installed_version != version:
            if verbose: print("\33[31mNOT MATCH\33[0m")
            return False, installed_version
        if verbose: print("\33[32mPASSED\33[0m")
        return True, installed_version
    except importlib.metadata.PackageNotFoundError:
        if verbose: print("\33[31mNOT FOUND\33[0m")
        return False, None
    
def install_package(package, version=None):
    package = f"{package}=={version}" if version else package
    print(f"\33[33m * RUNNING INSTALL PACKAGE : {package}\33[0m")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", package]
    )
    if result.returncode != 0:
        print(f"\33[31m - FAILED TO INSTALL {package}\33[0m")
        print(f"ERROR : {result.stderr}")

if __name__ == "__main__":
    if "dev" in sys.argv:
        verbose = bool(input("VERBOSE (False) : "))
        requirement = input("REQUIREMENTS_PATH (requirements.txt) : ")
        if requirement == "":
            requirement = None
        json_path = input("JSON_PATH (template.json) : ")
        if json_path == "":
            json_path = None
        print(f"verbose = {verbose}")
        print(f"requirement = {requirement}")
        print(f"json_path = {json_path}")
        print(f"setup(verbose={verbose}, requirement={requirement}, json_path={json_path})")
        input("Is it ok to run setup with these arguments. (Ctrl+C to abort)")
        setup(verbose=verbose, requirement=requirement, json_path=json_path)
    elif len(sys.argv) > 1:
        print("UNKNOWN ARGUMENTS >>>{sys.argv}<<<")
    elif len(sys.argv) == 1:
        setup()