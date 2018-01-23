__author__ = 'joel'
class P_Data:
    def __init__(self, pnum, video, sex, age, event, firstLEFTradius_in, firstLEFTdegrees, firstLEFTtstamp, firstRIGHTradius_in, firstRIGHTdegrees, firstRIGHTtstamp, atfridgeLEFTradius_in, atfridgeLEFTdegrees, atfridgeLEFTtstamp, atfridgeRIGHTradius_in, atfridgeRIGHTdegrees, atfridgeRIGHTtstamp, lastLEFTradius_in, lastLEFTdegrees, lastLEFTtstamp, lastRIGHTradius_in, lastRIGHTdegrees, lastRIGHTtstamp ):

        #the participant number - shared for each household
        self.pnum = pnum
        #the number of the video, includes the date and time (a,b,c or 1,2,3 at the end of the name means more than one event in a video)
        self.video = video
        #sex of the person in the video being measured
        self.sex = sex
        #age of the person in the video being measured
        self.age = age
        #coding represents the intent of the person in the video. if it is a hit (e.g. used the fridge) or false alarm (e.g. walking by the fridge)
        self.event = event

        #Paramerters captured when first entering the mat
        # foot distance of the 1st step onto the MAT with LEFT foot (in inches)
        self.firstLEFTradius_in = firstLEFTradius_in
        # angle of the 1st  step onto the MAT with LEFT foot (in degrees)
        self.firstLEFTdegrees = firstLEFTdegrees
        # timestamp of the 1st step onto the MAT with LEFT foot (in 00:00:000 hours, mins, milliseconds)
        self.firstLEFTtstamp  = firstLEFTtstamp
        # foot distance of the 1st  step onto the MAT with RIGHT foot (in inches)
        self.firstRIGHTradius_in  = firstRIGHTradius_in
        # angle of the 1st  step onto the MAT with RIGHT foot (in degrees)
        self.firstRIGHTdegrees  = firstRIGHTdegrees
        # timestamp of the 1st  step onto the MAT with RIGHT foot (in 00:00:000 hours, mins, milliseconds)
        self.firstRIGHTtstamp  = firstRIGHTtstamp


        #Paramerters captured when arriving at the fridge (if a hit, or if they used the fridge in anyway)
        # foot distance of the LEFT foot at fridge (if a hit) (in inches)
        self.atfridgeLEFTradius_in  = atfridgeLEFTradius_in
        # angle of the LEFT foot at fridge (if a hit) (in degrees)
        self.atfridgeLEFTdegrees  = atfridgeLEFTdegrees
        # timestamp of the LEFT foot at fridge (if a hit) (in 00:00:000 hours, mins, milliseconds)
        self.atfridgeLEFTtstamp = atfridgeLEFTtstamp
        # foot distance of the RIGHT foot at fridge (if a hit) (in inches)
        self.atfridgeRIGHTradius_in = atfridgeRIGHTradius_in
        # angle of the RIGHT foot at fridge (if a hit) (in degrees)
        self.atfridgeRIGHTdegrees = atfridgeRIGHTdegrees
        # timestamp of the RIGHT foot at fridge (if a hit) (in 00:00:000 hours, mins, milliseconds)
        self.atfridgeRIGHTtstamp = atfridgeRIGHTtstamp



        #Paramerters captured when leaving the mat
        # foot distance of the Last LEFT foot step before leaving mat (in inches)
        self.lastLEFTradius_in = lastLEFTradius_in
        # angle of the Last LEFT foot step before leaving mat (in degrees)
        self.lastLEFTdegrees = lastLEFTdegrees
        # timestamp of the Last LEFT foot step before leaving mat (in 00:00:000 hours, mins, milliseconds)
        self.lastLEFTtstamp = lastLEFTtstamp
        # foot distance of the Last RIGHT foot step before leaving mat: (in inches)
        self.lastRIGHTradius_in  = lastRIGHTradius_in
        # angle of the Last RIGHT foot step before leaving mat: (in degrees)
        self.lastRIGHTdegrees = lastRIGHTdegrees
        # timestamp of the Last RIGHT foot step before leaving mat: (in 00:00:000 hours, mins, milliseconds)
        self.lastRIGHTtstamp = lastRIGHTtstamp
