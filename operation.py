#operation.py
import tool, geometry

def listTypes():
    return ["Drill", "Pocket", "InsideContour", "OutsideContour", "Slot"]

class Operation:
    def __init__(self, op_type="new_op_type", op_name="new_operation"):
        self.depth = 0
        self.op_name = op_name
        self.op_type = op_type
        self.tool = tool.Tool()
        self.location = geometry.Point(0,0)
        

class Pocket(Operation):
    def __init__(self, width=0, length=0, *args, **kwargs):
        super().__init__(op_type="pocket", *args, **kwargs)
        self.width = width
        self.length = length


class Slot(Operation):
    def __init__(self, width=0, length=0, *args, **kwargs):
        super().__init__(op_type="slot", *args, **kwargs)
        self.width = width
        self.length = length


class Drill(Operation):
    def __init__(self, diameter=0, *args, **kwargs):
        super().__init__(op_type="drill", *args, **kwargs)
        self.diameter = diameter


class InsideContour(Operation):
    def __init__(self, *args, **kwargs):
        super().__init__(op_type="inside_contour", *args, **kwargs)


class OutsideContour(Operation):
    def __init__(self, *args, **kwargs):
        super().__init__(op_type="outside_contour", *args, **kwargs)

