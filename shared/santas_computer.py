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


    # mode helper function
    def __get_args(self, moded = 0, normal = 0):
        # mode flags
        mode = str(self.codes[self.ptr]).zfill(moded+2)[-3::-1]
        m = self.codes[self.ptr+1:self.ptr+moded+1] # get moded arguments
        n = self.codes[self.ptr+moded+1:self.ptr+moded+normal+1] # get non-moded arguments
        self.ptr += moded + normal + 1 # increment pointer over args
        args = list(map(lambda x, y: x if y == '1' else self.codes[x], m, mode))
        args.extend(n)
        return args

    # computer functions 
    def __add(self):
        x,y,out = self.__get_args(2,1)
        self.codes[out] = x + y

    def __mul(self):
        x,y,out = self.__get_args(2,1)
        self.codes[out] = x * y

    def __prompt(self):
        out, = self.__get_args(normal=1)
        self.codes[out] = int(input())
    
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
        x,y,out = self.__get_args(2,1)
        self.codes[out] = int(x < y)

    def __equal(self):
        x,y,out = self.__get_args(2,1)
        self.codes[out] = int(x == y)
    
    def __quit(self):
        self.quit = True
 
