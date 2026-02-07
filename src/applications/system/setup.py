from features.page import Prompter
from utils.file import *
from features.setup import *

prompter = Prompter()


class SetupConfig:
    def __init__(self,
                 requirements: str = join_app_path('requirements.txt'),
                 setup_template: str = join_app_path('setup_template.json'),
                 verbose: bool = False):
        self.requirements = requirements
        self.setup_template = setup_template
        self.verbose = verbose


config = SetupConfig()


def setup():
    if config.verbose:
        prompter \
            .add_separator(text="\33[33m * Config Data * \33[0m") \
            .add_blank() \
            .add_text(f"config.requirements : {config.requirements}") \
            .add_text(f"config.setup_template : {config.setup_template}") \
            .add_text(f"config.verbose : {config.verbose}") \
            .add_blank() \
            .add_separator(text="\33[33m * RUNNING TEST * \33[0m") \
            .add_blank() \
            .generate()

    requirements = get_require_packages(config.requirements)
    for requirement in requirements:
        package = check_package(PackageData(name=requirement["package"], requires_version=requirement["version"]))
        if config.verbose:
            if package.exists:
                prompter.add_text(f"\33[32m * PACKAGE INSTALLED: {package.name} * \33[0m")
            else:
                prompter.add_text(f"\33[31m * PACKAGE NOT FOUND: {package.name} * \33[0m")
            prompter.add_text(f"\33[0m   ↪ Installed version : {package.installed_version}\33[0m") \
                    .add_text(f"\33[0m   ↪ Requires version : {package.requires_version}\33[0m") \
                    .add_text(f"\33[0m   ↪ Package version is matches : {package.version_matches}\33[0m") \
                    .add_text(f"\33[0m   ↪ Package validation : {package.correct}\33[0m") \
                    .add_blank() \
                    .generate()


if __name__ == "__main__":
    setup()