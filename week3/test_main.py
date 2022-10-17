import unittest
from week3.main import is_possible, is_possible_with_double

class TestPart1(unittest.TestCase):
    def testValid(self):
        self.assertTrue(is_possible(111111))

    def testInvalid(self):
        self.assertFalse(is_possible(223450))
        self.assertFalse(is_possible(123789))

class TestPart2(unittest.TestCase):
    def testValid(self):
        self.assertTrue(is_possible_with_double(112233))
        self.assertTrue(is_possible_with_double(111122))

    def testInvalid(self):
        self.assertFalse(is_possible_with_double(111111))
        self.assertFalse(is_possible_with_double(123444))
        self.assertFalse(is_possible_with_double(223450))
        self.assertFalse(is_possible_with_double(123789))


if __name__ == '__main__':
    unittest.main()