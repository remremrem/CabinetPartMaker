#parts.py
import joinery, excisions, job_settings, geometry
        
class Part:
    #ANCHOR (DEPTH PLACEMENT) ENUMS
    FRONT = 1
    MID = 2
    BACK = 4
    PLACEMENT_ENUMS = {1:"FRONT", 2:"MID", 4:"BACK"}
    
    #FACING (ORIENTATION) ENUMS
    FRONT = 1
    TOP = 2
    BACK=  4
    BOTTOM = 8
    LEFT = 16
    RIGHT = 32
    FACING_ENUMS = {1:"FRONT", 2:"TOP", 4:"BACK", 8:"BOTTOM", 16:"LEFT", 32:"RIGHT", }
    
    def __init__(self, part_name="newpart", material="casework", shape="rectangle", cell=None, anchor=1, facing=2, anchor_adjust=0, x=0, y=0):
        self.length = x
        self.width = y
        self.material = material
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
        self.t = geometry.Point(0,0) #top
        self.b = geometry.Point(0,0) #bottom
        self.l = geometry.Point(0,0) #left
        self.r = geometry.Point(0,0) #right
        self.k = geometry.Point(0,0) #back
        self.f = geometry.Point(0,0) #front
        self.orient()
        
    def orient(self):
        if self.facing == Part.FRONT:
            self.t = geometry.Point(0,1)
            self.b = geometry.Point(0,-1)
            self.l = geometry.Point(-1,0)
            self.r = geometry.Point(1,0)
        elif self.facing == Part.BACK:
            self.t = geometry.Point(0,-1)
            self.b = geometry.Point(0,1)
            self.l = geometry.Point(-1,0)
            self.r = geometry.Point(1,0)
        elif self.facing == Part.TOP:
            self.l = geometry.Point(-1,0)
            self.r = geometry.Point(1,0)
            self.k = geometry.Point(0,1)
            self.f = geometry.Point(0,-1)
        elif self.facing == Part.BOTTOM:
            self.l = geometry.Point(-1,0)
            self.r = geometry.Point(1,0)
            self.k = geometry.Point(0,-1)
            self.f = geometry.Point(0,1)
        elif self.facing == Part.LEFT:
            self.t = geometry.Point(1,0)
            self.b = geometry.Point(-1,0)
            self.k = geometry.Point(0,1)
            self.f = geometry.Point(0,-1)
        elif self.facing == Part.RIGHT:
            self.t = geometry.Point(-1,0)
            self.b = geometry.Point(1,0)
            self.k = geometry.Point(0,1)
            self.f = geometry.Point(0,-1)
        
        
        
        
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
    
    def copy(self):
        newpart = Part(x=self.x, y=self.y, part_name=self.part_name, material=self.material, shape=self.shape, 
                       cell=self.cell, anchor=self.anchor, facing=self.facing, anchor_adjust=self.anchor_adjust)
        newpart.joints = self.joints
        newpart.excisions = self.excisions
        newpart.location = self.location
        return newpart
    


def HorizontalDivider(x=0, y=0, n="HorizontalDivider", material=None, settings=job_settings.JobSettings(), shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.TOP):
    m = material
    if not m:
        m = settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing)
    return part

def VerticalDivider(x=0, y=0, n="VerticalDivider", material=None, settings=job_settings.JobSettings(), shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.LEFT):
    m = material
    if not m:
        m = settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing)
    return part

def FrontSpanner(x=0, y=0, n="FrontSpanner", material=None, settings=job_settings.JobSettings(), shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.BOTTOM):
    m = material
    if not m:
        m = settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing)
    return part

def BackSpanner(x=0, y=0, n="BackSpanner", material=None, settings=job_settings.JobSettings(), shape="rectangle", cell=None, anchor=Part.BACK, facing=Part.BOTTOM):
    m = material
    if not m:
        m = settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing)
    return part

def VerticalFrontSpanner(x=0, y=0, n="VerticalFrontSpanner", material=None, settings=job_settings.JobSettings(), shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.BACK):
    m = material
    if not m:
        m = settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing)
    return part

def VerticalBackSpanner(x=0, y=0, n="VerticalBackSpanner", material=None, settings=job_settings.JobSettings(), shape="rectangle", cell=None, anchor=Part.BACK, facing=Part.FRONT):
    m = material
    if not m:
        m = settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing)
    return part

def HingeStrip(x=0, y=0, n="HingeStrip", material=None, settings=job_settings.JobSettings(), shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.LEFT):
    m = material
    if not m:
        m = settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing)
    return part

def BlindPanel(x=0, y=0, n="BlindPanel", material=None, settings=job_settings.JobSettings(), shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.BACK):
    m = material
    if not m:
        m = settings.blind_panel_material
    part = Part(n, m, shape, cell, anchor, facing)
    return part

def IntegratedKick(x=0, y=0, n="IntegratedKick", material=None, settings=job_settings.JobSettings(), shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.FRONT):
    m = material
    if not m:
        m = settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing)
    return part

def Shelf(x=0, y=0, n="Shelf", material=None, settings=job_settings.JobSettings(), shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.TOP):
    m = material
    if not m:
        m = settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing)
    return part

def AdjustableShelf(x=0, y=0, n="AdjustableShelf", material=None, settings=job_settings.JobSettings(), shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.TOP):
    m = material
    if not m:
        m = settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing)
    return part

def Bottom(x=0, y=0, n="Bottom", material=None, settings=job_settings.JobSettings(), shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.TOP):
    m = material
    if not m:
        m = settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing)
    return part

def Top(x=0, y=0, n="Top", material=None, settings=job_settings.JobSettings(), shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.BOTTOM):
    m = material
    if not m:
        m = settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing)
    return part

def LeftSide(x=0, y=0, n="LeftSide", material=None, settings=job_settings.JobSettings(), shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.RIGHT):
    m = material
    if not m:
        m = settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing)
    return part

def RightSide(x=0, y=0, n="RightSide", material=None, settings=job_settings.JobSettings(), shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.LEFT):
    m = material
    if not m:
        m = settings.casework_material
    part = Part(n, m, shape, cell, anchor, facing)
    return part

def Back(x=0, y=0, n="Back", material=None, settings=job_settings.JobSettings(), shape="rectangle", cell=None, anchor=Part.BACK, facing=Part.FRONT):
    m = material
    if not m:
        m = settings.back_material
    part = Part(n, m, shape, cell, anchor, facing)
    return part

def DrawerSide(x=0, y=0, n="DrawerSide", material=None, settings=job_settings.JobSettings(), shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.LEFT):
    m = material
    if not m:
        m = settings.drawer_box_material
    part = Part(n, m, shape, cell, anchor, facing)
    return part

def DrawerFront(x=0, y=0, n="DrawerFront", material=None, settings=job_settings.JobSettings(), shape="drawer_end_front", cell=None, anchor=Part.FRONT, facing=Part.BACK):
    m = material
    if not m:
        m = settings.drawer_box_material
    part = Part(n, m, shape, cell, anchor, facing)
    return part

def DrawerBack(x=0, y=0, n="DrawerBack", material=None, settings=job_settings.JobSettings(), shape="drawer_end_back", cell=None, anchor=Part.BACK, facing=Part.FRONT):
    m = material
    if not m:
        m = settings.drawer_box_material
    part = Part(n, m, shape, cell, anchor, facing)
    return part

def DrawerBottom(x=0, y=0, n="DrawerBottom", material=None, settings=job_settings.JobSettings(), shape="rectangle", cell=None, anchor=Part.FRONT, facing=Part.TOP):
    m = material
    if not m:
        m = settings.drawer_bottom_material
    part = Part(n, m, shape, cell, anchor, facing)
    return part
        
        
