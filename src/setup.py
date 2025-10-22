import os
import sys
import importlib.metadata
import subprocess

# requires ** requirements.txt check, package installer, dir check

def check_package(package_name, version=None, verbose=False):
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

def line_split(line: str):
    line = line.strip().replace(" ", "") # erase all blank between line

    if not line or line.startswith("#"): # if line is blank or comment line return nothing
        return None, None

    if "==" in line:
        return line.split("==", 1)
    
    return line, None # if line has no specified version

def check_requirements(template = "./../requirements.txt", verbose=False):
    missing=[]
    passed = 0
    interval = 0
    with open(template) as f:
        for line in f:
            package_name, version_req = line_split(line)
            if not package_name: # if package_name = None continue
                continue
            interval = interval + 1
            result, version_now = check_package(package_name, version_req, verbose=verbose)
            if not result:
                missing.append({"name":package_name, "version_req":version_req, "version_now":version_now})
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
                if missing[i]["version_now"]:
                    print(f'\33[33m - INCOMPATIBLE PACKAGE: \33[35m{missing[i]["name"]} \33[33mVERSION: \33[31m{missing[i]["version_now"]} \33[0m>>> \33[32m{missing[i]["version_req"]}\33[0m')
                else:
                    print(f'\33[33m - MISSING PACKAGE: \33[35m{missing[i]["name"]} \33[33mVERSION: \33[35m{missing[i]["version_req"]}\33[0m')






here = os.path.dirname(os.path.abspath(__file__))

requirements_path = os.path.join(here, "..", "requirements.txt")

if "--verbose" in sys.argv or "-v" in sys.argv:
    check_requirements(requirements_path, verbose=True)

check_requirements(requirements_path, verbose=False)