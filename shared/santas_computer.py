class ShipComputer:
    def __init__(self, codes) -> None:
        self.codes = codes
        self.ptr = -1 # not started
        self.quit = False

        # assign computer functions to codes
        self._optcodes = { 1: self.__add, 2: self.__mul, 3: self.__prompt, 4: self.__output, 
                          5: self.__jump_if_true, 6: self.__jump_if_false, 
                          7: self.__less_than, 8: self.__equal, 99: self.__quit }
    
    def execute(self):
        while not self.quit:
            self._optcodes[self.codes[self.__ptr]%100]()
    
    @property
    def __ptr(self):
        """
        increments program pointer like ++
        so functions are always in sync with program
        when dealing with arguments
        """
        self.ptr += 1
        return self.ptr 


    # mode helper function
    def __get_args_with_mode(self, argc):
        args = self.codes[self.ptr+1:self.ptr+argc+1] # get instruction
        # mode
        mode = str(self.codes[self.ptr]).zfill(argc+2)[-3::-1]
        self.ptr += argc # increment pointer over args
        return list(map(lambda x, y: x if y == '1' else self.codes[x], args, mode))

    # computer functions 
    def __add(self):
        x,y = self.__get_args_with_mode(2)
        out = self.codes[self.__ptr]
        self.codes[out] = x + y

    def __mul(self):
        x,y = self.__get_args_with_mode(2)
        out = self.codes[self.__ptr]
        self.codes[out] = x * y

    def __prompt(self):
        out = self.codes[self.__ptr]
        self.codes[out] = int(input())
    
    def __output(self):
        x, = self.__get_args_with_mode(1)
        print(x)

    def __jump_if_true(self):
        x,y = self.__get_args_with_mode(2)
        if x != 0: self.ptr = y - 1

    def __jump_if_false(self):
        x,y = self.__get_args_with_mode(2)
        if x == 0: self.ptr = y - 1 
    
    def __less_than(self):
        x,y = self.__get_args_with_mode(2)
        out = self.codes[self.__ptr]
        self.codes[out] = int(x < y)

    def __equal(self):
        x,y = self.__get_args_with_mode(2)
        out = self.codes[self.__ptr]
        self.codes[out] = int(x == y)
    
    def __quit(self):
        self.quit = True
 
