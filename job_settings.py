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
        
        self.drawer_rabbet_depth = .125 # how deep to rabbet drawer sides for front/back/solid bottom

        self.drawer_bottom_inset = .3937 # how far from bottom of drawer side to bottom of drawer bottom

        self.drawer_bottom_slot_width = .25 #how wide is the dado slot for drawer bottoms

        self.back_rabbet_depth = .125 #how deep to rabbet the back into the sides/top/bottom of cabinet

        self.back_inset = .375 # how far from the back of the cabinet side to the back of the cabinet back

        self.spanner_rabbet_depth = .125 #how deep a cabinet spanner should stick into a rabbet
        
        self.pilot_overdrill = .12 #how much deeper to drill a tapered pilot bit into spoilboard
        
        