#!/usr/bin/python
#
# Class to be used for a Cartesian coordinate system 
# mainly a data storage class but also supports some basic conversion routines to go from
# cartesianr coordinates to other coordinate systems 

import math 

class CartesianPointClass:
    def __init__(self , x=None, y=None):
        self.x = x
        self.y = y
        if x != None: 
            self.x = float(x)
        if y != None:
            self.y = float(y)
        
    # method to convert the current cartesian coordinates to polar
    def getPolarCoordinates(self):
        radius = None
        angle = None
        if (self.x != None) and (self.y != None):
            radius = (self.x ** 2 + self.y ** 2) ** 0.5
            radius = round(radius, 2)
            if self.y == 0:
                angle = 90
                if self.x < 0:
                    angle = angle * -1
            else:
                # angle is relative to the vertical line at x=0  - so zero is th line at x = 0
                angle = round(math.degrees(math.atan(self.x / self.y)), 2)
        return radius, angle
        
        

