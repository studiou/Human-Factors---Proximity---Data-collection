__author__ = 'joel'
#!/usr/bin/python
#
# Class to be used to test if a vector falls within a shape (triangle)
# the class deals in cartesian coordiantes

import math

# Check to see if two lines intersect
# return a 1 if they intersect
# return a 0 if the do not intersect
def line_intersection_test( p0_x, p0_y, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y):


    s1_x = float(p1_x - p0_x)
    s1_y = float(p1_y - p0_y)
    s2_x = float(p3_x - p2_x)
    s2_y = float(p3_y - p2_y)
    outcome = 0

    s = float (-s1_y * (p0_x - p2_x) + s1_x * (p0_y - p2_y)) / (-s2_x * s1_y + s1_x * s2_y)
    t = float ( s2_x * (p0_y - p2_y) - s2_y * (p0_x - p2_x)) / (-s2_x * s1_y + s1_x * s2_y)

    if (s >= 0 and s <= 1 and t >= 0 and t <= 1):
        outcome = 1

    return outcome

#basically feed line segment and the three lines that form the triangle separately to line_intersect_test to see if they intersect
def triangle_intersection_test(vecX1, vecY1, vecX2, vecY2, triX1, triY1, triX2, triY2,triX3, triY3):

    side_1_test = line_intersection_test(vecX1, vecY1, vecX2, vecY2, triX1, triY1, triX2, triY2)
    side_2_test = line_intersection_test(vecX1, vecY1, vecX2, vecY2, triX2, triY2, triX3, triY3)
    side_3_test = line_intersection_test(vecX1, vecY1, vecX2, vecY2, triX1, triY1, triX3, triY3)

    result = side_1_test + side_2_test + side_3_test

    if result > 0:
        outcome = "motion detected"
    else:
        outcome = "motion not detected"

    return outcome