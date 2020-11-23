#part_maker.py
import joinery, excisions, job_settings


def HorizontalDivider(n="HorizontalDivider", x, y, material=job_settings.casework_material, shape="rectangle", cell=None, anchor=Part.FRONT):
    part = Part(n, x, y, m, s, cell, anchor)
    return part

def VerticalDivider(n="VerticalDivider", x, y, material=job_settings.casework_material, shape="rectangle", cell=None, anchor=Part.FRONT):
    part = Part(n, x, y, m, s, cell, anchor)
    return part

def FrontSpanner(n="FrontSpanner", x, y, material=job_settings.casework_material, shape="rectangle", cell=None, anchor=Part.FRONT):
    part = Part(n, x, y, m, s, cell, anchor)
    return part

def BackSpanner(n="BackSpanner", x, y, material=job_settings.casework_material, shape="rectangle", cell=None, anchor=Part.BACK):
    part = Part(n, x, y, m, s, cell, anchor)
    return part

def VerticalFrontSpanner(n="VerticalFrontSpanner", x, y, material=job_settings.casework_material, shape="rectangle", cell=None, anchor=Part.FRONT):
    part = Part(n, x, y, m, s, cell, anchor)
    return part

def VerticalBackSpanner(n="VerticalBackSpanner", x, y, material=job_settings.casework_material, shape="rectangle", cell=None, anchor=Part.BACK):
    part = Part(n, x, y, m, s, cell, anchor)
    return part

def HingeStrip(n="HingeStrip", x, y, material=job_settings.casework_material, shape="rectangle", cell=None, anchor=Part.FRONT):
    part = Part(n, x, y, m, s, cell, anchor)
    return part

def BlindPanel(n="BlindPanel", x, y, material=job_settings.casework_material, shape="rectangle", cell=None, anchor=Part.FRONT):
    part = Part(n, x, y, m, s, cell, anchor)
    return part

def IntegratedKick(n="IntegratedKick", x, y, material=job_settings.casework_material, shape="rectangle", cell=None, anchor=Part.FRONT):
    part = Part(n, x, y, m, s, cell, anchor)
    return part

def Shelf(n="Shelf", x, y, material=job_settings.casework_material, shape="rectangle", cell=None, anchor=Part.FRONT):
    part = Part(n, x, y, m, s, cell, anchor)
    return part

def AdjustableShelf(n="AdjustableShelf", x, y, material=job_settings.casework_material, shape="rectangle", cell=None, anchor=Part.FRONT):
    part = Part(n, x, y, m, s, cell, anchor)
    return part

def Bottom(n="Bottom", x, y, material=job_settings.casework_material, shape="rectangle", cell=None, anchor=Part.FRONT):
    part = Part(n, x, y, m, s, cell, anchor)
    return part

def Top(n="Top", x, y, material=job_settings.casework_material, shape="rectangle", cell=None, anchor=Part.FRONT):
    part = Part(n, x, y, m, s, cell, anchor)
    return part

def LeftSide(n="LeftSide", x, y, material=job_settings.casework_material, shape="rectangle", cell=None, anchor=Part.FRONT):
    part = Part(n, x, y, m, s, cell, anchor)
    return part

def RightSide(n="RightSide", x, y, material=job_settings.casework_material, shape="rectangle", cell=None, anchor=Part.FRONT):
    part = Part(n, x, y, m, s, cell, anchor)
    return part

def Back(n="Back", x, y, material=job_settings.back_material, shape="rectangle", cell=None, anchor=Part.BACK):
    part = Part(n, x, y, m, s, cell, anchor)
    return part

def DrawerSide(n="DrawerSide", x, y, material=job_settings.drawer_box_material, shape="rectangle", cell=None, anchor=Part.FRONT):
    part = Part(n, x, y, m, s, cell, anchor)
    return part

def DrawerFront(n="DrawerFront", x, y, material=job_settings.drawer_box_material, shape="drawer_end_front", cell=None, anchor=Part.FRONT):
    part = Part(n, x, y, m, s, cell, anchor)
    return part

def DrawerBack(n="DrawerBack", x, y, material=job_settings.drawer_box_material, shape="drawer_end_back", cell=None, anchor=Part.BACK):
    part = Part(n, x, y, m, s, cell, anchor)
    return part

def DrawerBottom(n="DrawerBottom", x, y, material=job_settings.drawer_bottom_material, shape="rectangle", cell=None, anchor=Part.FRONT):
    part = Part(n, x, y, m, s, cell, anchor)
    return part
    
        
class Part:
    #DEPTH PLACEMENT ENUMS
    FRONT = 1
    MID = 2
    BACK = 4
    
    def __init__(self, part_name="newpart", x=0, y=0, material="casework", shape="rectangle", cell=None, anchor=1):
        self.length = x
        self.width = y
        self.material = material
        self.part_name = part_name
        self.joints = []
        self.excisions = []
        self.location = (0,0)
        self.shape = shape # rectangle, drawer_end_front, drawer_end_back, corner_90_left, corner_90_right, corner_90, corner_45
        self.anchor = anchor
        self.cell = cell
        
        
        
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
    
        
        
