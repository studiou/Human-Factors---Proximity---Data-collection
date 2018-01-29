"""
File assumes you have the unittest2 or unittest package loaded.

Unit tests designed for Processed_Data_Class
"""
import unittest
import os.path
import Time_Calculator
from datetime import timedelta
from Processed_Data_Class import *


time_1 = "00:00:05:383"
time_2 = "00:00:03:302"



class TestCartesianClass(unittest.TestCase):
     """ Unit Test Framework Class """
     def setUp(self):
         pass

     def tearDown(self):
         pass

     def test_instantiation_WithTestData1YieldsProper_timeCalculation(self):
      outputTime,outputNumeration = Time_Calculator.oldest_time(time_1,time_2)
      expectedTimeOutcome = timedelta(hours = 00, minutes = 00, seconds = 03, milliseconds = 302)
      self.assertEqual(expectedTimeOutcome, outputTime)
      self.assertEqual(2, outputNumeration)

     def test_instantiation_WithTestData2YieldsProper_timeCalculation(self):
      outputTime,outputNumeration = Time_Calculator.oldest_time(time_2,time_1)
      expectedTimeOutcome = timedelta(hours = 00, minutes = 00, seconds = 03, milliseconds = 302)
      self.assertEqual(expectedTimeOutcome, outputTime)
      self.assertEqual(1, outputNumeration)

     def test_instantiation_WithTestData3YieldsProper_timeCalculation(self):
      outputTime = Time_Calculator.difference_bt_time(time_1,time_2)
      expectedTimeOutcome = timedelta(hours = 00, minutes = -01, seconds = 86, milliseconds = 919)
      print expectedTimeOutcome
      self.assertEqual(expectedTimeOutcome, outputTime)

     def test_instantiation_WithTestData4YieldsProper_timeCalculation(self):
      outputTime = Time_Calculator.difference_bt_time(time_2,time_1)
      expectedTimeOutcome = timedelta(hours = 00, minutes = 00, seconds = 02, milliseconds = 810)
      print expectedTimeOutcome
      self.assertEqual(expectedTimeOutcome, outputTime)

if __name__ == "__main__":
    unittest.main()
