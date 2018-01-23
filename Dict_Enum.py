__author__ = 'joel'
from enum import Enum
class Raw(Enum):
            # sex - Male/Female
            sex = 0
            # age classification participant Adult/Child
            age = 1
            # event "Hit"/"False alarm"
            event = 2
            #the target (i.e. Dispense, dispensor Controls, Fridge door (dispensor side), Fridge door (no dispensor), Freezer Door)
            target = 3

            # Entering the mat
            # foot distance of the 1st step onto the MAT with LEFT foot (radius,angle,timestamp)
            firstLEFTradius_in = 4
            firstLEFTdegrees = 5
            firstLEFTtstamp = 6
            
            # foot distance of the 1st step onto the MAT with Right foot (radius,angle,timestamp)
            firstRIGHTradius_in = 7
            firstRIGHTdegrees = 8
            firstRIGHTtstamp = 9
            
            #Arriving at the fridge
            # foot distance of the Last step onto the MAT with Left foot (radius,angle,timestamp)
            atfridgeLEFTradius_in = 10
            atfridgeLEFTdegrees = 11
            atfridgeLEFTtstamp = 12
            
            # foot distance of the Last step onto the MAT with Right foot (radius,angle,timestamp)
            atfridgeRIGHTradius_in = 13
            atfridgeRIGHTdegrees = 14
            atfridgeRIGHTtstamp = 15

            #Leaving the mat
            # foot distance of the leaving the MAT with Left foot (radius,angle,timestamp)
            lastLEFTradius_in = 16
            lastLEFTdegrees = 17
            lastLEFTtstamp = 18

            # foot distance of the leaving the MAT with Right foot (radius,angle,timestamp)
            lastRIGHTradius_in = 19
            lastRIGHTdegrees = 20
            lastRIGHTtstamp = 21
            