"""
File assumes you have the unittest2 or unittest package loaded.

Unit tests designed for CartesianPointClass
"""
import unittest
import os.path

from CartesianPointClass import *

class TestCartesianClass(unittest.TestCase):
    """ Unit Test Framework Class """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init_with_no_Y(self):
        """ when I create a new instance with no y value - the value of y should be None """
        testInstance = CartesianPointClass(45)
        self.assertEqual(None, testInstance.y)

    def test_init_with_no_X(self):
        """ when I create a new instance with no x value - the value of x should be None """
        testInstance = CartesianPointClass()
        self.assertEqual(None, testInstance.x)
        
    def test_conversion_with_no_Y(self):
        """ when I try to convert a value with no x or no y I get none back for results """
        testInstance = CartesianPointClass(45.0)
        radius, angle = testInstance.getPolarCoordinates()
        self.assertEqual(None, radius)
        self.assertEqual(None, angle)

    def test_conversion_with_no_X(self):
        """ when I try to convert a value with no x or no y I get none back for results """
        testInstance = CartesianPointClass()
        radius, angle = testInstance.getPolarCoordinates()
        self.assertEqual(None, radius)
        self.assertEqual(None, angle)

    def test_conversion_on_UnitIsocolesPositiveX(self):
        """ when I try to convert a unit triangle with positive X I get the right values """
        testInstance = CartesianPointClass(1, 1)
        radius, angle = testInstance.getPolarCoordinates()
        self.assertEqual(1.41, radius)
        self.assertEqual(45, angle)
        
    def test_conversion_on_UnitIsocolesNegativeX(self):
        """ when I try to convert a unit triangle with negative X I get the right values """
        testInstance = CartesianPointClass(-1, 1)
        radius, angle = testInstance.getPolarCoordinates()
        self.assertEqual(1.41, radius)
        self.assertEqual(-45, angle)
        
    def test_conversion_on_345withPositiveX(self):
        """ when I try to convert a 3,4,5 (xyh) triangle with Positive X I get the right values """
        testInstance = CartesianPointClass(3, 4.0)
        radius, angle = testInstance.getPolarCoordinates()
        self.assertEqual(5.00, radius)
        self.assertEqual(36.87, angle)
        
    def test_conversion_on_345withNegativeX(self):
        """ when I try to convert a 3,4,5 (xyh) triangle with Negative X I get the right values """
        testInstance = CartesianPointClass(-3, 4.0)
        radius, angle = testInstance.getPolarCoordinates()
        self.assertEqual(5.00, radius)
        self.assertEqual(-36.87, angle)

if __name__ == "__main__":
    unittest.main()
