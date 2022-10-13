import unittest
from week2.main import trace_wire, get_crossings, get_steps

class Test(unittest.TestCase):
    def test_trace_wire(self):
        self.assertEqual(trace_wire(['U3']), [(0,0),(0,3)])
        self.assertEqual(trace_wire(['D3']), [(0,0),(0,-3)])
        self.assertEqual(trace_wire(['R3']), [(0,0),(3,0)])
        self.assertEqual(trace_wire(['L10']), [(0,0),(-10,0)])
        # combo
        self.assertEqual(trace_wire(['R8','U5','L5','D3']), [(0,0),(8,0),(8,5),(3,5),(3,2)])
        self.assertEqual(trace_wire(['U7','R6','D4','L4']), [(0,0),(0,7),(6,7),(6,3),(2,3)])
    
    def test_find_crossings(self):
        # cross
        self.assertEqual(list(get_crossings([(0,0),(0,3)],[(0,0),(-1,0),(-1,2),(4,2)])), [(0,2)])
        # touch
        self.assertEqual(list(get_crossings([(0,0),(3,0)],[(0,0),(0,4),(2,4),(2,0)])), [(2,0)])
        # not touch
        self.assertEqual(list(get_crossings([(0,0),(0,3)],[(0,0),(4,0),(4,2),(1,2)])), [])
        # parallel
        self.assertEqual(list(get_crossings([(0,0),(0,3)],[(0,0),(1,0),(1,4)])), [])
    
    def test_steps(self):
        self.assertEqual(sum(get_steps((2,2),[(0,0),(0,2),(2,2)])), 4)
        self.assertEqual(sum(get_steps((2,2),[(0,0),(2,0),(2,4),(0,4)])), 4)
        self.assertEqual(sum(get_steps((0,-2),[(0,0),(4,0),(4,-2),(-4,-2)])), 10)

if __name__ == '__main__':
    unittest.main()