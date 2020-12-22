# job_settings.py
import material

library = material.Library()
casework_material = library.casework
finished_end_material = library.finished_ends
finished_bottom_material = library.finished_bottoms
finished_top_material = library.finished_tops
back_material = library.backs
finished_back_material = library.finished_backs
applied_ends_material = library.applied_ends
drawer_box_material = library.casework
drawer_bottom_material = library.backs
blind_panel_material = library.applied_ends

hinge_type = "standard"
slide_type = "undermount"
kick_type = "integrated"

drawer_rabbet_depth = .125 # how deep to rabbet drawer sides for front/back/solid bottom

drawer_bottom_inset = .3937 # how far from bottom of drawer side to bottom of drawer bottom
drawer_bottom_slot_width = .25 #how wide is the dado slot for drawer bottoms

back_rabbet_depth = .125 #how deep to rabbet the back into the sides/top/bottom of cabinet
back_inset = .375 # how far from the back of the cabinet side to the back of the cabinet back
back_slot_depth = .25

spanner_rabbet_depth = .125 #how deep a cabinet spanner should stick into a rabbet

pilot_overdrill = .12 #how much deeper to drill a tapered pilot bit into spoilboard
pilot_distance_from_edge = 2.0 #how far from end of joint to pilot hole
pilot_min_distance_from_edge = 1.25 #how far from end of joint to pilot hole in extreme case
pilot_max_spacing = 6 # maximum distance between pilot holes
pilot_min_spacing = 2.5 # minimum distance between pilot holes

vertical_back_spanner_height = 5.5
        
        
