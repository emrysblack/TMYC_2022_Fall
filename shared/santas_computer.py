class ShipComputer:
    def __init__(self, codes) -> None:
        self.codes = codes
        self.ptr = 0
        self.quit = False

        # assign computer functions to codes
        self._optcodes = { 1: self.__add, 2: self.__mul, 3: self.__prompt, 4: self.__output, 
                          5: self.__jump_if_true, 6: self.__jump_if_false, 
                          7: self.__less_than, 8: self.__equal, 99: self.__quit }
    
    def execute(self):
        while not self.quit:
            self._optcodes[self.codes[self.ptr]%100]()


    # helper functions
    def __get_args(self, argc):
        # mode flags
        mode = str(self.codes[self.ptr]).zfill(argc+2)[-3::-1]
        args = self.codes[self.ptr+1:self.ptr+argc+1] # get moded arguments
        self.ptr += argc + 1 # increment pointer over args
        return list(map(lambda x, y: x if y == '1' else self.codes[x], args, mode))
    
    def __assign(self, value):
        out = self.codes[self.ptr]
        self.codes[out] = value
        self.ptr += 1
    
    def __input(self):
        self.ptr += 1
        return int(input())

    # computer functions 
    def __add(self):
        x,y = self.__get_args(2)
        self.__assign(x+y)

    def __mul(self):
        x,y = self.__get_args(2)
        self.__assign(x*y)

    def __prompt(self):
        x = self.__input()
        self.__assign(x)
    
    def __output(self):
        x, = self.__get_args(1)
        print(x)

    def __jump_if_true(self):
        x,y = self.__get_args(2)
        if x != 0: self.ptr = y

    def __jump_if_false(self):
        x,y = self.__get_args(2)
        if x == 0: self.ptr = y
    
    def __less_than(self):
        x,y = self.__get_args(2)
        self.__assign(int(x < y))

    def __equal(self):
        x,y = self.__get_args(2)
        self.__assign(int(x == y))
    
    def __quit(self):
        self.quit = True
