# joinery.py

import operations
import job_settings

drawer_rabbet_depth = .125

drawer_bottom_inset = '10mm'

drawer_bottom_slot_width = .25

back_rabbet_depth = .125

back_inset = .375

spanner_rabbet_depth = .125

dowel_hole = operation.Drill(diameter='8mm', depth=.57)
euro_hole = operation.Drill(diameter='5mm', depth=.57)
pilot_hole = operation.Drill(diameter='4mm', depth=job_settings.material_thickness)



ScrewJoint = screw_func()
DowelJoint = dowel_func()
Rabbet = rabbet_func()
Dado = dado_func()


def screw_func():
    joint = Joint("butt_screw")
    return joint

def dowel_func():
    joint = Joint("butt_dowel")
    joint.fasteners = 8
    return joint

def rabbet_func():
    joint = Joint("rabbet")
    joint.tenon_depth = 0
    joint.tenon_thickness = 0
    joint.tenon_width = 0
    joint.depth_margin = .015
    joint.thickness_margin = .015
    joint.width_margin = .015
    joint.fasteners = 6
    return joint

def dado_func():
    joint = Joint("dado")
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
    
    def __init__(self, joint_name="butt"):
        self.tenon_depth = 0
        self.tenon_thickness = 0
        self.tenon_width = 0
        self.depth_margin = 0
        self.thickness_margin = 0
        self.width_margin = 0
        self.fasteners = 5
        
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

