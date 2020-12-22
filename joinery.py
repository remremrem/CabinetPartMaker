# joinery.py
from geometry import Point as P3
from geometry import Point
import job_settings as JS
import coordinates, operation, cabinet

def ScrewJoint(male=None, female=None, origin=None, limit=None, mo=None):
    joint = Joint("butt_screw", male, female)
    joint.origin = origin
    joint.limit = limit
    joint.male_offset = mo
    male.joints.append(joint)
    female.joints.append(joint)
    pilot_holes = []
    minimum_joint_length = JS.pilot_min_distance_from_edge*2
    minimum_standard_joint_length = JS.pilot_distance_from_edge*2 + JS.pilot_min_spacing
    length = joint.length
    if length < minimum_joint_length:
        return joint
    if length < minimum_standard_joint_length:
        pattern_length = length - JS.pilot_min_distance_from_edge*2
        if pattern_length < JS.pilot_min_distance_from_edge*2 + JS.pilot_min_spacing:
            pilot_holes.append(JS.pilot_min_distance_from_edge + pattern_length*.5)
        else:
            num_holes = int(pattern_length / JS.pilot_min_spacing)
            spacing = float(pattern_length) / (num_holes - 1)
            location = JS.pilot_min_distance_from_edge
            while num_holes > 0:
                pilot_holes.append(location)
                location += spacing
                num_holes -= 1
    else:
        pattern_length = length - JS.pilot_distance_from_edge*2
        if pattern_length < JS.pilot_distance_from_edge*2 + JS.pilot_min_spacing:
            pilot_holes.append(JS.pilot_distance_from_edge + pattern_length*.5)
        else:
            num_holes = int(pattern_length / JS.pilot_max_spacing) + 2
            spacing = float(pattern_length) / (num_holes - 1)
            location = JS.pilot_distance_from_edge
            while num_holes > 0:
                pilot_holes.append(location)
                location += spacing
                num_holes -= 1
    if len(pilot_holes) > 0:
        start_point = (joint.origin + (joint.width_axis * (joint.width * .5)))
        for hole in pilot_holes:
            pc = start_point + (joint.length_axis * hole)
            o = coordinates.cabToPart(joint.female, pc)
            joint.female.addOperation(operation.PilotHole(origin=Point(o.x, o.y)))
            
    return joint

def DowelJoint(male=None, female=None, mp="trf", fp="r", mo=None):
    joint = Joint("butt_dowel", male, female)
    joint.fasteners = 10
    joint.male_position = mp
    joint.female_position = fp
    joint.male_offset = mo
    male.joints.append(joint)
    female.joints.append(joint)
    return joint

def Rabbet(male=None, female=None, mp="trf", fp="r", mo=None):
    joint = Joint("rabbet", male, female)
    joint.tenon_depth = 0
    joint.tenon_thickness = male.material.thickness
    joint.tenon_length = 0
    joint.depth_margin = .015
    joint.thickness_margin = .015
    joint.length_margin = .015
    joint.fasteners = 6
    joint.male_position = mp
    joint.female_position = fp
    joint.male_offset = mo
    male.joints.append(joint)
    female.joints.append(joint)
    return joint

def HalfBlindRabbet(male=None, female=None, mp="trf", fp="r", mo=None):
    joint = Joint("half_blind_rabbet", male, female)
    joint.tenon_depth = 0
    joint.tenon_thickness = male.material.thickness
    joint.tenon_length = 0
    joint.depth_margin = .015
    joint.thickness_margin = .015
    joint.length_margin = .015
    joint.fasteners = 6
    joint.blind_reveal = 1
    joint.male_position = mp
    joint.female_position = fp
    joint.male_offset = mo
    male.joints.append(joint)
    female.joints.append(joint)
    return joint

def BackDado(male=None, female=None, origin=None, limit=None, mo=None, inset=0, tf="inside"):
    joint = Joint("back_dado", male, female)
    joint.tenon_thickness = male.material.thickness
    joint.depth_margin = .015
    joint.thickness_margin = .015
    joint.length_margin = .02
    joint.fasteners = 2
    joint.origin = origin
    joint.limit = limit
    joint.tenon_depth = JS.back_slot_depth
    joint.tenon_length = joint.length + ((JS.back_slot_depth * 2) - joint.length_margin)
    joint.male_offset = mo
    joint.inset = inset
    joint.tab_face = tf
    print("facing: ", female.FACING_ENUMS[female.facing], joint.tenon_depth, joint.limit)
    joint.mortis_limit = joint.limit + (joint.length_axis * joint.length_margin)
    joint.mortis_origin = joint.origin - (joint.length_axis * joint.length_margin)
    if female.part_name in ["RightSide", "LeftSide"]:
        joint.mortis_origin = joint.origin - (joint.length_axis * (joint.tenon_depth+joint.length_margin))
        joint.mortis_limit = joint.limit + (joint.length_axis * (joint.tenon_depth+joint.length_margin))
        if isinstance(female.cabinet, cabinet.BaseCabinet) or isinstance(female.cabinet, cabinet.BaseCorner):
            if joint.limit.y >= (female.cabinet.height - female.thickness*1.5):
                joint.mortis_limit = P3(joint.mortis_limit.x, female.cabinet.height, joint.mortis_limit.z)
    male.joints.append(joint)
    female.joints.append(joint)
    print("MORTIS ORIGIN LIMIT: ", joint.mortis_origin, joint.mortis_limit)
    female.addOperation(operation.BackSlot(origin=coordinates.cabToPart(female, joint.mortis_origin), limit=coordinates.cabToPart(female, joint.mortis_limit)))        
    return joint

def Dado(male=None, female=None, origin=None, limit=None, mo=None, inset=0, tf="inside"):
    joint = Joint("dado", male, female)
    joint.tenon_depth = 0
    joint.tenon_thickness = male.material.thickness
    joint.tenon_length = 0
    joint.depth_margin = .015
    joint.thickness_margin = .015
    joint.length_margin = .015
    joint.fasteners = 2
    joint.origin = origin
    joint.limit = limit
    joint.male_offset = mo
    joint.inset = inset
    joint.tab_face = tf
    male.joints.append(joint)
    female.joints.append(joint)
    return joint

def BlindDado(male=None, female=None, mp="trf", fp="r", mo=None, inset=0, tf="inside"):
    joint = Joint("blind_dado", male, female)
    joint.tenon_depth = 0
    joint.tenon_thickness = male.material.thickness
    joint.tenon_length = 0
    joint.depth_margin = .015
    joint.thickness_margin = .015
    joint.length_margin = .015
    joint.fasteners = 2
    joint.blind_reveal = 1
    joint.male_position = mp
    joint.female_position = fp
    joint.male_offset = mo
    joint.inset = inset
    joint.tab_face = tf
    male.joints.append(joint)
    female.joints.append(joint)
    return joint


class Joint:
    #FASTENER TYPE ENUMS
    NONE = 0
    SCREWS = 1
    GLUE = 2
    PINNAILS = 4
    DOWELS = 8
    
    #male = male Part object, female = female Part object 
    #origin = closest point to cabinet origin in the cross-section of where the female and male parts intersect
    #limit = farthest point from cabinet origin in the cross-section of where the female and male parts intersect
    def __init__(self, joint_name="butt", male=None, female=None, origin=None, limit=None, inset=0, tf="inside"):
        self.tenon_depth = 0
        self.tenon_thickness = 0
        self.tenon_length = 0
        self.depth_margin = 0 # how shallow is the tenon compared to the mortis
        self.thickness_margin = 0 # how much thinner is the tenon compared to the mortis
        self.length_margin = 0 # how much narrower is the tenon compared to the mortis
        self.blind_reveal = 0 # how far from the edge of the part to the start of the joint on blind/half-blind joints
        self.inset = inset # how far inset to the center of a dado or slot
        self.tab_face = tf # if the male part needs a tab is the tab on the inside or outside of the part
        self.fasteners = 5
        self.male = male # which cabinet part is the "male" member of this joint
        #self.male_position = mp # where the male part is positioned on the female part
        self.male_offset = None # geometry.Point() offset for adjusting the male piece in relation to the female
        self.female = female # which cabinet part is the "female" member of this joint
        #self.female_position = fp # where the female part is positioned on the male part
        self.origin = origin
        self.limit = limit
        self.mortis_origin = origin
        self.mortis_limit = limit
        self.tenon_origin = origin
        self.tenon_limit = limit
        self.joint_name = joint_name
        self.operations = [] # a list of operations that make this joint
        
    @property
    def width(self):
        if self.origin and self.limit:
            return sorted((self.limit - self.origin).values)[1][0]
        else: return None
        
    @property
    def width_axis(self): #axis of the width (thickness) of this joint on the cabinet
        if self.origin and self.limit:
            wa = sorted((self.limit - self.origin).values)[1][1]
            if wa == "x":
                return coordinates.X
            elif wa == "y":
                return coordinates.Y
            elif wa == "z":
                return coordinates.Z
        else: return None
    
    @property
    def width_axis_male(self):
        return coordinates.cabinetAxisToPartAxis(self.width_axis(), self.male)
    
    @property
    def width_axis_female(self):
        return coordinates.cabinetAxisToPartAxis(self.width_axis(), self.female)
        
    @property
    def length(self):
        if self.origin and self.limit:
            return sorted((self.limit - self.origin).values)[2][0]
        else: return None
        
    @property
    def length_axis(self): #axis of the length of this joint on the cabinet
        if self.origin and self.limit:
            wa = sorted((self.limit - self.origin).values)[2][1]
            if wa == "x":
                return coordinates.X
            elif wa == "y":
                return coordinates.Y
            elif wa == "z":
                return coordinates.Z
        else: return None
    
    @property
    def length_axis_male(self):
        return coordinates.cabinetAxisToPartAxis(self.length_axis, self.male)
    
    @property
    def length_axis_female(self):
        return coordinates.cabinetAxisToPartAxis(self.length_axis, self.female)
        
    @property
    def depth_axis(self): #axis of the depth of this joint on the cabinet
        print("O L: ", self.origin, self.limit)
        if self.origin and self.limit:
            wa = sorted((self.limit - self.origin).values)[0][1]
            print("WA: ", wa)
            if wa == "x":
                return coordinates.X
            elif wa == "y":
                return coordinates.Y
            elif wa == "z":
                return coordinates.Z
        else: return None
    
    @property
    def depth_axis_male(self):
        return coordinates.cabinetAxisToPartAxis(self.depth_axis, self.male)
    
    @property
    def depth_axis_female(self):
        return coordinates.cabinetAxisToPartAxis(self.depth_axis, self.female)
        
    @property
    def center(self):
        return self.origin + ((self.limit - self.origin) * .5)
        

    def list_fasteners():
        fl = []
        f = self.fasteners
        if f >= 8:
            fl.append("dowels")
            f -= 8
        if f >= 4:
            fl.append("pinnails")
            f -= 4
        if f >= 2:
            fl.append("glue")
            f -= 2
        if f >= 1:
            fl.append("screws")
            f -= 1
            
    
    def __str__(self):
        s = "Joint(name: {0}, origin: {1}, limit: {2}, center: {7}, width: {3}, length: {4}, \n         male: {5}, female: {6}, length_axis: {8}, length_axis_male: {9}, length_axis_female: {10})"
        return s.format(self.joint_name, self.origin, self.limit, self.width, self.length, self.male.part_name, self.female.part_name, self.center, self.length_axis, self.length_axis_male, self.length_axis_female)

