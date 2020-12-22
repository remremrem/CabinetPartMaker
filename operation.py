#operation.py
import tool, geometry, job_settings


def DowelHole():
    return Drill(op_name="dowel_hole", diameter=.31496, depth=.57) #8mm diameter

def EuroHole():
    return Drill(op_name="euro_hole", diameter=.19685, depth=.57) #5mm diameter

def PilotHole(origin=geometry.Point(0,0)):
    return Drill(op_name="pilot_hole", origin=origin, diameter=.15748, depth=job_settings.casework_material.thickness + job_settings.pilot_overdrill) #4mm diameter

def listTypes():
    return ["Drill", "Pocket", "InsideContour", "OutsideContour", "Slot"]

def BackSlot(origin=None, limit=None):
    return Slot(op_name="back_slot", origin=origin, limit=limit)


class Operation:
    def __init__(self, op_type="new_op_type", op_name="new_operation", depth=0, origin=geometry.Point(0,0), limit=geometry.Point(0,0), size=None):
        self.depth = depth
        self.op_name = op_name
        self.op_type = op_type
        self.tool = tool.Tool()
        self.origin = origin
        self.limit = limit
        print("OPERATION SIZE: ", op_name, self.size, limit, origin)
        
    @property
    def center(self):
        return self.origin + (self.size*.5)
    @center.setter
    def center(self, value):
        if isinstance(value, geometry.Point):
            self.origin = value - (self.size*.5)
    
    @property
    def size(self):
        return self.limit - self.origin
    @size.setter
    def size(self, value):
        if isinstance(value, geometry.Point):
            self.limit = self.origin + value
        
    def __str__(self):
        return "Operation(name: {0}, origin: {1}, limit: {2}, depth: {3})".format(self.op_name, self.origin, self.limit, self.depth)
        

class Pocket(Operation):
    def __init__(self, width=1, length=1, *args, **kwargs):
        super().__init__(op_type="pocket", *args, **kwargs)
        self.size = geometry.Point(width, length)
        
    @property
    def width(self): return self.size.x
     
    @property
    def length(self): return self.size.y
     
    @property
    def x(self): return self.size.x
     
    @property
    def y(self): return self.size.y


class Slot(Operation):
    def __init__(self, width=1, length=1, *args, **kwargs):
        super().__init__(op_type="slot", *args, **kwargs)
        self.size = geometry.Point(width, length)
        
    @property
    def width(self): return self.size.x
     
    @property
    def length(self): return self.size.y
     
    @property
    def x(self): return self.size.x

    @x.setter
    def x(self, value):
        self.size.x = value
     
    @property
    def y(self): return self.size.y

    @y.setter
    def y(self, value):
        self.size.y = value


class Drill(Operation):
    def __init__(self, diameter=0, *args, **kwargs):
        super().__init__(op_type="drill", *args, **kwargs)
        self.diameter = diameter
        self.size = geometry.Point(0,0)
        
    @property
    def center(self):
        return self.origin
    @center.setter
    def center(self, value):
        if isinstance(value, geometry.Point):
            self.origin = value
    
    @property
    def limit(self):
        return self.origin
    @limit.setter
    def limit(self, value):
        pass


class Contour(Operation):
    def __init__(self, *args, **kwargs):
        super().__init__(op_type="contour", *args, **kwargs)
        self.points = []


class InsideContour(Contour):
    def __init__(self, *args, **kwargs):
        super().__init__(op_type="inside_contour", *args, **kwargs)


class OutsideContour(Contour):
    def __init__(self, *args, **kwargs):
        super().__init__(op_type="outside_contour", *args, **kwargs)

