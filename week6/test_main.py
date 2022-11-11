import unittest
from week6.main import Orbits

class Test(unittest.TestCase):
    def testGravity(self):
        self.assertEqual(Orbits.get_gravity([-1,0,2], [2,-10,-7]),[1,-1,-1])
    
    def testPositions(self):
        data = Orbits("week6/test_orbits.txt")
        expected = ((-1,2,4,3),(0,-10,-8,5),(2,-7,8,-1))
        self.assertEqual(data._positions, expected)

    def testStep(self):
        data = Orbits("week6/test_orbits.txt")
        moons_expected = [[2, -1, 1],[3, -7, -4],[1, -7, 5],[2, 2, 0]]
        velocity_expected = [[3, -1, -1],[1, 3, 3],[-3, 1, -3],[-1, -3, 1]]
        data.step()
        self.assertEqual(data.moons,moons_expected)
        self.assertEqual(data.vel,velocity_expected)
        
    

if __name__ == '__main__':
    unittest.main()