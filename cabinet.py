#cabinet.py

import job_settings


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


class Cell: #these are the cells that make up the "cabinet face grid"
    #CELL TYPE ENUMS
    OPEN = 0 # unfaced opening in the cabinet
    DOOR = 1 # opening with a door covering it
    DRAWER = 2 # opening with a drawer inside it
    ROW = 3 # this cell holds a row of other cells
    COLUMN = 4 # this cell holds a column of other cells
    
    #DOOR SWING (ACTION) ENUMS
    FIXED = 0
    SWING_LEFT = 1
    SWING_RIGHT = 2
    SWING_PAIR = 3
    SWING_UP = 4
    SWING_DOWN = 5
    PULLOUT = 6
    TIPOUT = 7
    
    def __init__(self, t=None, a=None):
        self.cell_type = t
        self.action = a
        self.cells = []
        if not a and t == 2:
            self.action = 6
    
    def addCell(self, newcell):
        self.cells.append(newcell)
        
    def asList(self):
        l = [self.cell_type]
        if self.cell_type > 2:
            for each in self.cells:
                l.append(each.asList())
        else:
            l.append(self)
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
            if l[cellcount].cell_type > 2:
                cell = l[cellcount]
                cells = Cell.fromList(l[cellcount+1])
                for each in cells:
                    cell.cells.append(each)
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
        
        self.cells = None
        
        self.parts = None


class WallCabinet(Cabinet):
    # *args and **kwargs automagically pass arguments to parent class
    def __init__(self, kick_height=4, kick_depth=2.5, *args, **kwargs):
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
    def __init__(self, left_width=32, right_width=32, left_side_depth=24,
        right_side_depth=24, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.left_side_depth = self.depth
        self.right_side_depth = self.depth
        self.left_width = self.left_width
        self.right_width = self.right_width
