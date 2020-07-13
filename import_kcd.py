# import_kcd.py

import cabinet


def parseCSV(csv):
    file = open(csv, "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        blah blah blah


def setDefaults(kcdcab, newcab):
    newcab.left_reveal = kcdcab.left_reveal
    newcab.right_reveal = kcdcab.right_reveal
    newcab.bottom_reveal = kcdcab.bottom_reveal
    newcab.top_reveal = kcdcab.top_reveal
    newcab.door_gap = kcdcab.door_gap
    newcab.drawer_gap = kcdcab.drawer_gap
    newcab.finished_left = kcdcab.finished_left
    newcab.finished_right = kcdcab.finished_right
    newcab.adjustable_shelves = kcdcab.adjustable_shelves
    newcab.fixed_shelves = kcdcab.fixed_shelves
    
        
def convert(cab):
    newcab = None
    if cab.ztype == "101":
        newcab = cabinet.Cabinet(cab.height, cab.depth, cab.width, cab.unit_num, cab.quantity, "Upper Cabinet")
        setDefaults(cab, newcab)

        
        
class KCD_Cab:
    def __init__(self):
        self.ztype = 0
        self.unit_num = 0
        self.unit_name = 0
        self.quantity = 0
        self.height = 0
        self.width = 0
        self.depth = 0
        self.bot_reveal = 0
        self.left_reveal = 0
        self.right_reveal = 0
        self.top_reveal = 0
        self.doorgap = 0
        self.drawergap = 0
        self.doors = []
        self.drawers = []
        self.left_side_depth = 0
        self.right_side_depth = 0
        self.kick_height = 0
        self.kick_depth = 0
        self.adjustable_shelves = 0
        self.openings = []
        
        
class KCD_Face:
    #FACE TYPE ENUMS
    OPEN = 0
    DOOR = 1
    DRAWER = 2
    FALSE = 3
    
    #DOOR SWING ENUMS
    FIXED = 0
    LEFT_SWING = 1
    RIGHT_SWING = 2
    UP_SWING = 3
    DOWN_SWING = 4
    PULLOUT = 5
    TIPOUT = 6
    
    def __init__(self):
        self.elevation = 0
        self.height = 0
        self.width = 0
        self.face_type = KCD_Face.OPEN
        self.action = KCD_Face.FIXED
        
        
        
        
        
        
