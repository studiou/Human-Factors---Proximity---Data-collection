import SpeedAndDistanceCal
import unittest
#non-intersecting
vecX1 = 1
vecY1 = 2
vecX2 = 1
vecY2 = 5

triX1 = 2
triY1 = 2
triX2 = 3
triY2 = 3
triX3 = 4
triY3 = 2

#intersecting
vecX1 = 2
vecY1 = 3
vecX2 = 4
vecY2 = 1

triX1 = 2
triY1 = 2
triX2 = 3
triY2 = 3
triX3 = 4
triY3 = 2



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
