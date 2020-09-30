# import_kcd.py

import cabinet
import geometry
from cabinet import Cell
import fnmatch


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
                elif " drawergap=" in prop:
                    cab.drawer_gap = float(prop.split("=")[1])
                elif " rightside=" in prop:
                    cab.right_side_depth = float(prop.split("=")[1])
                elif " leftside=" in prop:
                    cab.left_side_depth = float(prop.split("=")[1])
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
                    cab.ztype = prop.split("=")[1].strip()
            cabs.append(cab)
        elif "record=face" in line:
            face = KCD_Face()
            for prop in line.split(","):
                print("FACEPROP: ", prop)
                if fnmatch.fnmatch(prop, " d*z=*"):
                    face.elevation = float(prop.split("=")[1])
                    face.face_id = int(prop.split("d")[1].split("z")[0])
                elif fnmatch.fnmatch(prop, " d*h=*"):
                    face.height = float(prop.split("=")[1])
                elif fnmatch.fnmatch(prop, " d*w=*"):
                    face.width = float(prop.split("=")[1])
                elif fnmatch.fnmatch(prop, " d*ld=*"): #check for left swing door
                    if float(prop.split("=")[1]) > 0:
                        face.action += 1
                        face.face_type = 1
                elif fnmatch.fnmatch(prop, " d*rd=*"): #check for right swing door
                    if float(prop.split("=")[1]) > 0:
                        face.action += 2
                        face.face_type = 1
                elif fnmatch.fnmatch(prop, " d*dr=*"): #check if drawer
                    if float(prop.split("=")[1]) > 0:
                        face.action = 5
                        face.face_type = 2
            cab.faces[face.face_id] = face
    return cabs


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
        self.door_gap = .125
        self.drawer_gap = .125
        self.doors = []
        self.drawers = []
        self.left_side_depth = 0
        self.right_side_depth = 0
        self.kick_height = 0
        self.kick_depth = 2.5
        self.adjustable_shelves = 0
        self.finished_left = 0
        self.finished_right = 0
        self.faces = {}
        
    def __str__(self):
        faces = ""
        for each in self.faces.values(): 
            faces += each.__str__()+"\n"
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
            "\nfaces:\n" + faces + " " 
            )
        
        
class KCD_Face:
    #FACE TYPE ENUMS
    OPEN = 0
    DOOR = 1
    DRAWER = 2
    FALSE = 3
    
    #DOOR SWING (ACTION) ENUMS
    FIXED = 0
    SWING_LEFT = 1
    SWING_RIGHT = 2
    SWING_PAIR = 3
    SWING_UP = 4
    SWING_DOWN = 5
    PULLOUT = 6
    TIPOUT = 7
    
    def __init__(self, face_id=1):
        self.elevation = 0
        self.height = 0
        self.width = 0
        self.face_type = KCD_Face.OPEN
        self.action = KCD_Face.FIXED
        self.face_id = face_id
        
    def __str__(self):
        return str("FACE "+
            "face id: " + str(self.face_id) + " " +
            "height: " + str(self.height) + " " +
            "width: " + str(self.width) + " " +
            "face_type: " + str(self.face_type) + " " +
            "elevation: " + str(self.elevation) + " " +
            "action: " + str(self.action) + " "
            )

def convertFace(kface):
    face = cabinet.Face()
    face.elevation = kface.elevation
    face.height = kface.height
    face.width = kface.width
    

def convertCabinet(kcab, newcab):
    newcab.top_reveal = kcab.top_reveal
    newcab.bottom_reveal =  kcab.bottom_reveal
    newcab.left_reveal = kcab.left_reveal
    newcab.right_reveal = kcab.right_reveal
    newcab.door_gap = kcab.door_gap
    newcab.drawer_gap = kcab.drawer_gap
    newcab.finished_left = kcab.finished_left
    newcab.finished_right = kcab.finished_right
    newcab.adjustable_shelves = kcab.adjustable_shelves
    
def convertCorner(kcab, newcab):
    newcab.left_side_depth = kcab.left_side_depth
    newcab.right_side_depth = kcab.right_side_depth
    
    if "kcabtype is left corner":
        newcab.left_width = kcab.depth
        newcab.right_width = kcab.width
    else:
        newcab.left_width = kcab.width
        newcab.right_width = kcab.depth
    
    
def convertBaseCab(kcab, cabname="Base Cabinet", iscorner=False):
    if iscorner:
        newcab = cabinet.BaseCorner(kcab.height, kcab.depth, kcab.width, kcab.unit_number, kcab.quantity)
        convertCorner(kcab, newcab)
    else: newcab = cabinet.BaseCabinet(kcab.height, kcab.depth, kcab.width, kcab.unit_number, kcab.quantity)
    convertCabinet(kcab, newcab)
    newcab.kick_depth = kcab.kick_depth
    newcab.kick_height = kcab.kick_height
    return newcab
    
def convertTallCab(kcab, cabname="Tall Cabinet", iscorner=False):
    if iscorner:
        newcab = cabinet.TallCorner(kcab.height, kcab.depth, kcab.width, kcab.unit_number, kcab.quantity)
        convertCorner(kcab, newcab)
    else: newcab = cabinet.TallCabinet(kcab.height, kcab.depth, kcab.width, kcab.unit_number, kcab.quantity)
    convertCabinet(kcab, newcab)
    newcab.kick_depth = kcab.kick_depth
    newcab.kick_height = kcab.kick_height
    return newcab
    
def convertWallCab(kcab, cabname="Wall Cabinet", iscorner=False):
    if iscorner:
        newcab = cabinet.WallCorner(kcab.height, kcab.depth, kcab.width, kcab.unit_number, kcab.quantity)
        convertCorner(kcab, newcab)
    else: newcab = cabinet.WallCabinet(kcab.height, kcab.depth, kcab.width, kcab.unit_number, kcab.quantity)
    convertCabinet(kcab, newcab)
    return newcab
    
    
        

def convert(kcab):
    newcab = None
    print("CONVERT: ", kcab.ztype)
    if kcab.ztype == "101":
        newcab = convertWallCab(kcab, "Wall Cabinet", False)
        
        root_cell = Cell(celltype='COLUMN',action=None,divider=None,region="TBLR",size=geometry.Point(kcab.width, kcab.height) )
        print(kcab.faces)
        f = convertFace(kcab.faces[1])
        root_cell.addCell(Cell(celltype='DOOR',action=None,divider=None,region="TBLR",face=f, size=geometry.Point(kcab.width, kcab.height) ))
        
        newcab.root_cell = root_cell
        #print("CELLS AS LIST: ", newcab.root_cell.asList())
        print("CELLS AS LIST: ", newcab.root_cell)
        print("CELL TREE: \n" + newcab.root_cell.printTree())
        
    if kcab.ztype.lower() == "243v3":
        newcab = convertBaseCab(kcab, "Offset Vanity 3drw left", False)
        
        s = geometry.Point(kcab.width, kcab.height-kcab.kick_height)
        root_cell = Cell(celltype='COLUMN',action=None,divider=None,region="TBLR",size=s )
        
        s = geometry.Point(s.x, kcab.faces[5].height+kcab.drawer_gap+kcab.bottom_reveal)
        root_cell.addCell(Cell(celltype='ROW',action=None,divider=cabinet.CellDivider(t=.75, q=2),region='BLR', size=s ))
        
        s = geometry.Point(kcab.faces[2].width+kcab.door_gap*.5+kcab.left_reveal, s.y)
        root_cell[0].addCell(Cell(celltype='COLUMN',action=None,divider=None,region='BL', size=s ))
        root_cell[0][0].addCell(Cell(celltype='DRAWER',action="PULLOUT",divider=None,region='BL',face=convertFace(kcab.faces[4]), size=geometry.Point(s.x, kcab.faces[2].height+kcab.drawer_gap*.5) ))
        root_cell[0][0].addCell(Cell(celltype='DRAWER',action="PULLOUT",divider=None,region='L',face=convertFace(kcab.faces[2]), size=geometry.Point(s.x, kcab.faces[2].height+kcab.drawer_gap) ))
        root_cell[0][0].addCell(Cell(celltype='DRAWER',action="PULLOUT",divider=None,region='L',face=convertFace(kcab.faces[3]), size=geometry.Point(s.x, kcab.faces[2].height+kcab.drawer_gap) ))
        
        s = geometry.Point(kcab.width-s.x, s.y)
        root_cell[0].addCell(Cell(celltype='DOOR',action=None,divider=None,region="BR",face=convertFace(kcab.faces[5]), size=s ))
        
        
        s = geometry.Point(kcab.width, kcab.height-s.y)
        root_cell.addCell(Cell(celltype='FALSE',action=None,divider=None,region='TLR',face=convertFace(kcab.faces[1]), size=s ))
        
        
        
        newcab.root_cell = root_cell
        #print("CELLS AS LIST: ", newcab.root_cell.asList())
        #print("CELLS AS LIST: ", newcab.root_cell)
        print("CELL TREE: \n" + newcab.root_cell.printTree())
        
        
    return newcab
        
        
        
