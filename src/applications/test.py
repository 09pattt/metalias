from scripts import setup
from src.utils import file_utils

if __name__ == "__main__":
    """
    verbose = input(" verbose? 1/0 (0) >> ")
    if verbose == "1":
        verbose = True
    else:
        verbose = False

    requirement = input(" requirement source? (\"requirements.txt\") >> ")
    if requirement:
        requirement = file_utils.join(file_utils.appdir(), requirement)
    else:
        requirement = file_utils.join(file_utils.appdir(), "requirements.txt")
    
    print(f"{verbose} | {requirement}")

    setup.setup(verbose=verbose, requirement=requirement)
    """
    
    setup.setup(verbose=True)