import os
import sys
import importlib.metadata
import subprocess
from src.utils import file_utils

def setup(verbose: bool = False, requirement: str = None):

    """
    Assign config properties, handling class import/return data.
    """

    if requirement == None:
        requirement = file_utils.join(file_utils.appdir(), "requirements.txt")

    config = {
        "verbose": verbose,
        "requirement": requirement
    }

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
                    print(f'\33[33m - INCOMPATIBLE PACKAGE: \33[35m{missing[i]["name"]} \33[33mVERSION: \33[31m{missing[i]["version_now"]} \33[0m>>> \33[32m{missing[i]["version_req"]}\33[0m')
                else:
                    print(f'\33[33m - MISSING PACKAGE: \33[35m{missing[i]["name"]} \33[33mVERSION: \33[35m{missing[i]["version_req"]}\33[0m')
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