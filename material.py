# material.py


class Library:
    def __init__(self, species="Hickory"):
        #CORES
        self.Ply = Core()
        self.PB = Core("PB")
        self.UltraCore = Core("UltraCore")
        self.MDF = Core("MDF")
        self.Hardwood = Core("Hardwood")
        
        self.casework = Material("PrefinBirch", .7, 48, 96, self.Ply)
        self.backs = Material("PrefinBirch", .2, 48, 96, self.Ply)
        self.finished_ends = Material(species, .73, 48.5, 96.5, self.UltraCore)
        self.finished_bottoms = self.finished_ends
        self.finished_tops = self.finished_ends
        self.finished_backs = self.finished_ends
        self.applied_ends = Material(species, .8125, 48, 96, self.Hardwood)
        
        print("CASEWORK: ", self.casework)
        print("BACKS: ", self.backs)
        print("FINISHED ENDS: ", self.finished_ends)
        print("FINISHED BOTTOMS: ", self.finished_bottoms)
        print("FINISHED TOPS: ", self.finished_tops)
        print("FINISHED BACKS: ", self.finished_backs)
        print("APPLIED ENDS: ", self.applied_ends)
        


class Material:
    def __init__(self, color="new_material_color", thickness=.75, x=48, y=96, core=None):
        self.color = color
        self.thickness = thickness
        self.x = x
        self.y = y
        if core:
            self.core = core
        else: self.core = Core()
        
    def __str__(self):
        return str(self.x) + " x " + str(self.y) + " x " + str(self.thickness) + " " + self.color + " " + self.core.core_name 
        
class Core:
    def __init__(self, name="Ply"):
        self.core_name = name
        self.density = 1 #used to calculate tool feed rates
