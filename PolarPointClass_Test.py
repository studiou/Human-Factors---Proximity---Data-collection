"""
File assumes you have the unittest2 or unittest package loaded.

Unit tests designed for PolarPointClass
"""
import unittest
import os.path

from PolarPointClass import *

class TestPolarClass(unittest.TestCase):
    """ Unit Test Framework Class """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init_with_no_angle(self):
        """ when I create a new instance with no angle value - the value of angle should be None """
        testInstance = PolarPointClass(1.0)
        self.assertEqual(None, testInstance.angle)

    def test_init_with_no_radius(self):
        """ when I create a new instance with no radius value - the value of radius should be None """
        testInstance = PolarPointClass()
        self.assertEqual(None, testInstance.radius)
        
    def test_conversion_with_no_angle(self):
        """ when I try to convert a value with no radius or no angle I get none back for results """
        testInstance = PolarPointClass(1.0)
        x, y = testInstance.getCartesianCoordinates()
        self.assertEqual(None, x)
        self.assertEqual(None, y)
 
    def test_conversion_with_no_X(self):
        """ when I try to convert a value with no radius or no angle I get none back for results """
        testInstance = PolarPointClass()
        x, y = testInstance.getCartesianCoordinates()
        self.assertEqual(None, x)
        self.assertEqual(None, y)
         
    def test_conversion_on_UnitIsocolesPositiveAngle(self):
        """ when I try to convert a unit triangle with positive Angle I get the right values """
        testInstance = PolarPointClass(1.41, 45)
        radius, angle = testInstance.getCartesianCoordinates()
        x, y = testInstance.getCartesianCoordinates()
        self.assertEqual(1.0, x)
        self.assertEqual(1.0, y)
         
    def test_conversion_on_UnitIsocolesNegativeAngle(self):
        """ when I try to convert a unit triangle with negative Angle I get the right values """
        testInstance = PolarPointClass(1.41, -45)
        radius, angle = testInstance.getCartesianCoordinates()
        x, y = testInstance.getCartesianCoordinates()
        self.assertEqual(-1.0, x)
        self.assertEqual(1.0, y)
                 
    def test_conversion_on_345withPositiveAngle(self):
        """ when I try to convert a 3,4,5 (xyh) triangle with Positive Angle I get the right values """
        testInstance = PolarPointClass(5.0, 36.87)
        x, y = testInstance.getCartesianCoordinates()
        self.assertEqual(3.0, x)
        self.assertEqual(4.0, y)
        
#         
    def test_conversion_on_345withNegativeAngle(self):
        """ when I try to convert a 3,4,5 (xyh) triangle with Negative AngleI get the right values """
        testInstance = PolarPointClass(5.0, -36.87)
        x, y = testInstance.getCartesianCoordinates()
        self.assertEqual(-3.0, x)
        self.assertEqual(4.0, y)

if __name__ == "__main__":
    unittest.main()
