# material.py


Ply = Core()
PB = Core("PB")
UltraCore = Core("UC")
MDF = Core("MDF")

class Material:
    def __init__(self, color="new_material_color", thickness=.75, x=48, y=96):
        self.color = color
        self.thickness = thickness
        self.x = x
        self.y = y
        self.core = Ply
        
class Core:
    def __init__(self, name="Ply"):
        self.core_name = name
        self.density = 1 #used to calculate tool feed rates
