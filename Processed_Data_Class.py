__author__ = 'joel'

from Dict_Enum import *

class P_Data:
    def __init__(self, pnum_video=None, dataArray=None):

        # the participant number - shared for each household
        self.pnum_video = pnum_video
        
        if (dataArray != None) and ((len(dataArray) == Raw.ArrayLengthHit) or (len(dataArray) == Raw.ArrayLengthMiss)): 
            self.sex = dataArray[Raw.sex]
            self.age = dataArray[Raw.age]
            self.event = dataArray[Raw.event]
            self.target = dataArray[Raw.target]
        else:
            self.sex = None
            self.age = None
            self.event = None
            self.target = None    
            
