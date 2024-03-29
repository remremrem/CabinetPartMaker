# import_kcd.py

import cabinet, parts, geometry, coordinates
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

def convertFace(kface, kcab):
    face = cabinet.Face()
    face.elevation = kface.elevation
    if kface.action == KCD_Face.SWING_PAIR:
        face.width = kface.width*2
    else:
        face.width = kface.width
    face.height = kface.height
    face.action = kface.action
    print("NEW FACE: ", face)
    return face
    

def convertCabinet(kcab, newcab):
    print("CONVERT: ", newcab.cab_name)
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
        newcab = cabinet.BaseCorner(height=kcab.height, depth=kcab.depth, width=kcab.width, unit_num=kcab.unit_number, quantity=kcab.quantity, name=cabname)
        convertCorner(kcab, newcab)
    else: newcab = cabinet.BaseCabinet(height=kcab.height, depth=kcab.depth, width=kcab.width, unit_num=kcab.unit_number, quantity=kcab.quantity, name=cabname)
    convertCabinet(kcab, newcab)
    newcab.kick_depth = kcab.kick_depth
    newcab.kick_height = kcab.kick_height
    return newcab
    
def convertTallCab(kcab, cabname="Tall Cabinet", iscorner=False):
    if iscorner:
        newcab = cabinet.TallCorner(height=kcab.height, depth=kcab.depth, width=kcab.width, unit_num=kcab.unit_number, quantity=kcab.quantity, name=cabname)
        convertCorner(kcab, newcab)
    else: newcab = cabinet.TallCabinet(height=kcab.height, depth=kcab.depth, width=kcab.width, unit_num=kcab.unit_number, quantity=kcab.quantity, name=cabname)
    convertCabinet(kcab, newcab)
    newcab.kick_depth = kcab.kick_depth
    newcab.kick_height = kcab.kick_height
    return newcab
    
def convertWallCab(kcab, cabname="Wall Cabinet", iscorner=False):
    if iscorner:
        newcab = cabinet.WallCorner(height=kcab.height, depth=kcab.depth, width=kcab.width, unit_num=kcab.unit_number, quantity=kcab.quantity, name=cabname)
        convertCorner(kcab, newcab)
    else: newcab = cabinet.WallCabinet(height=kcab.height, depth=kcab.depth, width=kcab.width, unit_num=kcab.unit_number, quantity=kcab.quantity, name=cabname)
    convertCabinet(kcab, newcab)
    return newcab
    
    
        
"""def finalize(newcab, rootcell):
    newcab.root_cell = rootcell
    newcab.root_cell.establishOrigin(newcab)
    print("CELL TREE: \n" + newcab.root_cell.printTree())"""
        
def convert(kcab):
    def finalize(newcab, rootcell):
        newcab.root_cell = rootcell
        newcab.root_cell.establishOrigin(newcab)
        print("CELL TREE: \n" + newcab.root_cell.printTree())
        newcab.root_cell.makeParts(newcab)
        newcab.setPartOrigins()
        print("CABINET PARTS: ")
        for each in newcab.parts:
            print("name: ", each.part_name, "origin: ", each.origin, "part_size:", each.size, "cabinet_size: ", coordinates.partSizeToCabinet(each))
            for op in each.operations:
                print(op)
            each.jointsInPartCoords()
        for each in newcab.faces:
            print(each)
    
    newcab = None
    if kcab.ztype == "101":
        newcab = convertWallCab(kcab, "Wall Cabinet", False)
        
        root_cell = Cell(celltype=Cell.COLUMN,action=None,dividers=None,region="TBLR",size=geometry.Point(kcab.width, kcab.height) )
        f = convertFace(kcab.faces[1], kcab)
        root_cell.addCell(Cell(celltype=Cell.DOOR,action=f.action,dividers=None,region="TBLR",face=f, size=geometry.Point(kcab.width, kcab.height) ))
        
        finalize(newcab, root_cell)
        
        
    elif kcab.ztype == "201":
        newcab = convertBaseCab(kcab, "Base Cabinet", False)
        
        s = geometry.Point(kcab.width, kcab.height-kcab.kick_height)
        root_cell = Cell(celltype=Cell.COLUMN,action=None,dividers=None,region="TBLR",size=s )
        f = convertFace(kcab.faces[1], kcab)
        if len(kcab.faces) == 1:
            cell = Cell(celltype=Cell.DOOR,action=f.action,dividers=None,region="TBLR",face=f, size=geometry.Point(kcab.width, kcab.height-kcab.kick_height) )
            root_cell.addCell(cell)
        else:
            f2 = convertFace(kcab.faces[2], kcab)
            cell = Cell(celltype=Cell.DOOR,action=f2.action,dividers=None,region="BLR",face=f2, size=geometry.Point(kcab.width, f2.height+kcab.drawer_gap*.5+kcab.bottom_reveal) )
            root_cell.addCell(cell)
            cell = Cell(celltype=Cell.DRAWER,action=f.action,dividers=None,region="TLR",face=f, size=geometry.Point(kcab.width, f.height+kcab.drawer_gap*.5+kcab.top_reveal) )
            root_cell.addCell(cell)
        
        finalize(newcab, root_cell)
        
        
    elif kcab.ztype == "202":
        newcab = convertBaseCab(kcab, "Base Cabinet 2 Opening", False)
        kcab.faces[3].action = 3
        kcab.faces[4].action = 3
        
        s = geometry.Point(kcab.width, kcab.height-kcab.kick_height)
        root_cell = Cell(celltype=Cell.ROW,action=None,dividers=parts.Shelf(),region="TBLR",size=s )
        
        s = geometry.Point(s.x*.5, s.y)
        root_cell.addCell(Cell(celltype=Cell.COLUMN,action=None,dividers=None,region='TBL', size=s ))
        f = convertFace(kcab.faces[3], kcab)
        root_cell[0].addCell(Cell(celltype=Cell.DOOR,action=f.action,dividers=None,region="BLR",face=f, size=geometry.Point(s.x, f.height+kcab.drawer_gap*.5+kcab.bottom_reveal) ))
        f = convertFace(kcab.faces[1], kcab)
        root_cell[0].addCell(Cell(celltype=Cell.DRAWER,action=f.action,dividers=None,region="TLR",face=f, size=geometry.Point(s.x, f.height+kcab.drawer_gap*.5+kcab.top_reveal) ))
        
        root_cell.addCell(Cell(celltype=Cell.COLUMN,action=None,dividers=None,region='RBL', size=s ))
        f = convertFace(kcab.faces[4], kcab)
        root_cell[1].addCell(Cell(celltype=Cell.DOOR,action=f.action,dividers=None,region="BLR",face=f, size=geometry.Point(s.x, f.height+kcab.drawer_gap*.5+kcab.bottom_reveal) ))
        f = convertFace(kcab.faces[2], kcab)
        root_cell[1].addCell(Cell(celltype=Cell.DRAWER,action=f.action,dividers=None,region="TLR",face=f, size=geometry.Point(s.x, f.height+kcab.drawer_gap*.5+kcab.top_reveal) ))

        finalize(newcab, root_cell)
        
        
    elif kcab.ztype.lower() == "202-u":
        newcab = convertBaseCab(kcab, "Base Cabinet 2 Drawer Utility", False)
        
        s = geometry.Point(kcab.width, kcab.height-kcab.kick_height)
        root_cell = Cell(celltype=Cell.COLUMN,action=None,dividers=parts.FrontSpanner(),region="TBLR",size=s )
        
        f = convertFace(kcab.faces[3], kcab)
        root_cell.addCell(Cell(celltype=Cell.DOOR,action=f.action,dividers=None,region="BLR",face=f, size=geometry.Point(s.x, f.height+kcab.drawer_gap*.5+kcab.bottom_reveal) ))
        
        f = convertFace(kcab.faces[1], kcab)
        root_cell.addCell(Cell(celltype=Cell.ROW,action=None,dividers=[parts.VerticalDivider(), parts.VerticalDivider()],region="TLR",size=geometry.Point(s.x,  f.height+kcab.drawer_gap*.5+kcab.top_reveal)  ))
        root_cell[1].addCell(Cell(celltype=Cell.DRAWER,action=f.action,dividers=None,region="BTL",face=f, size=geometry.Point(s.x*.5, f.height+kcab.drawer_gap*.5+kcab.top_reveal) ))
        f = convertFace(kcab.faces[2], kcab)
        root_cell[1].addCell(Cell(celltype=Cell.DRAWER,action=f.action,dividers=None,region="BTR",face=f, size=geometry.Point(s.x*.5, f.height+kcab.drawer_gap*.5+kcab.top_reveal) ))

        finalize(newcab, root_cell)
        
        
    elif kcab.ztype == "211":
        newcab = convertBaseCab(kcab, "Blind Base Left Corner", False)
        
        s = geometry.Point(kcab.width, kcab.height-kcab.kick_height)
        root_cell = Cell(celltype=Cell.ROW,action=None,dividers=None,region="TBLR",size=s )
        if len(kcab.faces) == 1:
            f = convertFace(kcab.faces[1], kcab)
            root_cell.addCell(Cell(celltype=Cell.BLIND,action=None,dividers=None,region="TBL",face=None, size=geometry.Point(kcab.width-(f.width+kcab.right_reveal+kcab.door_gap), kcab.height-kcab.kick_height) ))
            root_cell.addCell(Cell(celltype=Cell.DOOR,action=f.action,dividers=None,region="TBR",face=f, size=geometry.Point(f.width+kcab.right_reveal+kcab.door_gap, kcab.height-kcab.kick_height) ))
        else:
            f = convertFace(kcab.faces[2], kcab)
            root_cell.addCell(Cell(celltype=Cell.BLIND,action=None,dividers=None,region="TBL",face=None, size=geometry.Point(kcab.width-(f.width+kcab.right_reveal+kcab.door_gap), kcab.height-kcab.kick_height) ))
            root_cell.addCell(Cell(celltype=Cell.COLUMN,action=None,dividers=None,region='TBR', size=geometry.Point(f.width+kcab.right_reveal+kcab.door_gap, kcab.height-kcab.kick_height) ))
            root_cell[1].addCell(Cell(celltype=Cell.DOOR,action=f.action,dividers=None,region="BRL",face=f, size=geometry.Point(f.width+kcab.right_reveal+kcab.door_gap, f.height+kcab.drawer_gap*.5+kcab.bottom_reveal) ))
            f2 = convertFace(kcab.faces[1], kcab)
            root_cell[1].addCell(Cell(celltype=Cell.DRAWER,action=f2.action,dividers=None,region="TRL",face=f2, size=geometry.Point(f.width+kcab.right_reveal+kcab.door_gap, kcab.faces[1].height+kcab.drawer_gap*.5+kcab.top_reveal) ))
            
        
        finalize(newcab, root_cell)
        
        
    elif kcab.ztype == "221":
        newcab = convertBaseCab(kcab, "Blind Base Right Corner", False)
        
        s = geometry.Point(kcab.width, kcab.height-kcab.kick_height)
        root_cell = Cell(celltype=Cell.ROW,action=None,dividers=None,region="TBLR",size=s )
        if len(kcab.faces) == 1:
            f = convertFace(kcab.faces[1], kcab)
            cell = Cell(celltype=Cell.DOOR,action=f.action,dividers=None,region="TBL",face=f, 
                        size=geometry.Point(f.width+kcab.left_reveal+kcab.door_gap, kcab.height-kcab.kick_height) )
            root_cell.addCell(cell)
            cell = Cell(celltype=Cell.BLIND,action=None,dividers=None,region="TBR",face=None, 
                        size=geometry.Point(kcab.width-(f.width+kcab.left_reveal+kcab.door_gap), kcab.height-kcab.kick_height) )
            root_cell.addCell(cell)
        else:
            f = convertFace(kcab.faces[2], kcab)
            cell = Cell(celltype=Cell.COLUMN,action=None,dividers=None,region='TBL', 
                        size=geometry.Point(f.width+kcab.left_reveal+kcab.door_gap, kcab.height-kcab.kick_height) )
            root_cell.addCell(cell)
            cell = Cell(celltype=Cell.DOOR,action=f.action,dividers=None,region="BL",face=f, 
                        size=geometry.Point(f.width+kcab.left_reveal+kcab.door_gap, f.height+kcab.drawer_gap*.5+kcab.bottom_reveal) )
            root_cell[0].addCell(cell)
            f2 = convertFace(kcab.faces[1], kcab)
            cell = Cell(celltype=Cell.DRAWER,action=f2.action,dividers=None,region="TL",face=f2, 
                        size=geometry.Point(f.width+kcab.left_reveal+kcab.door_gap, kcab.faces[1].height+kcab.drawer_gap*.5+kcab.top_reveal) )
            root_cell[0].addCell(cell)
            cell = Cell(celltype=Cell.BLIND,action=None,dividers=None,region="TBR",face=None, 
                        size=geometry.Point(kcab.width-(f.width+kcab.left_reveal+kcab.door_gap), kcab.height-kcab.kick_height) )
            root_cell.addCell(cell)
        
        finalize(newcab, root_cell)
        
        
    elif kcab.ztype.lower() == "243v3":
        newcab = convertBaseCab(kcab, "Offset Vanity 3drw left", False)
        
        s = geometry.Point(kcab.width, kcab.height-kcab.kick_height)
        root_cell = Cell(celltype=Cell.COLUMN,action=None,dividers=None,region="TBLR",size=s )
        
        s = geometry.Point(s.x, kcab.faces[5].height+kcab.drawer_gap+kcab.bottom_reveal)
        divider1 = parts.VerticalDivider()
        divider1.facing = parts.Part.LEFT
        divider2 = parts.HingeStrip()
        divider2.facing = parts.Part.RIGHT
        root_cell.addCell(Cell(celltype=Cell.ROW,action=None,dividers=[divider1, divider2],region='BLR', size=s ))
        
        s = geometry.Point(kcab.faces[2].width+kcab.door_gap*.5+kcab.left_reveal, s.y)
        root_cell[0].addCell(Cell(celltype=Cell.COLUMN,action=None,dividers=None,region='BL', size=s ))
        root_cell[0][0].addCell(Cell(celltype=Cell.DRAWER,action="PULLOUT",dividers=None,region='BL',face=convertFace(kcab.faces[4], kcab), size=geometry.Point(s.x, kcab.faces[4].height+kcab.drawer_gap*.5) ))
        root_cell[0][0].addCell(Cell(celltype=Cell.DRAWER,action="PULLOUT",dividers=None,region='L',face=convertFace(kcab.faces[3], kcab), size=geometry.Point(s.x, kcab.faces[3].height+kcab.drawer_gap) ))
        root_cell[0][0].addCell(Cell(celltype=Cell.DRAWER,action="PULLOUT",dividers=None,region='L',face=convertFace(kcab.faces[2], kcab), size=geometry.Point(s.x, kcab.faces[2].height+kcab.drawer_gap) ))
        
        s = geometry.Point(kcab.width-s.x, s.y)
        #offset vanity double doors come fucked from kcd cause they dont account for door gap
        """if kcab.faces[5].action == KCD_Face.SWING_PAIR:
            print("SWING PAIR BITCHES!!")
            #kcd_adjust = newcab.door_gap
            #kcab.faces[5].width -= kcd_adjust"""
        root_cell[0].addCell(Cell(celltype=Cell.DOOR,action=kcab.faces[5].action,dividers=None,region="BR",face=convertFace(kcab.faces[5], kcab), size=s ))
        
        s = geometry.Point(kcab.width, kcab.height-s.y)
        root_cell.addCell(Cell(celltype=Cell.FALSE,action=None,dividers=None,region='TLR',face=convertFace(kcab.faces[1], kcab), size=s ))
        
        finalize(newcab, root_cell)
        
        
    elif kcab.ztype == "272":
        newcab = convertBaseCab(kcab, "Base Corner90 Right", False)
        
        s = geometry.Point(kcab.width, kcab.height-kcab.kick_height)
        root_cell = Cell(celltype=Cell.COLUMN,action=None,dividers=None,region="TBLR",size=s )
        f = convertFace(kcab.faces[1], kcab)
        root_cell.addCell(Cell(celltype=Cell.DOOR,action=f.action,dividers=None,region="TBLR",face=f, size=geometry.Point(kcab.width, kcab.height-kcab.kick_height) ))

        finalize(newcab, root_cell)
        
        
    elif kcab.ztype.lower() == "261-d":
        newcab = convertBaseCab(kcab, "Base Cabinet Drawer Below", False)
        
        s = geometry.Point(kcab.width, kcab.height-kcab.kick_height)
        root_cell = Cell(celltype=Cell.COLUMN,action=None,dividers=parts.Shelf(),region="TBLR",size=s )
        f = convertFace(kcab.faces[2], kcab)
        f2 = convertFace(kcab.faces[1], kcab)
        root_cell.addCell(Cell(celltype=Cell.DRAWER,action=f2.action,dividers=None,region="TBLR",face=f2, size=geometry.Point(kcab.width, f2.height+kcab.drawer_gap*.5+kcab.bottom_reveal ) ))
        root_cell.addCell(Cell(celltype=Cell.DOOR,action=f.action,dividers=None,region="TBLR",face=f, size=geometry.Point(kcab.width, f.height+kcab.drawer_gap*.5+kcab.top_reveal) ))
            
        
        finalize(newcab, root_cell)
        
        
    return newcab
        
        
        
