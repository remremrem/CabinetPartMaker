# import_kcd.py

CSV = "jobfile.job"

def parseCSV():
    file = open(CSV, "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        
        
        
        
        
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
        
        
        
        
        
        
