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
    print distance
    timeTaken = timedelta.total_seconds(Time_Calculator.difference_bt_time(time1,time2))
    print timeTaken
    speed = round(distance/timeTaken,2)
    return(speed)