"""
Docstring for applications.page
"""

import questionary

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