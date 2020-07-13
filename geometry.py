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
        def width(self):
            return abs(self.end.y - self.start.y)
            
        @property
        def length(self):
            return abs(self.end.x - self.start.x)
            
        @property
        def area(self):
            return abs(self.length * self.width)
        
    def __str__(self):
        return "Rect({0}, {1})".format(self.start, self.end)
    
    def __eq__(self, other):
        return self.start == other.start and self.end == other.end
        
        
