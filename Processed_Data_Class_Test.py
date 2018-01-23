"""
File assumes you have the unittest2 or unittest package loaded.

Unit tests designed for Processed_Data_Class
"""
import unittest
import os.path

from Processed_Data_Class import *

TestDataSample1 = {u'Sub.4.August.16.8:18pm': [u'Female', u'Adult', u'Hit', u'Fridge door (no dispensor)', 21L, -15L, u'00:00:01:163', 39L, -30L, u'00:00:00:483', 21L, -15L, u'00:00:01:163', 22L, -40L, u'00:00:01:763', 14L, -30L, u'00:00:14:174', 38L, -20L, u'00:00:14:537']} 
TestDataSample2_BadLength = {u'Sub.4.August.16.8:18pm': [u'Female', u'Adult', u'Hit', u'Fridge door (no dispensor)', 21L, -15L, u'00:00:01:163', 39L, -30L, u'00:00:00:483', 21L, -15L, u'00:00:01:163', 22L, -40L, u'00:00:01:763', 14L, -30L, u'00:00:14:174', 38L, -20L]} 
TestDataSample2 = {u'Sub.4.August.17.5:31am': [u'Female', u'Adult', u'Hit', u'Fridge door (no dispensor)', 15L, -31L, u'00:00:02:546', 30L, -40L, u'00:00:02:239', 15L, -31L, u'00:00:02:546', 30L, -40L, u'00:00:02:239', 23L, -45L, u'00:00:06:580', 38L, -12L, u'00:00:07:013']}
TestDataSample_WithFalseAlarm = {u'Sub.4.August.16.6:44pm.1.2': [u'Female', u'Adult', u'False alarm', u'Make a selection', 43L, 38L, u'00:00:47:268', 32L, 72L, u'00:00:47:002', u'00:00:00:000', u'00:00:00:000', 43L, 38L, u'00:00:47:268', 32L, 72L, u'00:00:47:002']}

class TestCartesianClass(unittest.TestCase):
    """ Unit Test Framework Class """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_instantiation_WithTestData1YieldsProper_pnum_video(self):
        for key, value in TestDataSample1.iteritems():
            actualEntry = P_Data(key, value)
            self.assertEqual('Sub.4.August.16.8:18pm', actualEntry.pnum_video)
 
    def test_instantiation_WithNoData_pnum_video_is_None(self):
        for key, value in TestDataSample1.iteritems():
            actualEntry = P_Data()
            self.assertEqual(None, actualEntry.pnum_video)
 
    def test_instantiation_WithNoData_pnum_video_is_None(self):
        for key, value in TestDataSample1.iteritems():
            actualEntry = P_Data()
            self.assertEqual(None, actualEntry.pnum_video)
 
    def test_instantiation_Correctfor_sex(self):
        for key, value in TestDataSample1.iteritems():
            actualEntry = P_Data(key, value)
            self.assertEqual("Female", actualEntry.sex)
 
    def test_instantiation_Correctfor_age(self):
        for key, value in TestDataSample1.iteritems():
            actualEntry = P_Data(key, value)
            self.assertEqual("Adult", actualEntry.age)
 
    def test_instantiation_Correctfor_event(self):
        for key, value in TestDataSample1.iteritems():
            actualEntry = P_Data(key, value)
            self.assertEqual("Hit", actualEntry.event)
 
    def test_instantiation_Correctfor_target(self):
        for key, value in TestDataSample1.iteritems():
            actualEntry = P_Data(key, value)
            self.assertEqual("Fridge door (no dispensor)", actualEntry.target)
 
    def test_instantiation_BadLength_NoAttributes(self):
        for key, value in TestDataSample2_BadLength.iteritems():
            actualEntry = P_Data(key, value)
            self.assertEqual(None, actualEntry.target)
            
    def test_instantiation_WithFalseAlarm_YieldsSex(self):
        for key, value in TestDataSample_WithFalseAlarm.iteritems():
            actualEntry = P_Data(key, value)
            self.assertEqual("Female", actualEntry.sex)


if __name__ == "__main__":
    unittest.main()
