# joinery.py

import operation
import job_settings


def ScrewJoint(male=None, female=None, mp="trf", fp="r", mo=None):
    joint = Joint("butt_screw", male, female)
    joint.female_position = mp
    joint.female_position = fp
    joint.male_offset = mo
    male.joints.append(joint)
    female.joints.append(joint)
    return joint

def DowelJoint(male=None, female=None, mp="trf", fp="r", mo=None):
    joint = Joint("butt_dowel", male, female)
    joint.fasteners = 10
    joint.female_position = mp
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
    joint.female_position = mp
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
    joint.female_position = mp
    joint.female_position = fp
    joint.male_offset = mo
    male.joints.append(joint)
    female.joints.append(joint)
    return joint

def Dado(male=None, female=None, mp="trf", fp="r", mo=None):
    joint = Joint("dado", male, female)
    joint.tenon_depth = 0
    joint.tenon_thickness = male.material.thickness
    joint.tenon_width = 0
    joint.depth_margin = .015
    joint.thickness_margin = .015
    joint.width_margin = .015
    joint.fasteners = 2
    joint.female_position = mp
    joint.female_position = fp
    joint.male_offset = mo
    male.joints.append(joint)
    female.joints.append(joint)
    return joint

def BlindDado(male=None, female=None, mp="trf", fp="r", mo=None):
    joint = Joint("blind_dado", male, female)
    joint.tenon_depth = 0
    joint.tenon_thickness = male.material.thickness
    joint.tenon_width = 0
    joint.depth_margin = .015
    joint.thickness_margin = .015
    joint.width_margin = .015
    joint.fasteners = 2
    joint.blind_reveal = 1
    joint.female_position = mp
    joint.female_position = fp
    joint.male_offset = mo
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
    
    def __init__(self, joint_name="butt", male=None, female=None, mp="trf", fp="r"):
        self.tenon_depth = 0
        self.tenon_thickness = 0
        self.tenon_width = 0
        self.depth_margin = 0 # how shallow is the tenon compared to the mortis
        self.thickness_margin = 0 # how much thinner is the tenon compared to the mortis
        self.width_margin = 0 # how much narrower is the tenon compared to the mortis
        self.blind_reveal = 0 # how far from the edge of the part to the start of the joint on blind/half-blind joints
        self.fasteners = 5
        self.male = male # which cabinet part is the "male" member of this joint
        self.male_position = mp # where the male part is positioned on the female part
        self.male_offset = None # geometry.Point() offset for adjusting the male piece in relation to the female
        self.female = female # which cabinet part is the "female" member of this joint
        self.female_position = fp # where the female part is positioned on the male part
        
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

