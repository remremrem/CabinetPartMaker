# joinery.py

import operations
import job_settings


def ScrewJoint(male=None, female=None):
    joint = Joint("butt_screw", male, female)
    return joint

def DowelJoint(male=None, female=None):
    joint = Joint("butt_dowel", male, female)
    joint.fasteners = 10
    return joint

def Rabbet(male=None, female=None):
    joint = Joint("rabbet", male, female)
    joint.tenon_depth = 0
    joint.tenon_thickness = male.material.thickness
    joint.tenon_width = 0
    joint.depth_margin = .015
    joint.thickness_margin = .015
    joint.width_margin = .015
    joint.fasteners = 6
    return joint

def Dado(male=None, female=None):
    joint = Joint("dado", male, female)
    joint.tenon_depth = 0
    joint.tenon_thickness = 0
    joint.tenon_width = 0
    joint.depth_margin = .015
    joint.thickness_margin = .015
    joint.width_margin = .015
    joint.fasteners = 2
    return joint


class Joint:
    #FASTENER TYPE ENUMS
    NONE = 0
    SCREWS = 1
    GLUE = 2
    PINNAILS = 4
    DOWELS = 8
    
    def __init__(self, joint_name="butt", male=None, female=None):
        self.tenon_depth = 0
        self.tenon_thickness = 0
        self.tenon_width = 0
        self.depth_margin = 0
        self.thickness_margin = 0
        self.width_margin = 0
        self.fasteners = 5
        self.male = male
        self.male_position = "right"
        self.female = female
        self.female_position = "inside top"
        
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

