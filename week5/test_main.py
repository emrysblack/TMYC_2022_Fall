import unittest
from week5.main import read_orbit_file, get_orbital_distance, get_common_ancestor

class Test(unittest.TestCase):
    def testOrbits(self):
        data = read_orbit_file("week5/test_part1.txt")
        self.assertEqual(get_orbital_distance("D", data), 3)
        self.assertEqual(get_orbital_distance("L", data), 7)
        self.assertEqual(sum(get_orbital_distance(orbit, data) for orbit in data), 42)
    
    def testAncestors(self):
        data = read_orbit_file("week5/test_part2.txt")
        self.assertEqual(get_common_ancestor("YOU", "SAN", data), "D")
        self.assertEqual(get_common_ancestor("L", "B", data), "B")
        self.assertEqual(get_common_ancestor("COM", "COM", data), "COM")
        self.assertEqual(get_common_ancestor("COM", "I", data), "COM")
    

if __name__ == '__main__':
    unittest.main()