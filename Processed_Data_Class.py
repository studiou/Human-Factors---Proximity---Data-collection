__author__ = 'joel'

import math 
import Time_Calculator
from SpeedAndDistanceCal import *
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
            # first find the oldest ofr the first 2 steps ... 
            oldest, whichTime = Time_Calculator.oldest_time(dataArray[Raw.firstLEFTtstamp],dataArray[Raw.firstRIGHTtstamp])
            reference_time = oldest.total_seconds() # used later as part of time normalization
            if (whichTime == 1):
                foot = "Left"
                point = PolarPointClass(float(dataArray[Raw.firstLEFTradius_in]), float(dataArray[Raw.firstLEFTdegrees]))
            else:
                foot = "Right"
                point = PolarPointClass(float(dataArray[Raw.firstRIGHTradius_in]), float(dataArray[Raw.firstRIGHTdegrees]))
            pointNear, pointFar = GenerateProfile(self.age, self.sex, foot, point)
            self.PersonProfile1 = PersonProfileClass(0, pointNear, pointFar)
            
            # for a hit we need to select the nearest point
            if  (self.event == "Hit"):
                # is left or right foot closer?
                if (dataArray[Raw.atfridgeLEFTradius_in] <= dataArray[Raw.atfridgeRIGHTradius_in]):
                    text_time_stamp = dataArray[Raw.atfridgeLEFTtstamp] 
                    point = PolarPointClass(float(dataArray[Raw.atfridgeLEFTradius_in]), float(dataArray[Raw.atfridgeLEFTdegrees]))
                else:
                    text_time_stamp = dataArray[Raw.atfridgeRIGHTtstamp] 
                    point = PolarPointClass(float(dataArray[Raw.atfridgeRIGHTradius_in]), float(dataArray[Raw.atfridgeRIGHTdegrees]))
                interval_to_fridge = round(Time_Calculator.returnDeltaTime(text_time_stamp).total_seconds() - reference_time,2)
                pointNear, pointFar = GenerateProfile(self.age, self.sex, foot, point)
                self.PersonProfile2 = PersonProfileClass(interval_to_fridge, pointNear, pointFar)
            else: # for a miss we select the last point
                # is the last step left or right?
                if (dataArray[Raw.lastLEFTradius_in] >= dataArray[Raw.lastRIGHTradius_in]):
                    text_time_stamp = dataArray[Raw.lastLEFTtstamp] 
                    point = PolarPointClass(float(dataArray[Raw.lastLEFTradius_in]), float(dataArray[Raw.lastLEFTdegrees]))
                else:
                    text_time_stamp = dataArray[Raw.lastRIGHTtstamp] 
                    point = PolarPointClass(float(dataArray[Raw.lastRIGHTradius_in]), float(dataArray[Raw.lastRIGHTdegrees]))
                interval_to_exit = round(Time_Calculator.returnDeltaTime(text_time_stamp).total_seconds() - reference_time,2)
                pointNear, pointFar = GenerateProfile(self.age, self.sex, foot, point)
                self.PersonProfile2 = PersonProfileClass(interval_to_exit, pointNear, pointFar)


        else:
            self.sex = None
            self.age = None
            self.event = None
            self.target = None
            self.firstStep = None

        self.speed = SpeedAndDistanceCal.calSpeed(self.PersonProfile1.pointNear.getCartesianCoordinates(),
                                                      self.PersonProfile2.pointNear.getCartesianCoordinates(),
                                                      self.PersonProfile1.time_seconds,
                                                      self.PersonProfile1.time_seconds)

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
                p1x = orig_x - deltaLong_x
                p1y = orig_y + deltaLong_y
                p2x = orig_x + deltaShort_x
                p2y = orig_y - deltaShort_y 
            else:
                p1x = orig_x - deltaShort_x
                p1y = orig_y + deltaShort_y
                p2x = orig_x + deltaLong_x
                p2y = orig_y - deltaLong_y
        if p2y < 0:
            p2y = 0 
        cartesianP1 = CartesianPointClass(p1x,p1y)
        polarP1_radius, polarP1_angle =  cartesianP1.getPolarCoordinates()
        point1 = PolarPointClass(polarP1_radius, polarP1_angle)
        cartesianP2 = CartesianPointClass(p2x,p2y)
        polarP2_radius, polarP2_angle =  cartesianP2.getPolarCoordinates()
        point2 = PolarPointClass(polarP2_radius, polarP2_angle)

        if point1.radius > point2.radius:
            point3 = point2
            point2 = point1 
            point1 = point3
        
    return point1, point2


        
                          
            
            
            
        
        
            
        
        
        
                              
 
            
            
