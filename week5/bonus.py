class FlawedFrequencyTransmission():
    def __init__(self, data: str, repeat=1) -> None:
        self._adds: list[list[range]] = []
        self._subs: list[list[range]] = []
        self.data = (self.__load_file(data) if not data.isdigit() else [int(x) for x in data]) * repeat
        shift = int(''.join(map(str,self.data[:7]))) if repeat > 1 else 0
        
        self._get_phase_transforms(shift)

    def __load_file(self, path: str) -> list[int]:
        with open(path, mode ='r') as file:
            return [int(x) for x in file.read()]
    
    def _get_phase_transforms(self, shift:int) -> None:
        """
        computes positive and negative positions for first half of inputs
        """
        self.data_length = len(self.data)
        for i in range(shift,int((self.data_length - shift) / 2)):
            self._adds.append([])
            self._subs.append([])
            for j in range(i,self.data_length,4*(i+1)): # start of addition indexes
                k = j+i+1+i+1 # start of subtraction indexes
                self._adds[i-shift].append(range(j-shift,min(j+i+1-shift, self.data_length-shift)))
                if k < self.data_length:
                    self._subs[i -shift].append(range(k-shift,min(k+i+1-shift, self.data_length-shift)))
        self.data = self.data[shift:]

    def _run_phase(self) -> None:
        # first half of signal
        for i, (adds, subs) in enumerate(zip(self._adds,self._subs)):
            add = sum(sum(map(lambda idx: self.data[idx], x)) for x in adds)
            sub = sum(sum(map(lambda idx: self.data[idx], x)) for x in subs)
            self.data[i] = int(str(add - sub)[-1]) # last digit without sign
            
        # second half of signal
        for i in range(len(self.data) - 2, len(self._adds) - 1, -1):
            self.data[i] = (self.data[i] + self.data[i+1]) % 10 # last digit

    def step(self, steps:int=1) -> str:
        for _ in range(steps):
            self._run_phase()
        
        return ''.join(map(str,self.data[:8]))
    

def bonus1():
    fft = FlawedFrequencyTransmission("week5/bonus.txt")
    return fft.step(100)

def bonus2():
    fft = FlawedFrequencyTransmission("week5/bonus.txt", repeat=10_000)
    return fft.step(100)

def main():  
    print("part 1: ", bonus1())
    print("part 2: ", bonus2())

if __name__ == "__main__":
    main()
