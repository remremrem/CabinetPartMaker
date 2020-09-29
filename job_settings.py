# job_settings.py
import material

class JobSettings:
    def __init__(self):
        self.library = material.Library()
        self.casework_material = self.library.casework
        self.finished_end_material = self.library.finished_ends
        self.finished_bottom_material = self.library.finished_bottoms
        self.finished_top_material = self.library.finished_tops
        self.back_material = self.library.backs
        self.finished_back_material = self.library.finished_backs
        self.applied_ends_material = self.library.applied_ends
        
        self.hinge_type = "standard"
        self.slide_type = "undermount"
        self.kick_type = "integrated"
        
        
        