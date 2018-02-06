def DistanceFromPointToLine(line_x1,line_y1, line_x2,line_y2, point_x, point_y):
    #     calculate line in form y = mx + b.  ultimatley I want form ax + by +c = 0
    # where:
    #    a = -1.0 * slope
    #    b = 1.0
    #    c = -1 * -intercept
    # handle all but a vertical line
    if (line_x1 != line_x2):
        slope = (line_y2 - line_y1)/(line_x2 - line_x1)
        a = -1.0 * slope
        b = 1.0
        if (slope != 0):
            intercept = line_y1 - (slope * line_x1)
            c = -1 * intercept
            distance = round(abs((a * point_x) + (b * point_y) + c)/((a**2 + b**2) ** 0.5),2)
            xOnLine = round(((b * ((b*point_x) - (b*point_y))) - (a * c))/(a**2 + b**2),2)
            yOnLine = round(((a * ((-1.0 * b * point_x) + (a * point_y))) - (b * c))/(a**2 + b**2),2)
        else:
            distance = abs(line_y1 - point_y)
            xOnLine = point_x
            yOnLine = line_y1
    else:   # line is vertical
        distance = abs(line_x1 - point_x)
        xOnLine = line_x1
        yOnLine = point_y
    return distance, xOnLine, yOnLine
