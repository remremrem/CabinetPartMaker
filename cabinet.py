#cabinet.py

import job_settings
from enum import Enum

def newCab(cabinet_type="base", cab_name="Cabinet", width=24, height=30.5, depth=23.875, grid=[], faces=[], 
           rightside=0, leftside=0, leftback=0, rightback=0, fl=0, fr=0, fbk=0, fbt=0, ft=0, trv=.25, rrv=.0625, lrv=.0625, 
           brv=0, doorgap=.125, drawergap=.125, unitnum=1, shape="rect"):
    newcab = None
    if cabinet_type == "base":
        newcab = BaseCabinet()
        
    elif cabinet_type == "wall":
        newcab = WallCabinet()
        newcab.finished_bottom = fbt
        
    elif cabinet_type == "tall":
        newcab = TallCabinet()
        
    elif cabinet_type == "base_corner":
        newcab = BaseCorner()
        newcab.right_side_depth = rightside
        newcab.left_side_depth = leftside
        newcab.right_width = rightback
        newcab.left_width = leftback
        
    elif cabinet_type == "wall_corner":
        newcab = WallCorner()
        newcab.finished_bottom = fbt
        
    elif cabinet_type == "tall_corner":
        newcab = TallCorner()
        
    newcab.cab_name = cab_name
    newcab.unit_number = unitnum
    newcab.width = width
    newcab.height = height
    newcab.depth = depth
    newcab.left_reveal = lrv
    newcab.right_reveal = rrv
    newcab.bottom_reveal = brv
    newcab.top_reveal = trv
    
    newcab.door_gap = doorgap
    newcab.drawer_gap = drawergap
    newcab.finished_left = fl
    newcab.finished_right = fr
    newcab.finished_back = fbk
    newcab.finished_top = ft
    
    return newcab
        

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
    
    class FaceType(Enum): #CELL TYPE ENUMS
        OPEN = 1 # unfaced opening in the cabinet
        DOOR = 2 # opening with a door covering it
        DRAWER = 3 # opening with a drawer inside it
        FALSE = 4 # a false front

    class FaceAction(Enum): #DOOR SWING (ACTION) ENUMS    
        FIXED = 1
        SWING_LEFT = 2
        SWING_RIGHT = 3
        SWING_PAIR = 4
        SWING_UP = 5
        SWING_DOWN = 6
        PULLOUT = 7
        TIPOUT = 8

    
    def __init__(self):
        self.elevation = 0
        self.height = 0
        self.width = 0
        self.face_type = self.typeEnum('OPEN')
        self.action = self.typeEnum('FIXED')
        
    def typeEnum(self, t):
        if t:
            return self.FaceType[str(t)]
        
    def actionEnum(self, a):
        if a:
            return self.FaceAction[str(a)]
        
    def __str__(self):
        return str("FACE "+
            "height: " + str(self.height) + " " +
            "width: " + str(self.width) + " " +
            "face_type: " + str(self.face_type) + " " +
            "elevation: " + str(self.elevation) + " " +
            "action: " + str(self.action) + " "
            )


class Cell: #these are the cells that make up the "cabinet face grid"
    
    class CellType(Enum): #CELL TYPE ENUMS
        OPEN = 1 # unfaced opening in the cabinet
        DOOR = 2 # opening with a door covering it
        DRAWER = 3 # opening with a drawer inside it
        ROW = 4 # this cell holds a row of other cells
        COLUMN = 5 # this cell holds a column of other cells

    class CellAction(Enum): #DOOR SWING (ACTION) ENUMS    
        FIXED = 1
        SWING_LEFT = 2
        SWING_RIGHT = 3
        SWING_PAIR = 4
        SWING_UP = 5
        SWING_DOWN = 6
        PULLOUT = 7
        TIPOUT = 8

    def __init__(self, t=None, a=None):
        self.cell_type = self.typeEnum(t)
        self.action = self.actionEnum(a)
        self.cells = []
        self.divider = []
        self.face = []
        self.parent = None
        if not a and t == 3:
            self.action = 7
    
    def addCell(self, newcell):
        newcell.parent = self
        self.cells.append(newcell)
        
    def typeEnum(self, t):
        if t:
            return self.CellType[str(t)]
        
    def actionEnum(self, a):
        if a:
            return self.CellAction[str(a)]
            
    def __str__(self):
        return str([self, self.cell_type, self.parent])
    
    def printTree(self, tab=0):
        t=tab
        l = str(" ")*tab + self.__str__() +"\n"
        if self.cell_type.value > 3:
            t+=4
            for each in self.cells:
                l += each.printTree(t)
        return l
        
    def asList(self):
        l = [self]
        if self.cell_type.value > 3:
            l.append(self.cell_type)
            for each in self.cells:
                l.append(each.asList())
        else:
            l.append(self.cell_type)
        return l
    
    @staticmethod
    def fromList(l): # generate an "cabinet face grid" from a list of cells
        # example list: [ Cell(Cell.COLUMN),
        #                 [
        #                   Cell(Cell.ROW), 
        #                   [ 
        #                       Cell(Cell.DRAWER), 
        #                       Cell(Cell.DRAWER),
        #                   ],
        #                   Cell(Cell.DRAWER), 
        #                   Cell(Cell.DRAWER),
        #                 ],
        #               ]
        # this list represents a cabinet with two drawers side by side on top, 
        # one drawer in the middle, and one drawer in the bottom
        
        cell_list = []
        cellcount = 0
        while cellcount < len(l):
            if l[cellcount].cell_type.value > 3:
                cell = l[cellcount]
                cells = Cell.fromList(l[cellcount+1])
                for each in cells:
                    cell.addCell(each)
                cell_list.append(cell)
                cellcount += 2
            else:
                cell_list.append(l[cellcount])
                cellcount += 1
        if cell_list:
            return cell_list
        
        
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
        
        self.parts = None


class WallCabinet(Cabinet):
    # *args and **kwargs automagically pass arguments to parent class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.finished_bottom = False
        self.finished_top = False
        

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
        self.finished_bottom = False
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
