#!/usr/bin/python
#
# Class to be used for a polar coordinate system 
# mainly a data storage class but also supports some basic conversion routines to go from
# polar coordinates to other coordinate systems 

import math 

class PolarPointClass:
    def __init__(self , radius=None, angle=None):
        self.radius = radius
        self.angle = angle
        if radius != None: 
            self.radius = float(radius)
        if angle != None:
            self.angle = float(angle)
        
    # method to convert the current polar coordinates to cartesian
    def getCartesianCoordinates(self):
        x = None
        y = None
        # Note that angle is relative to the vertical
        if (self.radius != None) and (self.angle != None):
            x = round(self.radius * math.sin(math.radians(self.angle)), 2) 
            y = round(self.radius * math.cos(math.radians(self.angle)), 2) 
        return x, y
        
        

