import unittest
from week4.part1 import part1

class TestPart1(unittest.TestCase):
    def testExample(self):
        self.assertEqual(part1("123456789012", 3, 2), 1)



if __name__ == '__main__':
    unittest.main()