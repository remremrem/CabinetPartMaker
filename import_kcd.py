# import_kcd.py

import cabinet


def parseCSV(csv):
    file = open(csv, "r")
    lines = file.readlines()
    file.close()
    cabs = []
    for line in lines:
        if "record=cabinet" in line:
            cab = KCD_Cab()
            for prop in line.split(","):
                if " cabname=" in prop:
                    cab.cab_name = prop.split("=")[1]
                elif " doorgap=" in prop:
                    cab.door_gap = float(prop.split("=")[1])
                elif " rightside=" in prop:
                    cab.right_side = float(prop.split("=")[1])
                elif " leftside=" in prop:
                    cab.left_side = float(prop.split("=")[1])
                elif " bottomreveal=" in prop:
                    cab.bottom_reveal = float(prop.split("=")[1])
                elif " topreveal=" in prop:
                    cab.top_reveal = float(prop.split("=")[1])
                elif " rightreveal=" in prop:
                    cab.right_reveal = float(prop.split("=")[1])
                elif " leftreveal=" in prop:
                    cab.left_reveal = float(prop.split("=")[1])
                elif " unit=" in prop:
                    cab.unit_number = int(float(prop.split("=")[1]))
                elif " qty=" in prop:
                    cab.quantity = int(float(prop.split("=")[1]))
                elif " fl=" in prop:
                    cab.finished_left = int(float(prop.split("=")[1]))
                elif " fr=" in prop:
                    cab.finished_right = int(float(prop.split("=")[1]))
                elif " h=" in prop:
                    cab.height = float(prop.split("=")[1])
                elif " d=" in prop:
                    cab.depth = float(prop.split("=")[1])
                elif " w=" in prop:
                    cab.width = float(prop.split("=")[1])
                elif " kick=" in prop:
                    cab.kick_height = float(prop.split("=")[1])
                elif " z=" in prop:
                    cab.ztype = prop.split("=")[1]
            print(cab)
            cabs.append(cab)
    return cabs


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
        self.unit_number = 0
        self.cab_name = 0
        self.quantity = 0
        self.height = 0
        self.width = 0
        self.depth = 0
        self.bottom_reveal = 0
        self.left_reveal = 0
        self.right_reveal = 0
        self.top_reveal = 0
        self.door_gap = 0
        self.drawer_gap = 0
        self.doors = []
        self.drawers = []
        self.left_side_depth = 0
        self.right_side_depth = 0
        self.kick_height = 0
        self.kick_depth = 2.5
        self.adjustable_shelves = 0
        self.finished_left = 0
        self.finished_right = 0
        self.openings = []
        
    def __str__(self):
        return str("CABINET\n"+
            "ztype: " + str(self.ztype) + " " +
            "unit_number: " + str(self.unit_number) + " " +
            "cab_name: " + str(self.cab_name) + " " +
            "quantity: " + str(self.quantity) + " " +
            "height: " + str(self.height) + " " +
            "width: " + str(self.width) + " " +
            "depth: " + str(self.depth) + " " +
            "bottom_reveal: " + str(self.bottom_reveal) + " " +
            "left_reveal: " + str(self.left_reveal) + " " +
            "right_reveal: " + str(self.right_reveal) + " " +
            "top_reveal: " + str(self.top_reveal) + " " +
            "door_gap: " + str(self.door_gap) + " " +
            "drawer_gap: " + str(self.drawer_gap) + " " +
            "doors: " + str(self.doors) + " " +
            "drawers: " + str(self.drawers) + " " +
            "left_side_depth: " + str(self.left_side_depth) + " " +
            "right_side_depth: " + str(self.right_side_depth) + " " +
            "kick_height: " + str(self.kick_height) + " " +
            "kick_depth: " + str(self.kick_depth) + " " +
            "adjustable_shelves: " + str(self.adjustable_shelves) + " " +
            "finished_left: " + str(self.finished_left) + " " +
            "finished_right: " + str(self.finished_right) + " " +
            "openings: " + str(self.openings) + " " 
            )
        
        
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
        
        
        
        
        
        
