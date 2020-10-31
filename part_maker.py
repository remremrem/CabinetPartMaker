#part_maker.py
import joinery, excisions, job_settings








def HorizontalDivider(n="HorizontalDivider", x, y, material):
    part = Part(n, x, y, material)
    return part

def VerticalDivider(n="VerticalDivider", x, y, material):
    part = Part(n, x, y, material)
    return part

def FrontSpanner(n="FrontSpanner", x, y, material):
    part = Part(n, x, y, material)
    return part

def BackSpanner(n="BackSpanner", x, y, material):
    part = Part(n, x, y, material)
    return part

def SinkFrontSpanner(n="SinkFrontSpanner", x, y, material):
    part = Part(n, x, y, material)
    return part

def SinkBackSpanner(n="SinkBackSpanner", x, y, material):
    part = Part(n, x, y, material
    return part

def HingeStrip(n="HingeStrip", x, y, material):
    part = Part(n, x, y, material)
    return part

def BlindPanel(n="BlindPanel", x, y, material):
    part = Part(n, x, y, material)
    return part

def ToeKick(n="ToeKick", x, y, material):
    part = Part(n, x, y, material)
    return part

def Shelf(n="Shelf", x, y, material):
    part = Part(n, x, y, material)
    return part

def Bottom(n="Bottom", x, y, material):
    part = Part(n, x, y, material)
    return part

def Top(n="Top", x, y, material):
    part = Part(n, x, y, material)
    return part

def LeftSide(n="LeftSide", x, y, material):
    part = Part(n, x, y, material)
    return part

def RightSide(n="RightSide", x, y, material):
    part = Part(n, x, y, material)
    return part

def Back(n="Back", x, y, material):
    part = Part(n, x, y, material)
    return part

def DrawerSide(n="DrawerSide", x, y, material):
    part = Part(n, x, y, material)
    return part

def DrawerFront(n="DrawerFront", x, y, material):
    part = Part(n, x, y, material)
    return part

def DrawerBack(n="DrawerBack", x, y, material):
    part = Part(n, x, y, material)
    return part
    
        
class Part:
    def __init__(self, part_name="newpart", x=0, y=0, material="casework", shape="rectangle"):
        self.length = x
        self.width = y
        self.material = material
        self.part_name = part_name
        self.joints = []
        self.excisions = []
        self.location = (0,0)
        self.shape = "rectangle"
        self.anchor = "front" # front, back, middle
        
        
        
    @property
    def x(self):
        return self.length
    @x.setter
    def x(self, value):
        self.length = value
    
    @property
    def y(self):
        return self.width
    @y.setter
    def y(self, value):
        self.width = value
        
    def area(self):
        return self.length * self.width
    
        
        
