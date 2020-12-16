#cabinet.py

import parts, geometry, joinery, job_settings
from enum import Enum
from geometry import Point3 as P3


# a property that is modified based on the state of other poperties
class DynamicProperty:
    PERCENT = 1
    STATIC = 2
        
    def __init__(self, d=1, m=1):
        self.modifier = m
        self.value= d
        self.ptype = DynamicProperty.PERCENT
        
    @property    
    def value(self):
        if self.ptype == DynamicProperty.PERCENT:
            return self.modifier * self.value
        elif self.ptype == DynamicProperty.STATIC:
            return self.value
        

class Face:

    #DOOR SWING (ACTION) ENUMS
    FIXED = 0
    SWING_LEFT = 1
    SWING_RIGHT = 2
    SWING_PAIR = 3
    SWING_UP = 4
    SWING_DOWN = 5
    PULLOUT = 6
    TIPOUT = 7
    
    def __init__(self):
        self.elevation = 0
        self.size = geometry.Point(0,0)
        self.origin = None
        self.action = Face.FIXED
        
    def __str__(self):
        return str("FACE "+
            "height: " + str(self.height) + " " +
            "width: " + str(self.width) + " " +
            "origin: " + str(self.origin) + " " +
            "limit: " + str(self.limit) + " " 
            )
    
    @property
    def height(self):
        return self.size.y
    
    @height.setter
    def height(self, value):
        self.size = geometry.Point(self.size.x, value)
    
    @property
    def width(self):
        return self.size.x
    
    @width.setter
    def width(self, value):
        self.size = geometry.Point(value, self.size.y)
    
    @property
    def limit(self):
        if self.origin:
            return self.origin + geometry.Point(self.width, self.height)
        else: return None


class Cell(list): #these are the cells that make up the "cabinet face grid"
    
    #enums for bordering cell configuration
    B = 1 #BOTTOM
    T = 2 #TOP
    L = 4 #LEFT
    R = 8 #RIGHT
    
    BT = 3
    BL = 5
    TL = 6
    BTL = 7
    BR = 9
    TR = 10
    BTR = 11
    LR = 12
    BLR = 13
    TLR = 14
    BTLR = 15
        
    #CELL TYPE ENUMS
    OPEN = 1 # unfaced opening in the cabinet
    DOOR = 2 # opening with a door covering it
    DRAWER = 3 # opening with a drawer inside it
    FALSE = 4
    BLIND = 5
    ROW = 6 # this cell holds a row of other cells
    COLUMN = 7 # this cell holds a column of other cells
    CELL_TYPE_NAMES = {1:"OPEN", 2:"DOOR", 3:"DRAWER", 4:"FALSE", 5:"BLIND", 6:"ROW", 7:"COLUMN"}

    #ACTION (DOOR SWING) ENUMS
    FIXED = 1
    SWING_LEFT = 2
    SWING_RIGHT = 3
    SWING_PAIR = 4
    SWING_UP = 5
    SWING_DOWN = 6
    PULLOUT = 7
    TIPOUT = 8
    CELL_ACTION_NAMES = {1:"FIXED", 2:"SWING_LEFT", 3:"SWING_RIGHT", 4:"SWING_PAIR", 5:"SWING_UP", 6:"SWING_DOWN", 7:"PULLOUT", 8:"TIPOUT"}

    def __init__(self, celltype=OPEN, action=None, dividers=[], region=None, face=None, size=geometry.Point(1,1), depth=None):
        super().__init__()
        self.pos = 0
        self.parent = None
        self.region = region
        self.face = face
        self.size = size
        self.depth = depth
        self.origin = None
        self.cell_type = celltype
        self.action = action
        if not action and self.cell_type == 3:
            self.action = 7
        
        #check if dividers is a list of dividers or just a single divider
        if hasattr(dividers, '__iter__'): 
            self.dividers = dividers
        elif not dividers:
            self.dividers = []
        else:
            self.dividers = [dividers]
            


    @property
    def limit(self):
        return self.origin + self.size
    
    
    def __str__(self):
        return ( str(id(self)) + ", type: " + str(Cell.CELL_TYPE_NAMES[self.cell_type]) + ", pos: " + str(self.pos) + 
                ", len: " + str(len(self)) + ", size: " + str(self.size) + ", divider: " + 
                str(self.dividers) + ", origin: " + str(self.origin) + ",\n" + 
                "                face: " + str(self.face) + "\n" )
            
    def __repr__(self):
        return self.__str__()
    
    def addCell(self, newcell):
        #print("addCell: ", newcell, " to: ", self)
        newcell.parent = self
        newcell.pos = len(self)
        self.append(newcell)
    
    def establishOrigin(self, cabinet, cellcount=0): #only call this function on the root cell. recursion!
        if not self.parent: #root cell only
            h = 0 
            try:
                h = cabinet.kick_height
            except:
                pass
            self.origin = geometry.Point(0,h)
            c = 0
            for each in self:
                each.establishOrigin(cabinet, c)
                c+=1
        else:
            if cellcount == 0:
                self.origin = self.parent.origin
            elif cellcount > 0:
                if self.parent.cell_type == Cell.ROW:
                    self.origin = geometry.Point(self.parent[cellcount-1].limit.x, self.parent.origin.y)
                elif self.parent.cell_type == Cell.COLUMN:
                    self.origin = geometry.Point(self.parent.origin.x, self.parent[cellcount-1].limit.y)
            if self.cell_type > 5:
                c = 0
                for each in self:
                    each.establishOrigin(cabinet, c)
                    c+=1
        if self.face:
            if self.origin.x == 0:
                self.face.origin = geometry.Point(self.origin.x + cabinet.left_reveal , self.face.elevation)
            else:
                self.face.origin = geometry.Point(self.origin.x + cabinet.door_gap*.5 , self.face.elevation)
                    
    def printTree(self, tab=0):
        t=tab
        l = str(" ")*tab + self.__str__() +"\n"
        if self.cell_type > 5:
            t+=4
            for each in self:
                l += each.printTree(t)
        return l
    
    def makeParts(self, cabinet):
        count = 0
        for cell in self:
            if cell.cell_type == Cell.BLIND:
                if cell.origin.x < 1:
                    part = parts.LeftBlindPanel(x=cabinet.height, y=cell.limit.x, cell=cell)
                    part.origin = geometry.Point3(cell.origin.x, cell.origin.y, cabinet.depth)
                else:
                    part = parts.RightBlindPanel(x=cabinet.height, y=cabinet.width-cell.origin.x, cell=cell)
                    part.origin = geometry.Point3(cell.limit.x, cell.limit.y, cabinet.depth)
                cabinet.addPart(part)
                
            elif cell.cell_type < 4 or cell.cell_type > 5 :
                if self.dividers:
                    if count < len(self)-1:
                        for d in self.dividers:
                            div=d
                            if count > 0:
                                div = d.copy()
                            div.border_cells = (self[count], self[count+1])
                            cabinet.addPart(div)
                            
            elif cell.cell_type == Cell.FALSE:
                if cell.limit.y == cabinet.height:
                    cabinet.addPart(parts.VerticalFrontSpanner(x=cabinet.internal_width, y=cell.origin.y - cabinet.drawer_gap*.5, cell=cell))
                    cabinet.addPart(parts.VerticalBackSpanner(x=cabinet.internal_width, y=job_settings.vertical_back_spanner_height))
                    
            if cell.cell_type == Cell.DOOR or cell.cell_type == Cell.DRAWER or cell.cell_type == cell.FALSE:
                cabinet.addFace(cell.face)
                
            cell.makeParts(cabinet)
            count+=1
        

        
class Cabinet:
    def __init__(self, height=30, depth=12, width=24, unit_num=1, quantity=1, name="newcab"):
        self.height = height
        self.depth = depth
        self.width = width
        self.cab_name = name
        self.unit_number = unit_num
        self.quantity = 1

        self.left_reveal = .0625
        self.right_reveal = .0625
        self.bottom_reveal = 0
        self.top_reveal = .25
        
        self.door_gap = .125
        self.drawer_gap = .125
        
        self.kh = None

        self.finished_left = False
        self.finished_right = False
        self.finished_back = False

        self.adjustable_shelves = 0
        
        self.fixed_shelves = [] #list of fixed shelves and spanners
        self.dividers = []
        
        self.faces = []
        
        self.root_cell = None
        
        self.parts = []
        self.joints = []
        
    @property
    def kick_height(self):
        if self.kh:
            return self.kh
        else:
            return 0
    @kick_height.setter
    def kick_height(self, value):
        self.kh = value
        
    @property
    def internal_width(self):
        lw = 0
        rw = 0
        ls = self.getPartByName("LeftSide")
        if ls:
            lw = ls.thickness
        rs = self.getPartByName("RightSide")
        if rs:
            rw = rs.thickness
        return self.width - (lw+rw)
        
    @property
    def internal_height(self):
        tw = 0
        bw = 0
        ts = self.getPartByName("Top")
        if ts:
            tw = ts.thickness
        bs = self.getPartByName("Bottom")
        if bs:
            bw = bs.thickness
        return self.height - (tw+bw)
        
    def addPart(self, part):
        self.parts.append(part)
        
    def addFace(self, face):
        self.faces.append(face)
        
    def getPartByName(self, part_name):
        parts = []
        for p in self.parts:
            if p.part_name.lower() == part_name.lower():
                parts.append(p)
        if len(parts) == 1:
            return parts[0]
        elif len(parts) > 1:
            return parts
        else:
            return False
        
        
    def setPartOrigins(self):
        # part origin is it's closest point to the cabinet origin, in cabinet coordinates
        left_thickness = 0
        leftside = self.getPartByName("LeftSide")
        if leftside:
            left_thickness = leftside.thickness
            
        bottom_thickness = 0
        bottom = self.getPartByName("Bottom")
        if bottom:
            bottom_thickness = bottom.thickness
            
        for p in self.parts:
            if p.part_name == "RightSide":
                p.origin = P3(self.width - p.thickness, 0, 0)
            elif p.part_name == "LeftSide":
                p.origin = P3(0,0,0)
            elif p.part_name == "Bottom":
                p.origin = P3(left_thickness, self.kick_height, 0)
            elif p.part_name == "Top":
                p.origin = P3(left_thickness, self.height - p.thickness, 0)
            elif p.part_name == "Back":
                p.origin = P3(left_thickness, self.kick_height + bottom_thickness, job_settings.back_inset)
            elif p.part_name == "FrontSpanner":
                p.origin = P3(left_thickness, self.height - p.thickness, self.depth - p.size.y)
            elif p.part_name == "BackSpanner":
                p.origin = P3(left_thickness, self.height - p.thickness, 0)
            elif p.part_name == "VerticalFrontSpanner":
                p.origin = P3(left_thickness, self.height - p.y, self.depth - p.thickness)
            elif p.part_name == "VerticalBackSpanner":
                p.origin = P3(left_thickness, self.height - p.y, 0)
            elif p.part_name == "LeftBlindPanel":
                p.origin = P3(0, self.kick_height, self.depth - p.thickness)
            elif p.part_name == "RightBlindPanel":
                p.origin = P3(self.width - p.y, self.kick_height, self.depth - p.thickness)
            elif p.part_name == "IntegratedKick":
                p.origin = P3(left_thickness, self.kick_height - p.y, self.depth - p.thickness)
            """elif p.part_name == "DrawerFront":
                p.origin = P3(left_thickness, self.height - p.y, 0)
            elif p.part_name == "DrawerBack":
                p.origin = P3(left_thickness, self.height - p.y, 0)
            elif p.part_name == "DrawerRight":
                p.origin = P3(left_thickness, self.height - p.y, 0)
            elif p.part_name == "DrawerLeft":
                p.origin = P3(left_thickness, self.height - p.y, 0)
            elif p.part_name == "DrawerBottom":
                p.origin = P3(left_thickness, self.height - p.y, 0)"""
        
        


class WallCabinet(Cabinet):
    # *args and **kwargs automagically pass arguments to parent class
    def __init__(self, open_back=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.finished_bottom = False
        self.finished_top = False
        
        ls = parts.LeftSide(x=self.height, y=self.depth)
        print("LEFTSIDE!!!!!!!: ", ls, ls.size, self.height, self.depth)
        rs = parts.RightSide(x=self.height, y=self.depth)        
        self.addPart(ls)
        self.addPart(rs)
        top = parts.Top(x=self.internal_width, y=self.depth)
        joinery.ScrewJoint(top, ls, P3(ls.thickness, self.height-top.thickness, 0), P3(ls.thickness, self.height, self.depth))
        joinery.ScrewJoint(top, rs, P3(self.width-rs.thickness, self.height-top.thickness, 0), P3(self.width-rs.thickness, self.height, self.depth))
        bot = parts.Bottom(x=self.internal_width, y=self.depth)
        joinery.ScrewJoint(bot, ls, P3(ls.thickness, self.kick_height, 0), P3(ls.thickness, self.kick_height+bot.thickness, self.depth))
        joinery.ScrewJoint(bot, rs, P3(self.width-rs.thickness, self.kick_height, 0), P3(self.width-rs.thickness, self.kick_height+bot.thickness, self.depth))
        self.addPart(top)
        self.addPart(bot)
        if not open_back:
            back = parts.Back(x=self.internal_width, y=self.internal_height)
            
            joinery.Dado(back, ls, P3(ls.thickness, self.kick_height+bot.thickness, job_settings.back_inset), 
                                    P3(ls.thickness, self.height-top.thickness, job_settings.back_inset+job_settings.back_material.thickness))
            
            joinery.Dado(back, rs, P3(self.width-rs.thickness, self.kick_height+bot.thickness, job_settings.back_inset), 
                                    P3(self.width-rs.thickness, self.height-top.thickness, job_settings.back_inset+job_settings.back_material.thickness))
            
            joinery.Dado(back, top, P3(ls.thickness, self.height-top.thickness, job_settings.back_inset), 
                                    P3(self.width-rs.thickness, self.height-top.thickness, job_settings.back_inset+job_settings.back_material.thickness))
            
            joinery.Dado(back, bot, P3(ls.thickness, self.kick_height+bot.thickness, job_settings.back_inset), 
                        P3(self.width-rs.thickness, self.kick_height+bot.thickness, job_settings.back_inset+job_settings.back_material.thickness))
            
            self.addPart(back)
        

class BaseCabinet(Cabinet):
    # *args and **kwargs automagically pass arguments to parent class
    def __init__(self, kick_height=4, kick_depth=2.5, false_front=False, open_back=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.kick_height = kick_height
        self.kick_depth = kick_depth
        self.front_strip_depth = 5
        self.back_strip_depth = 5
        
        self.addPart(parts.LeftSide())
        self.addPart(parts.RightSide())
        self.addPart(parts.Bottom())
        if kick_height > 0:
            self.addPart(parts.IntegratedKick())
        if not open_back:
            self.addPart(parts.Back())
        if not false_front:
            self.addPart(parts.FrontSpanner())
            self.addPart(parts.BackSpanner())
       

class BaseCorner(BaseCabinet):
    def __init__(self, left_width=32, right_width=32, left_side_depth=24,
        right_side_depth=24, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.left_side_depth = self.depth
        self.right_side_depth = self.depth
        self.left_width = self.left_width
        self.right_width = self.right_width


class TallCabinet(Cabinet):
    # *args and **kwargs automagically pass arguments to parent class
    def __init__(self, kick_height=4, kick_depth=2.5, open_back=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.kick_height = kick_height
        self.kick_depth = kick_depth
        self.finished_top = False
        
        self.addPart(parts.LeftSide())
        self.addPart(parts.RightSide())
        self.addPart(parts.Top())
        self.addPart(parts.Bottom())
        if kick_height > 0:
            self.addPart(parts.IntegratedKick())
        if not open_back:
            self.addPart(parts.Back())


class TallCorner(TallCabinet):
    def __init__(self, left_width=32, right_width=32, left_side_depth=24,
        right_side_depth=24, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.left_side_depth = self.depth
        self.right_side_depth = self.depth
        self.left_width = self.left_width
        self.right_width = self.right_width


class WallCorner(WallCabinet):
    def __init__(self, left_width=24, right_width=24, left_side_depth=12,
        right_side_depth=12, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.left_side_depth = self.depth
        self.right_side_depth = self.depth
        self.left_width = self.left_width
        self.right_width = self.right_width
