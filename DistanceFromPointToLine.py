def DistanceFromPointToLine(line_x1,line_y1, line_x2,line_y2, point_x, point_y):
    #     calculate line in form y = mx + b.  ultimatley I want form ax + by +c = 0
    # where:
    #    a = -1.0 * slope
    #    b = 1.0
    #    c = -1 * -intercept
    # handle all but a vertical line
    if (line_x1 != line_x2):
        slope = (line_y2 - line_y1)/(line_x2 - line_x1)
        intercept = line_y1 - (slope * line_x1)
        a = -1.0 * slope
        b = 1.0
        c = -1 * intercept
        print "\n got here! slope = " + str(slope) + " intercept = " + str(intercept) 

        distance = abs((a * point_x) + (b * point_y) + c)/((a**2 + b**2) ** 0.5)
        xOnLine = ((b * ((b*line_x1) - (b*line_y1))) - (a * c))/(a**2 + b**2)
        yOnLine = ((a * ((-1.0 * b * line_x1) + (a * line_y1))) - (b * c))/(a**2 + b**2)
    else:   # line is vertical
        distance = abs(line_x1 - point_x)
        xOnLine = line_x1
        yOnLine = point_y
    return distance, xOnLine, yOnLine
