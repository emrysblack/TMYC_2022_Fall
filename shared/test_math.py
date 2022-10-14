import unittest
from shared.math import RightAngleMath

class TestRightAngleMath(unittest.TestCase):
    def test_intersects(self):
        line1 = ((0,0),(0,4))
        line2 = ((-2,2),(2,2))
        line3 = ((2,0),(2,4))
        self.assertEqual(RightAngleMath.intersects(line1, line2), (0,2))
        self.assertEqual(RightAngleMath.intersects(line2, line3), (2,2))
        self.assertFalse(RightAngleMath.intersects(line1, line3))

    def test_contains(self):
        self.assertTrue(RightAngleMath.contains(((0,0),(0,2)),(0,1)))
        self.assertTrue(RightAngleMath.contains(((-2,0),(2,0)),(1,0)))
        self.assertFalse(RightAngleMath.contains(((0,0),(0,2)),(1,1)))

    def test_distance(self):
        self.assertEqual(RightAngleMath.get_distance_manhattan((3,3)), 6)
        self.assertEqual(RightAngleMath.get_distance_manhattan((-3,3)), 6)
        self.assertEqual(RightAngleMath.get_distance_manhattan((-3,-3)), 6)
        self.assertEqual(RightAngleMath.get_distance_manhattan((0,-3)), 3)


if __name__ == '__main__':
    unittest.main()