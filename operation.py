#operation.py
import tool

def listTypes():
    return ["Drill", "Pocket", "InsideContour", "OutsideContour", "Slot"]

class OperationType:
    def __init__(self, otname="newoptype"):
        self.ot_name = otname
        self.depth = 0

class Pocket(OperationType):
    def __init__(self):
        super().__init__("pocket")


class InsideContour(OperationType):
    def __init__(self):
        super().__init__("inside_contour")


class OutsideContour(OperationType):
    def __init__(self):
        super().__init__("outside_contour")


class Slot(OperationType):
    def __init__(self):
        super().__init__("slot")


class Drill(OperationType):
    def __init__(self):
        super().__init__("drill")


class Operation:
    def __init__(self):
        self.op_type = None
        self.depth = 0
        self.tool = tool.Tool()
