import unittest
from week1.main import execute_intcodes

class TestMath(unittest.TestCase):
    def test_add(self):
        """
        Test basic adding
        """
        data = [1,0,0,0,99]
        execute_intcodes(data)
        self.assertEqual(data, [2,0,0,0,99])

    def test_mul(self):
        """
        Test basic multiply
        """
        data = [2,3,0,3,99]
        execute_intcodes(data)
        self.assertEqual(data, [2,3,0,6,99])
    
    def test_mul_big(self):
        """
        Test basic multiply on bigger number
        """
        data = [2,4,4,5,99,0]
        execute_intcodes(data)
        self.assertEqual(data, [2,4,4,5,99,9801])
    
    def test_add_mul(self):
        """
        Test addition op combined with mul
        """
        data = [1,1,1,4,99,5,6,0,99]
        execute_intcodes(data)
        self.assertEqual(data, [30,1,1,4,2,5,6,0,99])

if __name__ == '__main__':
    unittest.main()