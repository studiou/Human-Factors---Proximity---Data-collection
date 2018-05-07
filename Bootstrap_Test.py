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
IN_vecX1 = 1
IN_vecY1 = 5
IN_vecX2 = 3
IN_vecY2 = 1

#non-intersecting vector
Non_IN_vecX1 = 1
Non_IN_vecY1 = 1
Non_IN_vecX2 = 1
Non_IN_vecY2 = 5

# boarding vector
#Vector 1
BVec1p1_x = 1
BVec1p1_y = 5
BVec1p2_x = 4
BVec1p2_y = 4

#Vector 2
BVec2p1_x = 3
BVec2p1_y = 3
BVec2p2_x = 5
BVec2p2_y = 5



class Speedcal(unittest.TestCase):
    """ Unit Test Framework Class """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_intersecting_test1(self):
        output = Bootstrap.triangle_intersection_test(IN_vecX1, IN_vecY1,IN_vecX2,IN_vecY2, triX1, triY1, triX2, triY2, triX3, triY3)
        expectedTimeOutcome = "motion detected"
        self.assertEqual(expectedTimeOutcome, output)

    def test_intersecting_test2(self):
        output = Bootstrap.triangle_intersection_test(Non_IN_vecX1, Non_IN_vecY1,Non_IN_vecX2,Non_IN_vecY2, triX1, triY1, triX2, triY2, triX3, triY3)
        expectedTimeOutcome = "motion not detected"
        self.assertEqual(expectedTimeOutcome, output)

    def test_intersecting_test5(self):
        output = Bootstrap.line_intersection_test(BVec1p1_x, BVec1p1_y, BVec1p2_x, BVec1p2_y, BVec2p1_x, BVec2p1_y, BVec2p2_x, BVec2p2_y)
        expectedTimeOutcome = 1
        self.assertEqual(expectedTimeOutcome, output)



if __name__ == "__main__":
    unittest.main()
