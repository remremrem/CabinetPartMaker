#coordinates.py
from geometry import Point as P3

cabinet = P3(1,1,1)
System1 = cabinet
c = cabinet
front_facing = cabinet
top_facing = P3(-c.x, c.z, c.y)
bottom_facing = P3(c.x, c.z, -c.y)

left_facing = P3(-c.y, c.z, -c.x)
lf = left_facing
left_facing_revert = P3(-lf.z, -lf.x, lf.y)

right_facing = P3(c.y, c.z, c.x)
back_facing = P3(-c.x, c.y, -c.z)

X = P3(1,0,0)
Y = P3(0,1,0)
Z = P3(0,0,1)


cabinet_front = P3(0,0,1)
cabinet_back = P3(0,0,-1)
cabinet_left = P3(-1,0,0)
cabinet_right = P3(1,0,0)
cabinet_top = P3(0,1,0)
cabinet_bottom = P3(0,-1,0)

def cabinetAxisToPartAxis(axis, part): #axis is a char in "xyzXYZ" or a Point. part is a Part object
    global X,Y,Z
    print("AXIS!: ", axis)
    cabinet_axis = axis
    if isinstance(axis, str):
        if axis == "x" or axis == "X":
            cabinet_axis = X
        elif axis == "y" or axis == "Y":
            cabinet_axis = Y
        elif axis == "z" or axis == "Z":
            cabinet_axis = Z
        
    part_axis = None
    if part.facing == part.LEFT:
        if cabinet_axis == X:
            part_axis = Z
        elif cabinet_axis == Y:
            part_axis = X*-1
        elif cabinet_axis == Z:
            part_axis = Y
            
    if part.facing == part.RIGHT:
        if cabinet_axis == X:
            part_axis = Z*-1
        elif cabinet_axis == Y:
            part_axis = X
        elif cabinet_axis == Z:
            part_axis = Y
            
    elif part.facing == part.TOP:
        if cabinet_axis == X:
            part_axis = X*-1
        elif cabinet_axis == Y:
            part_axis = Z
        elif cabinet_axis == Z:
            part_axis = Y
            
    elif part.facing == part.BOTTOM:
        if cabinet_axis == X:
            part_axis = X
        elif cabinet_axis == Y:
            part_axis = Z*-1
        elif cabinet_axis == Z:
            part_axis = Y
            
    elif part.facing == part.BACK:
        if cabinet_axis == X:
            part_axis = X*-1
        elif cabinet_axis == Y:
            part_axis = Y
        elif cabinet_axis == Z:
            part_axis = Z*-1
            
    elif part.facing == part.FRONT:
        part_axis = cabinet_axis
    return part_axis
           


def partToCab(part, coords):
    def changeCoordSys(part, c):
        new_position = P3(0,0,0)
        if part_sys == P3(-1,0,0): #left facing
            new_position.x = part.size.z - c.z
            new_position.y = part.size.x - c.x
            new_position.z = c.y

        elif part_sys == P3(1,0,0): #right facing
            new_position.x = c.z
            new_position.y = c.x
            new_position.z = c.yleft_thickness
            
        elif part_sys == P3(0,0,-1): #rear facing
            new_position.x = part.size.x - c.x
            new_position.y = c.y
            new_position.z = part.size.z - c.z
            
        elif part_sys == P3(0,0,1): #front facing
            new_position = c
            
        elif part_sys == P3(0,-1,0): #bottom facing
            new_position.x = c.x
            new_position.y = part.size.z - c.z
            new_position.z = c.y
            
        elif part_sys == P3(0,1,0): #top facing
            new_position.x = part.size.x - c.x
            new_position.y = c.z
            new_position.z = c.y
        return new_position
    
    new_position = changeCoordSys(part, coords)
    cabinet_coordinates = part.origin + new_position
    return cabinet_coordinates
        

def cabToPart(part, coords):
    if not coords or not part.origin:
        return None
    c = coords - part.origin
    def changeCoordSys(part, c):
        ps = partSizeToCabinet(part)
        
        new_position = P3(0,0,0)
        if part.facing == part.LEFT: #left facing
            new_position.x = ps.y + c.y
            new_position.y = c.z
            new_position.z = -c.x
            
        elif part.facing == part.RIGHT: #right facing
            new_position.x = c.y
            new_position.y = c.z
            new_position.z = c.x
            
        elif part.facing == part.BACK: #rear facing
            new_position.x = ps.x - c.x
            new_position.y = c.y
            new_position.z = ps.z - c.z
            
        elif part.facing == part.FRONT: #front facing
            new_position = c
            
        elif part.facing == part.BOTTOM: #bottom facing
            new_position.x = c.x
            new_position.y = c.z
            new_position.z = -c.y
            
        elif part.facing == part.TOP: #top facing
            new_position.x = ps.x - c.x
            new_position.y = c.z
            new_position.z = c.y
        return new_position
    
    
    new_position = changeCoordSys(part, c)
    print("CAB TO PART: ", coords, c, new_position)
    return new_position
    

def partSizeToCabinet(part):
    if part.facing == part.FRONT:
        size_in_cab_coords = P3(part.size.x, part.size.y, part.size.z)
    elif part.facing == part.BACK: 
        size_in_cab_coords = P3(part.size.x, part.size.y, part.size.z)
    elif part.facing == part.LEFT: 
        size_in_cab_coords = P3(part.size.z, part.size.x, part.size.y)
    elif part.facing == part.RIGHT:
        size_in_cab_coords = P3(part.size.z, part.size.x, part.size.y)
    elif part.facing == part.TOP:
        size_in_cab_coords = P3(part.size.x, part.size.z, part.size.y)
    elif part.facing == part.BOTTOM:
        size_in_cab_coords = P3(part.size.x, part.size.z, part.size.y)
    return size_in_cab_coords
