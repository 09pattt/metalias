import os

def pwd():
    return os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    result = pwd()
    print(result)