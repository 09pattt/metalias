from importlib import metadata
from dataclasses import dataclass


@dataclass
class PackageData:
    name: str
    installed_version: str = None
    requires_version: str = None
    exists: bool = None
    version_matches: bool = None
    correct: bool = None


def get_require_packages(template: str):
    requirements = []

    with open(template) as file:
        for line in file:
            line = line.strip().replace(" ", "")
            if not line or line.startswith("#"):
                continue
            if "==" in line:
                package, version = line.split("==", 1)
                requirements.append({"package": package, "version": version})
            else:
                requirements.append({"package": line, "version": None})
    return requirements


def check_package(package: PackageData) -> PackageData:
    try:
        package.installed_version = metadata.version(package.name)
        package.exists = True
        if package.requires_version and package.installed_version != package.requires_version:
            print(repr(package.installed_version))
            print(package.installed_version)
            print(repr(package.requires_version))
            print(package.requires_version)
            package.version_matches = False
        else:
            package.version_matches = True
    except metadata.PackageNotFoundError:  # Package not found
        package.exists = False
    return package