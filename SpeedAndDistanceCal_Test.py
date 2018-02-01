import SpeedAndDistanceCal
import unittest

x2= 28
y2= 31
x1= 6
y1=17

time_1 = 03.302
time_2 = 5.383

class Speedcal(unittest.TestCase):
    """ Unit Test Framework Class """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_calDistance_speedAndDistanceCal(self):
        output = SpeedAndDistanceCal.calDistance(x1, y1, x2, y2)
        expectedTimeOutcome = 26.08
        self.assertEqual(expectedTimeOutcome, output)

    def test_calDistance_speedAndDistanceCal2(self):
        output = SpeedAndDistanceCal.calDistance(x2, y2, x1, y1)
        expectedTimeOutcome = -26.08
        self.assertEqual(expectedTimeOutcome, output)

    def test_calDistance_speedAndDistanceCal2(self):
        output = SpeedAndDistanceCal.calSpeed(x1, y1, x2, y2,time_1,time_2)
        expectedTimeOutcome = 12.53
        self.assertEqual(expectedTimeOutcome, output)


if __name__ == "__main__":
    unittest.main()
