#tool.py

class Tool:
    def __init__(self, tname="newtool", diameter=0):
        self.tool_name = tname
        self.diameter = diameter
        self.chipload = 0
        self.flutes = 2
