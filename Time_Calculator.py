import datetime
from datetime import timedelta

def oldest_time(time_1, time_2):
    # accepts two timestamps and returns the oldest
    whichTime = 1
    t1 = returnDeltaTime(time_1)
    t2 = returnDeltaTime(time_2)
    oldest = min(t1,t2)
    if t1 != oldest:
        whichTime = 2
    return(oldest,whichTime)

def returnDeltaTime (time):
    hr, min, sec, ms = map(int, time.split(":"))
    return (timedelta(hours = hr, minutes= min, seconds=sec, milliseconds=ms))


def difference_bt_time(time_1, time_2):
    #subtracts the first timestamp by the second timestamp
    t1 = returnDeltaTime(time_1)
    t2 = returnDeltaTime(time_2)
    outcome = t2 - t1
    return(outcome)