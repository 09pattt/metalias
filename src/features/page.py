"""
Docstring for applications.page
"""

import questionary
import logging
from features.appdata import RuntimeData

class Prompter:
    def __init__(self):
        self.lines = []
        self.table = []
        self.columns = []

    def reset(self):
        self.lines = []
        self.table = []
        self.columns = []
        return self
    
    # Text box
    
    def clear(self):
        self.lines = []
        return self
    
    def add_text(self, *texts):
        for text in texts:
            self.lines.append({"type":"message", "content":str(text)})
        return self
    
    def add_blank(self, cycle:int = 1):
        i = 0
        while i < cycle:
            self.lines.append({"type":"blank"})
            i += 1
        return self

    def add_separator(self, text:str = "", fill:str = "-"):
        self.lines.append({"type":"separator", "content":text, "fill":fill})
        return self
    
    # Table

    def close_table(self):
        if self.table:
            self.lines.append({"type":"table", "content":self.table})
        self.table = []
        return self
    
    def clear_table(self):
        self.table = []
    
    def add_column(self, list:list, width:int = 0, header:str = ""):
        if not width:
            width = 0
            for item in list:
                string_length = len(str(item))
                if string_length > width:
                    width = string_length
        length = len(list)
        self.table.append({"header":header, "list":list, "width":width, "length":length})
        return self

    def generate(self, reset: bool = True):
        for line in self.lines:
            if line["type"] == "message":
                print(line["content"])
            
            elif line["type"] == "blank":
                print("")

            elif line["type"] == "separator":
                if line["content"]:
                    print(str(line["content"]).center(RuntimeData().terminal_width, line["fill"]))
                else:
                    print(line["fill"] * RuntimeData().terminal_width)

            elif line["type"] == "table":
                width = RuntimeData().terminal_width
                rows = []
                total_width = 0
                for column in line["content"]:
                    total_width += column["width"] + 1
                    if total_width < width:
                        rows.append(column)
                    else:
                        for column2 in rows:
                            print(f"{column2["header"]:<{column2["width"]}}", end=" ")
                        print()
                        
                        for column2 in rows:
                            print("-" * column2["width"], end=" ")
                        print("")
                        
                        columns_length = []
                        for column2 in rows:
                            columns_length.append(column2["length"])
                        for index in range(0, max(columns_length)):
                            for column2 in rows:
                                if index < column2["length"]:
                                    print(f"{column2["list"][index]:<{column2["width"]}}", end=" ")
                                else:
                                    print(f"{"":<{column2["width"]}}", end=" ")
                            print("")
                        print("")

                        rows = [column]
                        total_width = column["width"] + 1

                for column2 in rows:
                    print(f"{column2["header"]:<{column2["width"]}}", end=" ")
                print()
                
                for column2 in rows:
                    print("-" * column2["width"], end=" ")
                print("")
                
                columns_length = []
                for column2 in rows:
                    columns_length.append(column2["length"])
                for index in range(0, max(columns_length)):
                    for column2 in rows:
                        if index < column2["length"]:
                            print(f"{column2["list"][index]:<{column2["width"]}}", end=" ")
                        else:
                            print(f"{"":<{column2["width"]}}", end=" ")
                    print("")
        if reset:
            self.reset()
        return self

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