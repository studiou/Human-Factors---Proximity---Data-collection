"""
File assumes you have the unittest2 or unittest package loaded.

Unit tests designed for Processed_Data_Class
"""
import unittest
import os.path

from Processed_Data_Class import *
from PolarPointClass import *
from CartesianPointClass import *
from PersonProfileClass import *
from Dict_Enum import *


TestDataSample1 = {u'Sub.17.Aug.28.10.47pm.a': [u'Female', u'Adult', u'Hit', u'Dispense', 37L, 0L, u'00:00:03:908', 17L, 0L, u'00:00:04:483', 11L, 15L, u'00:00:05:067', 18L, -31L, u'00:00:05:666', 47L, -46L, u'00:00:29:845', 33L, 4L, u'00:00:28:756']}
TestDataSample1BadLength = {u'Sub.17.Aug.28.10.47pm.a': [u'Female', u'Adult', u'Hit', u'Dispense', 37L, 0L, u'00:00:03:908', 17L, 0L, u'00:00:04:483', 11L, 15L, u'00:00:05:067', 18L, -31L, u'00:00:05:666', 47L, -46L, u'00:00:29:845', 33L, 4L]}

TestDataSample2 = {u'Sub.4.August.17.5:31am': [u'Female', u'Adult', u'Hit', u'Fridge door (no dispensor)', 15L, -31L, u'00:00:02:546', 30L, -40L, u'00:00:02:239', 15L, -31L, u'00:00:02:546', 30L, -40L, u'00:00:02:239', 23L, -45L, u'00:00:06:580', 38L, -12L, u'00:00:07:013']}
TestDataSample2_BadLength = {u'Sub.4.August.16.8:18pm': [u'Female', u'Adult', u'Hit', u'Fridge door (no dispensor)', 21L, -15L, u'00:00:01:163', 39L, -30L, u'00:00:00:483', 21L, -15L, u'00:00:01:163', 22L, -40L, u'00:00:01:763', 14L, -30L, u'00:00:14:174', 38L, -20L]} 

# same as test sample 2 except we made right foot closer to dispenser at fridge....
TestDataSample3 = {u'Sub.4.August.17.5:31am': [u'Female', u'Adult', u'Hit', u'Fridge door (no dispensor)', 15L, -31L, u'00:00:02:546', 30L, -40L, u'00:00:02:239', 30L, -40L, u'00:00:03:239', 15L, -31L, u'00:00:03:546', 23L, -45L, u'00:00:06:580', 38L, -12L, u'00:00:07:013']}

TestDataSample_WithFalseAlarm = {u'Sub.17.Aug.27.12.12pm': [u'Female', u'Adult', u'False alarm', u'Make a selection', 31L, -22L, u'00:00:05:558', 16L, 27L, u'00:00:06:100', u'None', u'None', u'None', u'None', u'None', u'None', 25L, 87L, u'00:00:06:595', 16L, 27L, u'00:00:06:100']}
TestDataSample_WithFalseAlarmBadDataLength = {u'Sub.17.Aug.27.12.12pm': [u'Female', u'Adult', u'False alarm', u'Make a selection', 31L, -22L, u'00:00:05:558', 16L, 27L, u'00:00:06:100', u'None', u'None', u'None', u'None', u'None', u'None', 25L, 87L, u'00:00:06:595', 16L, 27L, u'00:00:06:100',0]}

# {u'Sub.17.Aug.28.10.47pm.a': [u'Female', u'Adult', u'Hit', u'Dispense', 37L, 0L, u'00:00:03:908', 17L, 0L, u'00:00:04:483', 11L, 15L, u'00:00:05:067', 18L, -31L, u'00:00:05:666', 47L, -46L, u'00:00:29:845', 33L, 4L, u'00:00:28:756']}
# {u'Sub.17.Aug.29.6.44pm.b': [u'Female', u'Adult', u'Hit', u'Fridge door (no dispensor)', 22L, -8L, u'00:00:03:396', 36L, -44L, u'00:00:02:521', 18L, 5L, u'00:00:04:268', 16L, -31L, u'00:00:03:812', 18L, 10L, u'00:00:11:777', 40L, -10L, u'00:00:12:963']}
# {u'Sub.17.Aug.27.4.33pm': [u'Female', u'Adult', u'Hit', u'Fridge door (dispensor side)', 45L, 5L, u'00:00:01:277', 25L, -28L, u'00:00:01:894', 25L, -5L, u'00:00:02:397', 25L, -28L, u'00:00:01:894', 19L, 0L, u'00:00:15:361', 38L, -24L, u'00:00:16:208']}
# {u'Sub.17.Aug.27.10.04am': [u'Female', u'Adult', u'False alarm', u'Dispense', 43L, -44L, u'00:00:02:989', 22L, -11L, u'00:00:03:523', u'None', u'None', u'None', u'None', u'None', u'None', 24L, 50L, u'00:00:03:954', 25L, 90L, u'00:00:04:656']}
# {u'Sub.17.Aug.27.12.12pm': [u'Female', u'Adult', u'False alarm', u'Make a selection', 31L, -22L, u'00:00:05:558', 16L, 27L, u'00:00:06:100', u'None', u'None', u'None', u'None', u'None', u'None', 25L, 87L, u'00:00:06:595', 16L, 27L, u'00:00:06:100']}
# {u'Sub.17.Aug.28.10.01pm': [u'Female', u'Adult', u'Hit', u'Dispense', 42L, -38L, u'00:00:05:383', 22L, -35L, u'00:00:06:066', 11L, 10L, u'00:00:06:520', 15L, -45L, u'00:00:07:144', 47L, -35L, u'00:00:21:023', 31L, -15L, u'00:00:20:369']}
# {u'Sub.17.Aug.27.3.49pm': [u'Female', u'Adult', u'Hit', u'Fridge door (no dispensor)', 19L, 2L, u'00:00:03:302', 38L, -25L, u'00:00:02:752', 16L, 5L, u'00:00:04:181', 12L, -20L, u'00:00:03:741', 40L, -33L, u'00:00:15:703', 29L, -10L, u'00:00:14:545']}
# {u'Sub.17.Aug.27.2.49pm': [u'Female', u'Adult', u'Hit', u'Fridge door (no dispensor)', 22L, 0L, u'00:00:06:590', 33L, -44L, u'00:00:05:863', 9L, -32L, u'00:00:08:512', 21L, -25L, u'00:00:07:529', 9L, -32L, u'00:00:08:512', 35L, -10L, u'00:00:23:189']}
# {u'Sub.17.Aug.27.9.23am': [u'Female', u'Adult', u'Hit', u'Fridge door (no dispensor)', 41L, -5L, u'00:00:04:952', 19L, -18L, u'00:00:05:454', 13L, 20L, u'00:00:05:981', 19L, -18L, u'00:00:05:454', 18L, -3L, u'00:00:10:180', 39L, -9L, u'00:00:11:826']}
# {u'Sub.17.Aug.27.3.24pm': [u'Female', u'Adult', u'False alarm', u'Make a selection', 25L, -15L, u'00:00:01:112', 42L, -53L, u'00:00:00:00:552', u'None', u'None', u'None', u'None', u'None', u'None', 36L, 59L, u'00:00:02:195', 21L, 47L, u'00:00:01:495']}
# {u'Sub.17.Aug.29.6.49pm': [u'Female', u'Adult', u'Hit', u'Fridge door (no dispensor)', 39L, 5L, u'00:00:03:579', 18L, -15L, u'00:00:03:930', 18L, 15L, u'00:00:04:581', 18L, -15L, u'00:00:03:930', 22L, 0L, u'00:00:08:569', 46L, 5L, u'00:00:09:337']}
# {u'Sub.17.Aug.27.12.06pm': [u'Female', u'Adult', u'Hit', u'Fridge door (no dispensor)', 15L, -18L, u'00:00:06:389', 31L, -30L, u'00:00:05:556', 15L, -18L, u'00:00:06:389', 31L, -30L, u'00:00:05:556', 15L, -18L, u'00:00:06:389', 36L, -25L, u'00:00:56:418']}
# {u'Sub.17.Aug.27.2.22pm': [u'Female', u'Adult', u'Hit', u'Fridge door (no dispensor)', 20L, 10L, u'00:00:01:987', 37L, 2L, u'00:00:01:004', 20L, 10L, u'00:00:01:987', 28L, -22L, u'00:00:06:107', 48L, -48L, u'00:00:20:255', 36L, -28L, u'00:00:19:683']

class TestCartesianClass(unittest.TestCase):
    """ Unit Test Framework Class """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_instantiation_WithTestData1YieldsProper_pnum_video(self):
        for key, value in TestDataSample1.iteritems():
            actualEntry = P_Data(key, value)
            self.assertEqual('Sub.17.Aug.28.10.47pm.a', actualEntry.pnum_video)
  
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
            self.assertEqual("Dispense", actualEntry.target)
   
    def test_instantiation_BadLength_NoAttributes(self):
        for key, value in TestDataSample2_BadLength.iteritems():
            actualEntry = P_Data(key, value)
            self.assertEqual(None, actualEntry.target)
              
    def test_instantiation_WithNoArrayu(self):
        for key, value in TestDataSample_WithFalseAlarm.iteritems():
            actualEntry = P_Data(key)
            self.assertEqual(None, actualEntry.sex)
 
    def test_instantiation_WithHitArrayDataLengthWrong(self):
        for key, value in TestDataSample1BadLength.iteritems():
            actualEntry = P_Data(key, value)
            self.assertEqual(None, actualEntry.sex)
 
    def test_instantiation_WithMissArrayDataLengthWrong(self):
        for key, value in TestDataSample_WithFalseAlarmBadDataLength.iteritems():
            actualEntry = P_Data(key,value)
            self.assertEqual(None, actualEntry.sex)
              
    def test_instantiation_WithFalseAlarm_YieldsSex(self):
        for key, value in TestDataSample_WithFalseAlarm.iteritems():
            actualEntry = P_Data(key, value)
            self.assertEqual("Female", actualEntry.sex)
 
    def test_instantiation_WithTestData1_FirstPersonProfileCorrectSelectingLeft(self):
        for key, value in TestDataSample1.iteritems():
            actualEntry = P_Data(key, value)
            self.assertEqual(0.0, actualEntry.PersonProfile1.time_seconds)
            self.assertEqual(37.25, actualEntry.PersonProfile1.pointNear.radius)
            self.assertEqual(6.71, actualEntry.PersonProfile1.pointNear.angle)
            
    def test_instantiation_WithTestData1_FirstPersonProfileCorrectSelectingRight(self):
        for key, value in TestDataSample2.iteritems():
            actualEntry = P_Data(key, value)
            self.assertEqual(0.0, actualEntry.PersonProfile1.time_seconds)
            self.assertEqual(34.29, actualEntry.PersonProfile1.pointNear.radius)
            self.assertEqual(-41.26, actualEntry.PersonProfile1.pointNear.angle)        
            
    def test_instantiation_WithTestData1_2ndPersonProfileCorrectSelectingForHitLeft(self):
        for key, value in TestDataSample1.iteritems():
            actualEntry = P_Data(key, value)
            self.assertEqual(1.16, actualEntry.PersonProfile2.time_seconds)
            self.assertEqual(11.83, actualEntry.PersonProfile2.pointNear.radius)
            self.assertEqual(36.57, actualEntry.PersonProfile2.pointNear.angle)
            
    def test_instantiation_WithTestData1_2ndPersonProfileCorrectSelectingForHitRight(self):
        for key, value in TestDataSample3.iteritems():
            actualEntry = P_Data(key, value)
            self.assertEqual(1.31, actualEntry.PersonProfile2.time_seconds)
            self.assertEqual(18.96, actualEntry.PersonProfile2.pointNear.radius)
            self.assertEqual(-37.19, actualEntry.PersonProfile2.pointNear.angle)
                        
if __name__ == "__main__":
    unittest.main()
