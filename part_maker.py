#part_maker.py
import joinery, hardware, job_settings

def makeParts(cabinets):
    for cabinet in cabinets:
        if cabinet.shape == "rectangle":
            makeStandardCabinet(cabinet)
            
def makeStandardCabinet(cabinet):
    
    
def processLeftSide(side, cabinet):
    
            
processPart(part):
    if part.shape == "rectangle":
        
class Part:
    def __init__(self):
        self.length = 0
        self.width = 0
        self.material = None
        self.part_name = "part"
        self.joints = []
        self.hardware = []
        self.location = (0,0)
        self.shape = "rectangle"
        
        
        
    @property
    def x(self):
        return self.length
    @x.setter
    def x(self, value):
        self.length = value
    
    @property
    def y(self):
        return self.width
    @y.setter
    def y(self, value):
        self.width = value
        
    def area(self):
        return self.length * self.width
        
