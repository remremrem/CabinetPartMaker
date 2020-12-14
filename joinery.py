# joinery.py
from geometry import Point3 as P3

def ScrewJoint(male=None, female=None, origin=None, limit=None, mo=None):
    joint = Joint("butt_screw", male, female)
    joint.origin = origin
    joint.limit = limit
    joint.male_offset = mo
    male.joints.append(joint)
    female.joints.append(joint)
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
    joint.tenon_width = 0
    joint.depth_margin = .015
    joint.thickness_margin = .015
    joint.width_margin = .015
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
    joint.tenon_width = 0
    joint.depth_margin = .015
    joint.thickness_margin = .015
    joint.width_margin = .015
    joint.fasteners = 6
    joint.blind_reveal = 1
    joint.male_position = mp
    joint.female_position = fp
    joint.male_offset = mo
    male.joints.append(joint)
    female.joints.append(joint)
    return joint

def Dado(male=None, female=None, origin=None, limit=None, mo=None, inset=0, tf="inside"):
    joint = Joint("dado", male, female)
    joint.tenon_depth = 0
    joint.tenon_thickness = male.material.thickness
    joint.tenon_width = 0
    joint.depth_margin = .015
    joint.thickness_margin = .015
    joint.width_margin = .015
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
    joint.tenon_width = 0
    joint.depth_margin = .015
    joint.thickness_margin = .015
    joint.width_margin = .015
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
    
    def __init__(self, joint_name="butt", male=None, female=None, origin=None, limit=None, inset=0, tf="inside"):
        self.tenon_depth = 0
        self.tenon_thickness = 0
        self.tenon_width = 0
        self.depth_margin = 0 # how shallow is the tenon compared to the mortis
        self.thickness_margin = 0 # how much thinner is the tenon compared to the mortis
        self.width_margin = 0 # how much narrower is the tenon compared to the mortis
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
        self.joint_name = joint_name
        
    @property
    def width(self):
        if self.origin and self.limit:
            return sorted((self.limit - self.origin).values)[1]
        else: return None
        
    @property
    def length(self):
        if self.origin and self.limit:
            return sorted((self.limit - self.origin).values)[2]
        else: return None
        
        
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
        return "Joint(name: {0}, origin: {1}, limit: {2}, width: {3}, length: {4}, male: {5}, female: {6})".format(self.joint_name, self.origin, self.limit, self.width, self.length, self.male.part_name, self.female.part_name)

