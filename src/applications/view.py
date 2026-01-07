"""
Docstring for applications.page
"""

import questionary
import logging

class Prompter:
    def __init__(self):
        self.lines = []
    
    def add_message(self, text: any):
        self.lines.append({"type":"message", "content":str(text)})
        return self
    
    def add_table(self, **kwargs):
        table_list = []
        for k, v in kwargs.items():
            table_list.append({"header":k, "items":v})
        self.lines.append({"type":"table", "content":table_list})
        return self

    def generate(self):
        for line in self.lines:
            if line["type"] == "message":
                print(line["content"])

            elif line["type"] == "table":
                for table in line["content"]:
                    print(table["header"])
                    print("----------------")
                    for item in table["items"]:
                        print(item)

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