import unittest
from week5.bonus import FlawedFrequencyTransmission as FFT

def strToList(string):
       return [int(x) for x in string]

class Test(unittest.TestCase):    
    def testPhase(self):
        data1 = strToList("12345678")
        data2 = strToList("80871224585914546619083218645595")
        data3 = strToList("19617804207202209144916044189917")
        data4 = strToList("69317163492948606335995924319873")

        self.assertEqual(FFT(data1).step(4),"01029498")
        self.assertEqual(FFT(data2).step(100),"24176176")
        self.assertEqual(FFT(data3).step(100),"73745418")
        self.assertEqual(FFT(data4).step(100),"52432133")
    
    def testRepeatAndShift(self):
        data1 = strToList("03036732577212944063491565474664")
        data2 = strToList("02935109699940807407585447034323")
        data3 = strToList("03081770884921959731165446850517")

        self.assertEqual(FFT(data1, repeat=10_000, shift=7).step(100),"84462026")
        self.assertEqual(FFT(data2, repeat=10_000, shift=7).step(100),"78725270")
        self.assertEqual(FFT(data3, repeat=10_000, shift=7).step(100),"53553731")

    

if __name__ == '__main__':
    unittest.main()