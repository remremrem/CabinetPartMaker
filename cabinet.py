#cabinet.py



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

        self.adjustable_shelves = 0
        
        self.fixed_shelves = [] #list of fixed shelves and spanners
        self.dividers = []


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


class TallCorner(TallCabinet):
    def __init__(self, left_width=32, right_width=32, left_side_depth=24,
        right_side_depth=24, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.left_side_depth = self.depth
        self.right_side_depth = self.depth
        self.left_width = self.left_width
        self.right_width = self.right_width


class WallCorner(Cabinet):
    def __init__(self, left_width=32, right_width=32, left_side_depth=24,
        right_side_depth=24, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.left_side_depth = self.depth
        self.right_side_depth = self.depth
        self.left_width = self.left_width
        self.right_width = self.right_width
