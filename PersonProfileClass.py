#!/usr/bin/python
#
# Class to be used for a person rpofile - 1 time 2 polar coordinates 
# mainly a data storage class but also supports some basic conversion routines to go from

class PersonProfileClass:
    def __init__(self , time=None, polarPoint1=None, polarPoint2=None):
        self.time_seconds = time
        self.pointNear = polarPoint1
        self.pointFar = polarPoint2
        
        

