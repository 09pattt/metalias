import logging

logging.basicConfig(
    level=logging.INFO,
    format=" * %(asctime)s (%(levelname)s) >>> %(message)s"
)

class Log:
    def __init__(self, message):
        self.message = message
    
    def info(self):
        logging.info(self.message)
    
    def warning(self):
        logging.warning(self.message)

    def error(self):
        logging.error(self.message)

def VarPair(variable: str, value: any, saparator: str = "=="):
    if value == True:
        expression = f"\33[32m{value}\33[0m"
    elif value == False:
        expression = f"\33[31m{value}\33[0m"
    elif value == None:
        expression = f"\33[31m{value}\33[0m"
    elif type(value) == str:
        expression = f'\33[32m"{value}"\33[0m'
    else:
        expression = f"\33[32m{value}\33[0m"
    print(f"\33[33m{variable} \33[35m: {type(value)} \33[0m {saparator} {expression}\33[0m")