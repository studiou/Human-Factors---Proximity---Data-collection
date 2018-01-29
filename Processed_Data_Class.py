__author__ = 'joel'

import math 
import Time_Calculator
from PolarPointClass import *
from CartesianPointClass import *
from PersonProfileClass import *
from Dict_Enum import *

class P_Data:
    def __init__(self, pnum_video=None, dataArray=None):
        # the participant number - shared for each household
        self.pnum_video = pnum_video
        
        
        if (dataArray != None) and ((len(dataArray) == Raw.ArrayLength)): 
            self.sex = dataArray[Raw.sex]
            self.age = dataArray[Raw.age]
            self.event = dataArray[Raw.event]
            self.target = dataArray[Raw.target]
#             first find the oldest
#             then given that...  the first time is always 0..
#             use routine to calculate the 2 points in the person profile
            foot = "Left"
            point = PolarPointClass(37, 0)
            pointNear, pointFar = GenerateProfile(self.age, self.sex, foot, point)
            self.PersonProfile1 = PersonProfileClass(0, pointNear, pointFar)
#             
# #             #find the oldest time and report that as the first step
# #             flag = Time_Calculator.oldest_time(dataArray[Raw.firstLEFTtstamp,Raw.firstRIGHTtstamp])
# #             print flag
# #             if flag == dataArray[Raw.firstLEFTtstamp]:
# #                 self.firstStep = dataArray[Raw.firstLEFTtstamp]
# #             else:
# #                 self.firstStep = dataArray[Raw.firstRIGHTtstamp]
        else:
            self.sex = None
            self.age = None
            self.event = None
            self.target = None
            self.firstStep = None


# This function will calculate the 2 points that represent the minecraft person 
# given the sex and age of the person.   
# note in the first iteration the age does not matter and everyone is an adult
AdultMaleShortSide_inches = 5.5
AdultMaleLongSide_inches = 8.95
AdultFemaleShortSide_inches = 4.35
AdultFemaleLongSide_inches = 11.35

def GenerateProfile(age = None, sex = None, foot = None, point = None):
    if ((age !="Adult") or not ((sex == "Female") or (sex == "Male")) or not ((foot == "Left") or (foot == "Right"))):
        point1 = PolarPointClass()
        point2 = PolarPointClass()
    else:
        if (sex == "Male"):
            shortSide_inches = AdultMaleShortSide_inches
            longSide_inches = AdultMaleLongSide_inches
        else:
            shortSide_inches = AdultFemaleShortSide_inches
            longSide_inches = AdultFemaleLongSide_inches
            
        deltaShort_x = shortSide_inches * math.cos(math.radians(point.angle))
        deltaShort_y = shortSide_inches * math.sin(math.radians(point.angle))
        deltaLong_x = longSide_inches * math.cos(math.radians(point.angle))
        deltaLong_y = longSide_inches * math.sin(math.radians(point.angle))
        
        orig_x, orig_y = point.getCartesianCoordinates()
        if (point.angle < 0):
            if (foot == "Left"):
                p1x = orig_x - deltaLong_x
                p1y = orig_y - deltaLong_y
                p2x = orig_x + deltaShort_x
                p2y = orig_y + deltaShort_y 
            else:
                p1x = orig_x - deltaShort_x
                p1y = orig_y - deltaShort_y
                p2x = orig_x + deltaLong_x
                p2y = orig_y + deltaLong_y 
        else:
            if (foot == "Left"):
                print "\n I got here for angle and foot\n"
                print " orig_x = " + str(orig_x)
                print " orig_y = " + str(orig_y)
                print " Delta x short = " + str(deltaShort_x)
                print " Delta y short = " + str(deltaShort_y)
                print " Delta x long = " + str(deltaLong_x)
                print " Delta y long = " + str(deltaLong_y)
                
                p1x = orig_x + deltaShort_x
                p1y = orig_y - deltaShort_y 
                p2x = orig_x - deltaLong_x
                p2y = orig_y + deltaLong_y
            else:
                p1x = orig_x + deltaLong_x
                p1y = orig_y - deltaLong_y 
                p2x = orig_x - deltaShort_x
                p2y = orig_y + deltaShort_y
        cartesianP1 = CartesianPointClass(p1x,p1y)
        polarP1_radius, polarP1_angle =  cartesianP1.getPolarCoordinates()
        print "PolarR radius = " + str(polarP1_radius)
        print "PolarR angle = " + str(polarP1_angle)
                
        print "Cartesian x = " + str(cartesianP1.x)
        print "Cartesian y = " + str(cartesianP1.y)
        
        point1 = PolarPointClass(polarP1_radius, polarP1_angle)
        print "polar radius = " + str(point1.radius)
        print "polar angle = " + str(point1.angle)
        
        
        cartesianP2 = CartesianPointClass(p2x,p2y)
        polarP2_radius, polarP2_angle =  cartesianP2.getPolarCoordinates()
        point2 = PolarPointClass(polarP2_radius, polarP2_angle)
    return point1, point2


        
                          
            
            
            
        
        
            
        
        
        
                              
 
            
            
