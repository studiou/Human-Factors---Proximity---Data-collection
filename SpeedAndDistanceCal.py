__author__ = 'joel'
import math
import Time_Calculator
import datetime
from datetime import timedelta

def calDistance(x1, y1, x2, y2):
    # accepts two cartesian points and returns the distance
    outcome = round(math.sqrt(((x2-x1)**(2))+((y2-y1)**(2))),2)
    return(outcome)


def calSpeed(x1, y1, x2, y2,time1,time2):
    # accepts two cartesian points and returns the distance
    distance = calDistance(x1, y1, x2, y2)

    timeTaken = time2 - time1

    #print " x1 = " + str(x1) + " y1 = " + str(y1) + " x2 = " + str(x2) + " y2 = " + str(y2) + " t1 = " + str(time1) +   " t2 = " + str(time2) + "\n distance =" + str(distance) + " time taken = " + str (timeTaken)

    if timeTaken <= 0:
        speed = 999999999   # obviously large
    else:
        speed = round(distance/timeTaken,2)
    return(speed)