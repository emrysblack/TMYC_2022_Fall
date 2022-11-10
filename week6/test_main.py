import unittest
from week6.main import get_positions, get_gravity, step_positions, step_velocities

class Test(unittest.TestCase):
    def testGravity(self):
        self.assertEqual(get_gravity([-1,0,2], [2,-10,-7]),[1,-1,-1])
    
    def testPositions(self):
        data = [[-1,0,2],[2,-10,-7],[4,-8,8]]
        expected = ((-1,2,4),(0,-10,-8),(2,-7,8))
        self.assertEqual(get_positions(data), expected)

    def testStep(self):
        data = [[-1, 0, 2],[2, -10, -7],[4, -8, 8],[3, 5, -1]]
        data1 = [[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        expected = [[2, -1, 1],[3, -7, -4],[1, -7, 5],[2, 2, 0]]
        expected1 = [[3, -1, -1],[1, 3, 3],[-3, 1, -3],[-1, -3, 1]]
        step_velocities(data, data1)
        step_positions(data,data1)
        self.assertEqual(data,expected)
        self.assertEqual(data1,expected1)
        
    

if __name__ == '__main__':
    unittest.main()