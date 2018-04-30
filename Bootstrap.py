__author__ = 'joel'
#!/usr/bin/python
#
# Class to be used to test if a vector falls within a shape (triangle)
# the class deals in cartesian coordiantes

import math

# Check whether vector coordinates lie on the same side of the triangle
def side(vecX1, vecY1, vecX2, vecY2, sideX1, sideY1, sideX2,  sideY2):
    z1 = float ((sideX2 - sideX1) * (vecY1 - sideY1) - (vecX1 - sideX1) * (sideY2 - sideY1))
    z2 = float ((sideX2 - sideX1) * (vecY2 - sideY1) - (vecX2 - sideX1) * (sideY2 - sideY1))
    return z1 * z2



def intersecting(vecX1, vecY1, vecX2, vecY2, triX1, triY1, triX2, triY2,triX3, triY3):
     #Check whether segment is outside one of the three half-planes
     #delimited by the triangle.
    #vector 1
    output = "ERROR"
    #vector 1
    f1 = float(side(vecX1, vecY1, triX3, triY3, triX1, triY1, triX2, triY2))
    f3 = float(side(vecX1, vecY1, triX1, triY1, triX2, triY2, triX3, triY3))
    f5 = float(side(vecX1, vecY1, triX2, triY2, triX3, triY3, triX1, triY1))
    #vector 2
    f2 = float(side(vecX2, vecY2, triX3, triY3, triX1, triY1, triX2, triY2))
    f4 = float(side(vecX2, vecY2, triX1, triY1, triX2, triY2, triX3, triY3))
    f6 = float(side(vecX2, vecY2, triX2, triY2, triX3, triY3, triX1, triY1))

    #Check whether triangle is totally inside one of the two half-planes
    #delimited by the segment.
    f7 = side(triX1, triY1, triX2, triY2, vecX1, vecY1, vecX2, vecY2)
    f8 = side(triX2, triY2, triX3, triY3, vecX1, vecY1, vecX2, vecY2)

    #Otherwise we're intersecting with at least one edge */
    output = "motion detected"


    #If segment is strictly outside triangle, or triangle is strictly
    #apart from the line, we're not intersecting
    if ((f1 < 0 and f2 < 0) or (f3 < 0 and f4 < 0) or (f5 < 0 and f6 < 0) or (f7 > 0 and f8 > 0)):
        output = "motion not detected"

    #If segment is aligned with one of the edges, we're overlapping */
    if ((f1 == 0 and f2 == 0) or (f3 == 0 and f4 == 0) or (f5 == 0 and f6 == 0)):
        output = "motion detected"

    #If segment is outside but not strictly, or triangle is apart but
    #not strictly, we're touching */
    if ((f1 <= 0 and f2 <= 0) or (f3 <= 0 and f4 <= 0) or (f5 <= 0 and f6 <= 0) or (f7 >= 0 and f8 >= 0)):
        output = "motion detected"

    #/* If both segment points are strictly inside the triangle, we
    # * are not intersecting either */
    if (f1 > 0 and f2 > 0 and f3 > 0 and f4 > 0 and f5 > 0 and f6 > 0):
        output = "motion not detected"

    return output