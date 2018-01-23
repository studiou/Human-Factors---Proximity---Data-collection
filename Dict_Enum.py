__author__ = 'joel'
from enum import Enum
class Raw(Enum):
            #imported_xls_data[x][1] = age of participant (i.e.adult or child)
            age = 1
            #imported_xls_data[x][2] = event (i.e. hit or miss)
            event = 2
            #imported_xls_data[x][3] = the target (i.e. Dispense, dispensor Controls, Fridge door (dispensor side), Fridge door (no dispensor), Freezer Door)
            target = 3

            #Entering the mat
            #imported_xls_data[x][4] = foot distance of the 1st step onto the MAT with LEFT foot (in inches)
            firstLEFTradius_in = 4
            #imported_xls_data[x][5] = angle of the 1st step onto the MAT with LEFT foot (in degrees)
            firstLEFTdegrees = 5
            #imported_xls_data[x][6] = timestamp of the 1st step onto the MAT with LEFT foot (in 00:00:000 hours, mins, milliseconds)
            firstLEFTtstamp = 6
            #imported_xls_data[x][7] = foot distance of the 1st  step onto the MAT with RIGHT foot (in inches)
            firstRIGHTradius_in = 7
            #imported_xls_data[x][8] = angle of the 1st  step onto the MAT with RIGHT foot (in degrees)
            firstRIGHTdegrees = 8
            #imported_xls_data[x][9] = timestamp of the 1st  step onto the MAT with RIGHT foot (in 00:00:000 hours, mins, milliseconds)
            firstRIGHTtstamp = 9

            #Arriving at the fridge
            #imported_xls_data[x][10] = foot distance of the LEFT foot at fridge (if a hit) (in inches)
            atfridgeLEFTradius_in = 10
            #imported_xls_data[x][11] = angle of the LEFT foot at fridge (if a hit) (in degrees)
            atfridgeLEFTdegrees = 11
            #imported_xls_data[x][12] = timestamp of the LEFT foot at fridge (if a hit) (in 00:00:000 hours, mins, milliseconds)
            atfridgeLEFTtstamp = 12
            #imported_xls_data[x][13] = foot distance of the RIGHT foot at fridge (if a hit) (in inches)
            atfridgeRIGHTradius_in = 13
            #imported_xls_data[x][14] = angle of the RIGHT foot at fridge (if a hit) (in degrees)
            atfridgeRIGHTdegrees = 14
            #imported_xls_data[x][15] = timestamp of the RIGHT foot at fridge (if a hit) (in 00:00:000 hours, mins, milliseconds)
            atfridgeRIGHTtstamp = 15




            #Leaving the mat
            #imported_xls_data[x][16] = foot distance of the Last LEFT foot step before leaving mat (in inches)
            lastLEFTradius_in = 16
            #imported_xls_data[x][17] = angle of the Last LEFT foot step before leaving mat (in degrees)
            lastLEFTdegrees = 17
            #imported_xls_data[x][18] = timestamp of the Last LEFT foot step before leaving mat (in 00:00:000 hours, mins, milliseconds)
            lastLEFTtstamp = 18
            #imported_xls_data[x][19] = foot distance of the Last RIGHT foot step before leaving mat: (in inches)
            lastRIGHTradius_in = 19
            #imported_xls_data[x][20] = angle of the Last RIGHT foot step before leaving mat: (in degrees)
            lastRIGHTdegrees = 20
            #imported_xls_data[x][21] = timestamp of the Last RIGHT foot step before leaving mat: (in 00:00:000 hours, mins, milliseconds)
            lastRIGHTtstamp = 21