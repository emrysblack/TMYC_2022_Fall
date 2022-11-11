from itertools import chain
from typing import Union

# class var types
transmission = Union[list[int],None]
filepath = Union[str,None]
summation = list[list[range]]

class FlawedFrequencyTransmission():
    def __init__(self, data: transmission=None, path: filepath=None, repeat=1, shift=0) -> None:
        self._adds: summation = []
        self._subs: summation = []
        self._repeat = repeat
        self._shift = shift
        if data:
            self.data = data * self._repeat
        if path:
            self.__load_file(path)
        self._get_phase_transforms()

    def __load_file(self, path):
        with open(path, mode ='r') as file:
            self.data = [int(x) for x in file.read()] * self._repeat
            if self._shift:
                self._shift = int(''.join(map(str,self.data[:self._shift])))
    
    def _get_phase_transforms(self):
        """
        computes positive and negative positions for first half of inputs
        """
        self.data_length = len(self.data)
        for i in range(self._shift,int((self.data_length - self._shift) / 2)):
            self._adds.append([])
            self._subs.append([])
            for j in range(i,self.data_length,4*(i+1)): # start of addition indexes
                k = j+i+1+i+1 # start of subtraction indexes
                self._adds[i-self._shift].append(range(j-self._shift,min(j+i+1-self._shift, self.data_length-self._shift)))
                if k < self.data_length:
                    self._subs[i -self._shift].append(range(k-self._shift,min(k+i+1-self._shift, self.data_length-self._shift)))
        if self._shift:
            self.data = self.data[self._shift:]
    
    def step(self, steps:int) -> str:
        for _ in range(steps):
            # first half of signal
            for i, (adds, subs) in enumerate(zip(self._adds,self._subs)):
                add = sum(map(lambda x: sum(map(lambda y: self.data[y], x)), adds))
                sub = sum(map(lambda x: sum(map(lambda y: self.data[y], x)), subs))
                self.data[i] = int(str(add - sub)[-1])
            
            # second half of signal
            for i in range(len(self.data) - 2, len(self._adds) - 1, -1):
                self.data[i] = (self.data[i] + self.data[i+1]) % 10
        
        return ''.join(map(str,self.data[:8]))
    

def bonus1():
    fft = FlawedFrequencyTransmission(path="week5/bonus.txt")
    return fft.step(100)

def bonus2():
    fft = FlawedFrequencyTransmission(path="week5/bonus.txt", repeat=10_000, shift=7)
    return fft.step(100)

def main():  
    print("part 1: ", bonus1())
    print("part 2: ", bonus2())

if __name__ == "__main__":
    main()
