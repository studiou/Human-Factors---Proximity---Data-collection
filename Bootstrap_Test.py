import Bootstrap
import unittest


#triangle aka area of interest
triX1 = 2
triY1 = 2
triX2 = 3
triY2 = 3
triX3 = 4
triY3 = 2

#intersecting vector
IN_vecX1 = 2
IN_vecY1 = 3
IN_vecX2 = 4
IN_vecY2 = 1

#non-intersecting vector
Non_IN_vecX1 = 1
Non_IN_vecY1 = 2
Non_IN_vecX2 = 1
Non_IN_vecY2 = 5



class Speedcal(unittest.TestCase):
    """ Unit Test Framework Class """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_intersecting_test1(self):
        output = Bootstrap.intersecting(IN_vecX1, IN_vecY1,IN_vecX2,IN_vecY2, triX3, triY3, triX1, triY1, triX2, triY2)
        expectedTimeOutcome = "motion detected"
        self.assertEqual(expectedTimeOutcome, output)

    def test_intersecting_test2(self):
        output = Bootstrap.intersecting(Non_IN_vecX1, Non_IN_vecY1,Non_IN_vecX2,Non_IN_vecY2, triX3, triY3, triX1, triY1, triX2, triY2)
        expectedTimeOutcome = "motion not detected"
        self.assertEqual(expectedTimeOutcome, output)

if __name__ == "__main__":
    unittest.main()
