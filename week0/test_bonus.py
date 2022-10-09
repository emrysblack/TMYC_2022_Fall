from unittest.mock import patch
import unittest
from io import StringIO
from week0.bonus import ShipComputer


class TestMath(unittest.TestCase):
    def test_add(self):
        """
        Test basic adding
        """
        computer = ShipComputer([1,0,0,0,99])
        computer.execute()
        self.assertEqual(computer.codes, [2,0,0,0,99])

    def test_mul(self):
        """
        Test basic multiply
        """
        computer = ShipComputer([2,3,0,3,99])
        computer.execute()
        self.assertEqual(computer.codes, [2,3,0,6,99])
    
    def test_mul_big(self):
        """
        Test basic multiply on bigger number
        """
        computer = ShipComputer([2,4,4,5,99,0])
        computer.execute()
        self.assertEqual(computer.codes, [2,4,4,5,99,9801])
    
    def test_add_mul(self):
        """
        Test addition op combined with mul
        """
        computer = ShipComputer([1,1,1,4,99,5,6,0,99])
        computer.execute()
        self.assertEqual(computer.codes, [30,1,1,4,2,5,6,0,99])
    
class TestJumpCompare(unittest.TestCase):
    def runIOTest(self, given_answer, expected_out, data):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
            computer = ShipComputer(data)
            computer.execute()
            self.assertEqual(fake_out.getvalue().strip(), expected_out)
    

    def test_jump_1(self):
        """
        should print 0 if input is 0 and 1 otherwise
        """
        data = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        self.runIOTest(0, "0", data.copy())
        self.runIOTest(1, "1", data.copy())
        self.runIOTest(-1, "1", data.copy())
    
    def test_jump_2(self):
        """
        should print 0 if input is 0 and 1 otherwise
        """
        data = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
        self.runIOTest(0, "0", data.copy())
        self.runIOTest(1, "1", data.copy())
        self.runIOTest(-1, "1", data.copy())
    
    def test_jump_3(self):
        """
        should print 999 if input is below 8,
        1000 if input is 8 and
        1001 if input is above 8
        """
        data = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
                1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
                999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        self.runIOTest(7, "999", data.copy())
        self.runIOTest(8, "1000", data.copy())
        self.runIOTest(9, "1001", data.copy())

if __name__ == '__main__':
    unittest.main()