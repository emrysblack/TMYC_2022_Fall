import unittest
from week3.main import check, six_digits, increasing, has_duplicates, has_double

class Test(unittest.TestCase):
    def testSixDigits(self):
        self.assertTrue(check("111111", six_digits))
        self.assertFalse(check("223", six_digits))
    
    def testIncreasing(self):
        self.assertTrue(check("1123", increasing))
        self.assertFalse(check("2230", increasing))
    
    def testHasDuplicates(self):
        self.assertTrue(check("111", has_duplicates))
        self.assertFalse(check("123", has_duplicates))
    
    def testHasDouble(self):
        self.assertTrue(check("112", has_double))
        self.assertFalse(check("123", has_double))
        self.assertFalse(check("111", has_double))

    def testValid(self):
        self.assertTrue(check("111111", six_digits, increasing, has_duplicates))
        self.assertTrue(check("112233", six_digits, increasing, has_double))
        self.assertTrue(check("111122", six_digits, increasing, has_double))

    def testInvalid(self):
        self.assertFalse(check("223450", six_digits, increasing, has_duplicates))
        self.assertFalse(check("123789", six_digits, increasing, has_duplicates))
        self.assertFalse(check("111111", six_digits, increasing, has_double))
        self.assertFalse(check("123444", six_digits, increasing, has_double))
        self.assertFalse(check("223450", six_digits, increasing, has_double))
        self.assertFalse(check("123789", six_digits, increasing, has_double))

if __name__ == '__main__':
    unittest.main()