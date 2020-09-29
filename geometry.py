# geometry.py

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    @property
    def magnitude(self):
        return abs(self.x) + abs(self.y)
        
    def __str__(self):
        return "Point({0}, {1})".format(self.x, self.y)
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
    def __mul__(self, s): # s is a scalar
        x = self.x * s
        y = self.y * s
        return Point(x, y)
    
    def __lt__(self, other):
        return self.magnitude < other.magnitude
    
    def __gt__(self, other):
        return self.magnitude > other.magnitude
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
        
class Line:
    def __init__(self, start=Point(0,0), end=Point(0,0)):
        self.start = start
        self.end = end
        
        @property
        def location(self):
            return self.start
        
        @location.setter
        def location(self, value):
            self.start = value
            
        @property
        def length(self):
            return abs(self.end - self.start)
        
    def __str__(self):
        return "Line({0}, {1})".format(self.start, self.end)
    
    def __eq__(self, other):
        return self.start == other.start and self.end == other.end
        
        
class Rect:
    def __init__(self, size=Point(1,1), location=Point(0,0)):
        self.size = size
        self.location = location
            
        @property
        def y(self):
            return abs(self.size.y)
        @property
        def width(self):
            return abs(self.size.y)
            
        @property
        def x(self):
            return abs(self.size.x)
        @property
        def length(self):
            return abs(self.size.x)
            
        @property
        def area(self):
            return abs(self.size.x * self.size.y)
        
    def __str__(self):
        return "Rect({0}, {1})".format(self.size, self.location)
    
    def __eq__(self, other):
        return self.size == other.size and self.location == other.location
    
    def __mul__(self, s): # s is a scalar. use this method for scaling
        size = self.size * s
        return Rect(size, self.location)
    
    
class Arc:
    def __init__(self, location=Point(0,0), radius=1, angle=0, sweep=360, diameter=None):
        self.location = location
        self.angle = angle
        self.sweep = sweep
        if diameter and radius==1:
            self.radius = diameter*.5
        else: self.radius = radius
        
    @property
    def diameter(self):
        return self.radius * 2
    
    @property
    def circumference(self):
        return self.radius * math.pi
    
    @property
    def area(self):
        return ((math.pi * self.radius) ** 2) * (360.0/self.sweep)
        
    def __str__(self):
        return "Arc({0}, {1})".format(self.location, self.radius)
    
    def __eq__(self, other):
        return self.location == other.location and self.radius == other.radius
    
    def __mul__(self, s): # s is a scalar. use this method for scaling
        radius = self.radius * s
        return Arc(self.location, radius, self.angle, self.sweep)
        
