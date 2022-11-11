import unittest
from week5.bonus import FlawedFrequencyTransmission as FFT


class Test(unittest.TestCase):    
    def testPhase(self):
        self.assertEqual(FFT("12345678").step(4),"01029498")
        self.assertEqual(FFT("80871224585914546619083218645595").step(100),"24176176")
        self.assertEqual(FFT("19617804207202209144916044189917").step(100),"73745418")
        self.assertEqual(FFT("69317163492948606335995924319873").step(100),"52432133")
    
    def testRepeatAndShift(self):
        self.assertEqual(FFT("03036732577212944063491565474664", repeat=10_000).step(100),"84462026")
        self.assertEqual(FFT("02935109699940807407585447034323", repeat=10_000).step(100),"78725270")
        self.assertEqual(FFT("03081770884921959731165446850517", repeat=10_000).step(100),"53553731")

    

if __name__ == '__main__':
    unittest.main()