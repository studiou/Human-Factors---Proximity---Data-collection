__author__ = 'joel'
import math

def solveforx(y, angle):
    if angle > 0:
        #x=y*tan(angle)
        x = y*(math.tan(math.radians(angle)))
    else:
        x = 0

    return (x)