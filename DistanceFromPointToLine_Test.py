"""
File assumes you have the unittest2 or unittest package loaded.

Unit tests designed for CartesianPointClass
"""
import unittest
import os.path

from DistanceFromPointToLine import *
from CartesianPointClass import *

x1_45DegreeLine = 0.0
y1_45DegreeLine = 20.0
x2_45DegreeLine = 20.0
y2_45DegreeLine = 0.0

x1_VerticalLine = 50.0
y1_VerticalLine = 0.
x2_VerticalLine = 50.0
y2_VerticalLine = 1000.

x1_HorizontalLine = 50.0
y1_HorizontalLine = 1000.
x2_HorizontalLine = 500.0
y2_HorizontalLine = 1000.

class TestDistanceFromPointToLine(unittest.TestCase):
    """ Unit Test Framework Class """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPointBelow45DegreeLine(self):
        distance, x, y = DistanceFromPointToLine(x1_45DegreeLine, y1_45DegreeLine, x2_45DegreeLine, y2_45DegreeLine, 0, 0)
        self.assertEqual(14.14, distance)
        self.assertEqual(10.0, x)
        self.assertEqual(10.0, y)
 
    def testPointAbove45DegreeLine(self):
        # extending the 45 degree line 14.14 * 2!  should yield 20,20 we have made a square
        distance, x, y = DistanceFromPointToLine(x1_45DegreeLine, y1_45DegreeLine, x2_45DegreeLine, y2_45DegreeLine, 20.0, 20.0)
        self.assertEqual(14.14, distance)
        self.assertEqual(10.0, x)
        self.assertEqual(10.0, y)        
             
    def testPointOn45DegreeLine(self):
        distance, x, y = DistanceFromPointToLine(x1_45DegreeLine, y1_45DegreeLine, x2_45DegreeLine, y2_45DegreeLine, 10.0, 10.0)
        self.assertEqual(0, distance)
        self.assertEqual(10.0, x)
        self.assertEqual(10.0, y)        
     
    def testPointLeftOfLineWithInfinteSlope(self):
        distance, x, y = DistanceFromPointToLine(x1_VerticalLine, y1_VerticalLine, x2_VerticalLine, y2_VerticalLine, 10.0, 10.0)
        self.assertEqual(40.0, distance)
        self.assertEqual(x2_VerticalLine, x)
        self.assertEqual(10.0, y)       
             
    def testPointRightOfLineWithInfinteSlope(self):
        distance, x, y = DistanceFromPointToLine(x1_VerticalLine, y1_VerticalLine, x2_VerticalLine, y2_VerticalLine, 550.0, 10.0)
        self.assertEqual(500.0, distance)
        self.assertEqual(x2_VerticalLine, x)
        self.assertEqual(10.0, y)
             
    def testPointOnLineWithInfinteSlope(self):
        distance, x, y = DistanceFromPointToLine(x1_VerticalLine, y1_VerticalLine, x2_VerticalLine, y2_VerticalLine, 50.0, 10.0)
        self.assertEqual(0.0, distance)
        self.assertEqual(x2_VerticalLine, x)
        self.assertEqual(10.0, y)
    
    def testPointAboveLineWith0Slope(self):
        distance, x, y = DistanceFromPointToLine(x1_HorizontalLine, y1_HorizontalLine, x2_HorizontalLine, y2_HorizontalLine, 50.0, y2_HorizontalLine+10.0)
        self.assertEqual(10.0, distance)
        self.assertEqual(50, x)
        self.assertEqual(y2_HorizontalLine, y)

    def testPointBelowLineWith0Slope(self):
        distance, x, y = DistanceFromPointToLine(x1_HorizontalLine, y1_HorizontalLine, x2_HorizontalLine, y2_HorizontalLine, 50.0, y2_HorizontalLine-10.0)
        self.assertEqual(10.0, distance)
        self.assertEqual(50, x)
        self.assertEqual(y2_HorizontalLine, y)
        
    def testPointOnLineWith0Slope(self):
        distance, x, y = DistanceFromPointToLine(x1_HorizontalLine, y1_HorizontalLine, x2_HorizontalLine, y2_HorizontalLine, 50.0, y2_HorizontalLine)
        self.assertEqual(0.0, distance)
        self.assertEqual(50, x)
        self.assertEqual(y2_HorizontalLine, y)
        
    def testPointOnLineReturnsDistanceAsRadius(self):
        distance, x, y = DistanceFromPointToLine(x1_45DegreeLine, y1_45DegreeLine, x2_45DegreeLine, y2_45DegreeLine, 20.0, 20.0)
        cartPoint = CartesianPointClass(x,y)
        radius, angle = CartesianPointClass(x,y).getPolarCoordinates()
        self.assertEqual(radius, distance)
        
if __name__ == "__main__":
    unittest.main()
