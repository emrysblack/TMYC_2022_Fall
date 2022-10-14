class ShipComputer:
    def __init__(self, codes) -> None:
        self.codes = codes
        self._ptr = 0
        self._quit = False

        # assign computer functions to codes
        self._optcodes = { 1: self.__add, 2: self.__mul, 3: self.__prompt, 4: self.__output, 
                          5: self.__jump_if_true, 6: self.__jump_if_false, 
                          7: self.__less_than, 8: self.__equal, 99: self.__quit }
    
    def execute(self):
        while not self._quit:
            self._optcodes[self.codes[self._ptr]%100]()
    
    # mode helper function
    def __get_args_with_mode(self, argc):
        args = self.codes[self._ptr+1:self._ptr+argc+1] # get instruction
        # mode
        mode = str(self.codes[self._ptr]).zfill(argc+2)[-3::-1]
        return list(map(lambda x, y: x if y == '1' else self.codes[x], args, mode))

    # computer functions 
    def __add(self):
        x,y = self.__get_args_with_mode(2)
        out = self.codes[self._ptr + 3]

        self.codes[out] = x + y
        self._ptr += 4
    
    def __mul(self):
        x,y = self.__get_args_with_mode(2)
        out = self.codes[self._ptr + 3]

        self.codes[out] = x * y
        self._ptr += 4
    
    def __prompt(self):
        out = self.codes[self._ptr+1]
        self.codes[out] = int(input())
        self._ptr += 2
    
    def __output(self):
        x, = self.__get_args_with_mode(1)
        print(x)
        self._ptr += 2

    def __jump_if_true(self):
        x,y = self.__get_args_with_mode(2)
        self._ptr += y - self._ptr if x != 0 else 3

    def __jump_if_false(self):
        x,y = self.__get_args_with_mode(2)
        self._ptr += y - self._ptr if x == 0 else 3
    
    def __less_than(self):
        x,y = self.__get_args_with_mode(2)
        out = self.codes[self._ptr + 3]

        self.codes[out] = int(x < y)
        self._ptr += 4
    
    def __equal(self):
        x,y = self.__get_args_with_mode(2)
        out = self.codes[self._ptr + 3]

        self.codes[out] = int(x == y)
        self._ptr += 4
    
    def __quit(self):
        self._quit = True
 
