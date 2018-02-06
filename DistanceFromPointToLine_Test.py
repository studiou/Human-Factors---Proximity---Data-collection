"""
File assumes you have the unittest2 or unittest package loaded.

Unit tests designed for CartesianPointClass
"""
import unittest
import os.path

from DistanceFromPointToLine import *

x1_45DegreeLine = 0.0
y1_45DegreeLine = 20.0
x2_45DegreeLine = 20.0
y2_45DegreeLine = 0.0

class TestDistanceFromPointToLine(unittest.TestCase):
    """ Unit Test Framework Class """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPointBelow45DegreeLine(self):
        distance, x, y = DistanceFromPointToLine(x1_45DegreeLine, y1_45DegreeLine, x2_45DegreeLine, y2_45DegreeLine, 0, 0)
        print distance, x, y 
        self.assertEqual(20.0, distance)
        self.assertEqual(0.0, x)
        self.assertEqual(20.0, y)

    def testPointAbove45DegreeLine(self):
        pass
            
    def testPointOn45DegreeLine(self):
        pass
    
    def testPointLeftOfLineWithInfinteSlope(self):
        pass
    
    def testPointRightOfLineWithInfinteSlope(self):
        pass
    
    def testPointOnLineWithInfinteSlope(self):
        pass
    
    def testPointAboveLineWith0Slope(self):
        pass

    def testPointBelowLineWith0Slope(self):
        pass

    def testPointOnLineWith0Slope(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
