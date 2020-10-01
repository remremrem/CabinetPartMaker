#cabinet.py

import job_settings
import geometry
from enum import Enum

# class to represent middle spanners or fixed shelves
class Spanner:

    #PLACEMENT ENUMS
    FRONT = 1
    MID = 2
    BACK = 3

    def __init__(self):
        self.depth = 0
        self.placement = Spanner.FRONT
        self.location = 0 #location from bottom of cabinet to center of spanner
        
        
# class to represent vertical dividers
class Divider:

    #PLACEMENT ENUMS
    FRONT = 1
    MID = 2
    BACK = 3

    def __init__(self):
        self.depth = 0
        self.placement = Divider.FRONT
        self.location = 0 #location from left of cabinet to center of divider
        

class Face:
    
    def __init__(self):
        self.elevation = 0
        self.height = 0
        self.width = 0
        
    def __str__(self):
        return str("FACE "+
            "height: " + str(self.height) + " " +
            "width: " + str(self.width) + " " +
            "face_type: " + str(self.face_type) + " " +
            "elevation: " + str(self.elevation) + " " +
            "action: " + str(self.action) + " "
            )


class DynamicProperty:
    class Ptype(Enum):
        PERCENT = 1
        STATIC = 2
        
    def __init__(self, d=1, m=1):
        self.modifier = m
        self.d_value= d
        self.ptype = self.ptypeEnum('PERCENT')
        
    def ptypeEnum(self, t):
        if t:
            return self.Ptype[str(t)]
        
    @property    
    def value(self):
        if self.ptype.value == 1:
            return self.modifier * self.d_value
        elif self.ptype.value == 2:
            return self.d_value


# class to represent vertical dividers
class CellDivider:
    def __init__(self, t=.75, q=1):
        self.thickness = t
        self.quantity = q
        
        
class Cell(list): #these are the cells that make up the "cabinet face grid"
    
    class Border(Enum): #enums for bordering cell configuration
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
        
    class CellType(Enum): #CELL TYPE ENUMS
        OPEN = 1 # unfaced opening in the cabinet
        DOOR = 2 # opening with a door covering it
        DRAWER = 3 # opening with a drawer inside it
        FALSE = 4
        ROW = 5 # this cell holds a row of other cells
        COLUMN = 6 # this cell holds a column of other cells

    class CellAction(Enum): #DOOR SWING (ACTION) ENUMS    
        FIXED = 1
        SWING_LEFT = 2
        SWING_RIGHT = 3
        SWING_PAIR = 4
        SWING_UP = 5
        SWING_DOWN = 6
        PULLOUT = 7
        TIPOUT = 8

    def __init__(self, celltype=None, action=None, divider=None, region=None, face=None, size=geometry.Point(1,1), depth=None):
        super().__init__()
        self.pos = 0
        self.parent = None
        self.region = region
        self.divider = divider
        self.face = None
        self.size = size
        self.depth = depth
        
        
        if celltype:
            try:
                self.cell_type = Cell.CellType(int(celltype))
            except:
                self.cell_type = Cell.CellType[celltype.upper()]
        else:
            print("NO CELL TYPE: ", id(self))
            self.cell_type = None
            
        if action:
            try:
                self.action = Cell.CellAction(int(action))
            except:
                self.action = Cell.CellAction[action.upper()]
        else:
            self.action = None
            
        if not action and celltype == 3:
            self.action = 7
            
    def __str__(self):
        return str(id(self)) + ", type: " + str(self.cell_type.name) + ", pos: " + str(self.pos) + ", len: " + str(len(self)) + ", size: " + str(self.size)
            
    def __repr__(self):
        return self.__str__()
    
    def addCell(self, newcell):
        #print("addCell: ", newcell, " to: ", self)
        newcell.parent = self
        newcell.pos = len(self)
        self.append(newcell)
    
    def printTree(self, tab=0):
        t=tab
        l = str(" ")*tab + self.__str__() +"\n"
        if self.cell_type.value > 4:
            t+=4
            for each in self:
                l += each.printTree(t)
        return l
    
    def addBorder(self, b):
        if b:
            try:
                self.adjacent_cells += int(b)
            except:
                try:
                    self.adjacent_cells += self.CellType[str(b)].value
                except:
                    print("Invalid Border Value: ", b + "\n must use one of following values: " + list(self.Border))
                    
    @staticmethod        
    def typeEnum(t):
        if t:
            try:
                return Cell.CellType(int(t))
            except:
                try:
                    return Cell.CellType[str(t)]
                except:
                    print("Invalid typeEnum Value: ", b + "\n must use one of following values: " + list(Cell.CellType))
    
    @staticmethod
    def actionEnum(a):
        if a:
            try:
                return Cell.CellAction(int(a))
            except:
                try:
                    return Cell.CellAction[str(a)]
                except:
                    print("Invalid actionEnum Value: ", b + "\n must use one of following values: " + list(Cell.CellAction))

        
        
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
        


class WallCabinet(Cabinet):
    # *args and **kwargs automagically pass arguments to parent class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.finished_bottom = False
        self.finished_top = False
        
    def makeParts(self):
        pass
        

class BaseCabinet(Cabinet):
    # *args and **kwargs automagically pass arguments to parent class
    def __init__(self, kick_height=4, kick_depth=2.5, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.kick_height = kick_height
        self.kick_depth = kick_depth
        self.front_strip_depth = 5
        self.back_strip_depth = 5
        
        self.mid_spanners = []
       

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
    def __init__(self, kick_height=4, kick_depth=2.5, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.kick_height = kick_height
        self.kick_depth = kick_depth
        self.finished_top = False


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
