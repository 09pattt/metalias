import os
import sys
import importlib.metadata
import subprocess

# requires ** requirements.txt check, package installer, dir check

def check_package(package_name, version=None):
    if config["verbose"]: print(f"RUNNING CHECK FOR: \33[35m{package_name}\33[0m")
    try:
        installed_version = importlib.metadata.version(package_name)
        if version and installed_version != version:
            if config["verbose"]: print("\33[31mNOT MATCH\33[0m")
            return False, installed_version
        if config["verbose"]: print("\33[32mPASSED\33[0m")
        return True, installed_version
    except importlib.metadata.PackageNotFoundError:
        if config["verbose"]: print("\33[31mNOT FOUND\33[0m")
        return False, None

def line_split(line: str):
    line = line.strip().replace(" ", "") # erase all blank between line

    if not line or line.startswith("#"): # if line is blank or comment line return nothing
        return None, None

    if "==" in line:
        return line.split("==", 1)
    
    return line, None # if line has no specified version

def check_requirements(template = "./../../requirements.txt"):
    missing=[]
    passed = 0
    interval = 0
    with open(template) as f:
        for line in f:
            package_name, version_req = line_split(line)
            if not package_name: # if package_name = None continue
                continue
            interval = interval + 1
            result, version_now = check_package(package_name, version_req)
            if not result:
                missing.append({"name":package_name, "version_req":version_req, "version_now":version_now})
            else:
                passed = passed + 1
    if config["verbose"]:
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
    return missing

def install_package(package, version=None):
    package = f"{package}=={version}" if version else package
    print(f"\33[33m * RUNNING INSTALL PACKAGE : {package}\33[0m")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", package]
    )
    if result.returncode != 0:
        print(f"\33[31m - FAILED TO INSTALL {package}\33[0m")
        print(f"ERROR : {result.stderr}")


def setup():
    config["abspath"] = os.path.dirname(os.path.abspath(__file__))
    config["requirement"] = os.path.join(config["abspath"], "..", "..", "requirements.txt")
    missing = check_requirements(config["requirement"])
    if missing:
        for i in range(len(missing)):
            install_package(missing[i]["name"], missing[i]["version_req"])
        result = check_requirements(config["requirement"])
        if result:
            print(f"\33[41m\33[37m [ ! ] FAILED missing : {missing}\33[0m")
            return False
        else:
            print(f"\33[42m\33[30m SUCCESSFULLY \33[0m")
            return True
    return True



config = {
    "verbose": False,
    "abspath": None,
    "requirement": None
}

if __name__ == "__main__":
    config["abspath"] = os.path.dirname(os.path.abspath(__file__))
    config["requirement"] = os.path.join(config["abspath"], "..", "..", "requirements.txt")

    if "help" in sys.argv or "-h" in sys.argv: # install missing package or correct the version and fix .metalias directory
        print("help, -h : open setup manual")
        print("verbose, -v : print verbose of processing")
        print("check, -c : check if existed packages match requirement without install")
        sys.exit(0)

    if "verbose" in sys.argv or "-v" in sys.argv: # verbose the process
        config["verbose"] = True

    if "check" in sys.argv or "-c" in sys.argv: # check package but will not install
        config["verbose"] = True
        if check_requirements(config["requirement"]):
            sys.exit(1)
        else:
            sys.exit(0)

    setup()