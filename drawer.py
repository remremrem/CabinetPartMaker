# drawer.py


class Drawer:
    
    #slide types
    SIDEMOUNT = 1
    UNDERMOUNT = 2
    
    def __init__(self, h=0, w=0, d=0, qty=1, slide=Drawer.UNDERMOUNT):
        self.height = h
        self.width = w
        self.depth = d
        self.slide = slide
        self.quantity = qty
        self.joints = []
        self.parts = []
        
    def addJoint(self, joint=None):
        if joint:
            self.joints.append(joint)
            
    def addPart(self, part=None):
        if part:
            self.parts.append(part)
        
