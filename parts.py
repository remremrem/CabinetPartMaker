#parts.py
import joinery, excisions, job_settings, geometry, coordinates
from geometry import Point3 as P3
        
class Part:
    #ANCHOR (PLACEMENT) ENUMS
    FRONT = 1
    MID = 2
    BACK = 4
    TOP = 8
    BOTTOM = 16
    LEFT = 32
    RIGHT = 64
    PLACEMENT_ENUMS = {1:"FRONT", 2:"MID", 4:"BACK", 8:"TOP", 16:"BOTTOM", 32:"LEFT", 64:"RIGHT"}
    
    #FACING (ORIENTATION) ENUMS
    FRONT = 1
    TOP = 2
    BACK=  4
    BOTTOM = 8
    LEFT = 16
    RIGHT = 32
    FACING_ENUMS = {1:"FRONT", 2:"TOP", 4:"BACK", 8:"BOTTOM", 16:"LEFT", 32:"RIGHT", }
    
    def __init__(self, part_name="newpart", material=job_settings.casework_material, shape="rectangle", cell=None, anchor=1, facing=2, origin=P3(0,0,0), x=0, y=0, anchor_adjust=0):
        self.size = P3(x, y, material.thickness)
        self._material = material
        self.part_name = part_name
        self.joints = []
        self.excisions = []
        self.facing = facing
        self.anchor_adjust = anchor_adjust
        self.location = (0,0)
        self.shape = shape # rectangle, drawer_end_front, drawer_end_back, corner_90_left, corner_90_right, corner_90, corner_45
        self.anchor = anchor
        self.cell = cell
        self.border_cells = (None, None)
        self.t = None #top
        self.b = None #bottom
        self.l = None #left
        self.r = None #right
        self.k = None #back
        self.f = None #front
        self.orient()
        self.origin = origin  # part origin is the part's closest point to the cabinet origin, in cabinet coordinates
        self.operations = [] # a list of all operations machined on this part
        
    def jointsInPartCoords(self):
        for joint in self.joints:
            print("Part name: {5}, Joint name: {0}, origin: {1}, limit: {2}, male: {3}, female: {4}".format(joint.joint_name, coordinates.cabToPart(self, joint.origin), coordinates.cabToPart(self, joint.limit), joint.male.part_name, joint.female.part_name, self.part_name))
        
    def orient(self):
        if self.facing == Part.FRONT:
            self.t = P3(0,1,0)
            self.b = P3(0,-1,0)
            self.l = P3(-1,0,0)
            self.r = P3(1,0,0)
            self.f = P3(0,0,1)
            self.k = P3(0,0,-1)
        elif self.facing == Part.BACK:
            self.t = P3(0,1,0)
            self.b = P3(0,-1,0)
            self.l = P3(-1,0,0)
            self.r = P3(1,0,0)
            self.f = P3(0,0,1)
            self.k = P3(0,0,-1)
        elif self.facing == Part.TOP:
            self.t = P3(0,1,0)
            self.b = P3(0,-1,0)
            self.l = P3(-1,0,0)
            self.r = P3(1,0,0)
            self.f = P3(0,0,1)
            self.k = P3(0,0,-1)
        elif self.facing == Part.BOTTOM:
            self.t = P3(0,1,0)
            self.b = P3(0,-1,0)
            self.l = P3(-1,0,0)
            self.r = P3(1,0,0)
            self.f = P3(0,0,1)
            self.k = P3(0,0,-1)
        elif self.facing == Part.LEFT:
            self.t = P3(0,1,0)
            self.b = P3(0,-1,0)
            self.l = P3(-1,0,0)
            self.r = P3(1,0,0)
            self.f = P3(0,0,1)
            self.k = P3(0,0,-1)
        elif self.facing == Part.RIGHT:
            self.t = P3(0,1,0)
            self.b = P3(0,-1,0)
            self.l = P3(-1,0,0)
            self.r = P3(1,0,0)
            self.f = P3(0,0,1)
            self.k = P3(0,0,-1)
        
        
      
    @property
    def x(self):
        return self.size.x
    @x.setter
    def x(self, value):
        self.size.x = value
    
    @property
    def y(self):
        return self.size.y
    @y.setter
    def y(self, value):
        self.size.y = value
    
    @property
    def length(self):
        return self.size.x
    @length.setter
    def length(self, value):
        self.size.x = value
    
    @property
    def width(self):
        return self.size.y
    @width.setter
    def width(self, value):
        self.size.y = value
    
    @property
    def z(self):
        return self._material.thickness
    
    @property
    def thickness(self):
        return self._material.thickness
    
    @property
    def material(self):
        return self._material
    @material.setter
    def material(self, value):
        self._material = value
        self.size.z = value.thickness

    @property
    def area(self):
        return self.length * self.width
    
    @property
    def volume(self):
        return self.length * self.width * self.thickness
    
    def copy(self):
        newpart = Part(x=self.x, y=self.y, part_name=self.part_name, material=self._material, shape=self.shape, 
                       cell=self.cell, anchor=self.anchor, facing=self.facing, anchor_adjust=self.anchor_adjust)
        newpart.joints = self.joints
        newpart.excisions = self.excisions
        newpart.location = self.location
        return newpart
    


def HorizontalDivider(x=0, y=0, n="HorizontalDivider", material=None, shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.TOP, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part

def VerticalDivider(x=0, y=0, n="VerticalDivider", material=None, shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.LEFT, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part

def FrontSpanner(x=0, y=0, n="FrontSpanner", material=None, shape="rectangle", cell=None, anchor=Part.FRONT+Part.TOP, facing=Part.BOTTOM, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part

def BackSpanner(x=0, y=0, n="BackSpanner", material=None, shape="rectangle", cell=None, anchor=Part.BACK+Part.TOP, facing=Part.BOTTOM, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part

def VerticalFrontSpanner(x=0, y=0, n="VerticalFrontSpanner", material=None, shape="rectangle", cell=None, anchor=Part.FRONT+Part.TOP, facing=Part.BACK, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part

def VerticalBackSpanner(x=0, y=0, n="VerticalBackSpanner", material=None, shape="rectangle", cell=None, anchor=Part.BACK+Part.TOP, facing=Part.FRONT, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part

def HingeStrip(x=0, y=0, n="HingeStrip", material=None, shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.LEFT, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part

def LeftBlindPanel(x=0, y=0, n="LeftBlindPanel", material=None, shape="rectangle", cell=None, anchor=Part.FRONT+Part.LEFT, facing=Part.BACK, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.blind_panel_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part

def RightBlindPanel(x=0, y=0, n="RightBlindPanel", material=None, shape="rectangle", cell=None, anchor=Part.FRONT+Part.RIGHT, facing=Part.BACK, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.blind_panel_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part

def IntegratedKick(x=0, y=0, n="IntegratedKick", material=None, shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.FRONT, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part

def Shelf(x=0, y=0, n="Shelf", material=None, shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.TOP, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part

def AdjustableShelf(x=0, y=0, n="AdjustableShelf", material=None, shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.TOP, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part

def Bottom(x=0, y=0, n="Bottom", material=None, shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.TOP, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part

def Top(x=0, y=0, n="Top", material=None, shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.BOTTOM, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part

def LeftSide(x=0, y=0, n="LeftSide", material=None, shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.RIGHT, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    part.origin = P3(m.thickness, 0, 0)
    return part

def RightSide(x=0, y=0, n="RightSide", material=None, shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.LEFT, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part

def Back(x=0, y=0, n="Back", material=None, shape="rectangle", cell=None, anchor=Part.BACK, facing=Part.FRONT, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.back_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part

def DrawerLeft(x=0, y=0, n="DrawerLeft", material=None, shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.RIGHT, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.drawer_box_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part

def DrawerRight(x=0, y=0, n="DrawerRight", material=None, shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.LEFT, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.drawer_box_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part

def DrawerFront(x=0, y=0, n="DrawerFront", material=None, shape="drawer_end_front", cell=None, anchor=Part.FRONT, facing=Part.BACK, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.drawer_box_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part

def DrawerBack(x=0, y=0, n="DrawerBack", material=None, shape="drawer_end_back", cell=None, anchor=Part.BACK, facing=Part.FRONT, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.drawer_box_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part

def DrawerBottom(x=0, y=0, n="DrawerBottom", material=None, shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.TOP, origin=P3(0,0,0)):
    m = material
    if not m:
        m = job_settings.drawer_bottom_material
    part = Part(n, m, shape, cell, anchor, facing, origin, x, y)
    return part
        
        
