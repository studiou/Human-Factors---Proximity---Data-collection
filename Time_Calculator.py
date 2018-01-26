import datetime
from datetime import timedelta

def oddest_time(time_1, time_2):
    # accepts two timestamps and returns the oldest

    t1 = timedelta(days = int(time_1[0]), hours=int(time_1[1]), minutes=int(time_1[2]), milliseconds=int(time_1[3]))
    t2 = timedelta(days = int(time_2[0]), hours=int(time_2[1]), minutes=int(time_2[2]), milliseconds=int(time_2[3]))
    oldest = min(t1,t2)

    return(oldest)

def difference_bt_time(time_1, time_2):
    #subtracts the first timestamp by the second timestamp
    t1 = timedelta(days = int(time_1[0]), hours=int(time_1[1]), minutes=int(time_1[2]), milliseconds=int(time_1[3]))
    t2 = timedelta(days = int(time_2[0]), hours=int(time_2[1]), minutes=int(time_2[2]), milliseconds=int(time_2[3]))
    outcome = t2 - t1

    return(outcome)