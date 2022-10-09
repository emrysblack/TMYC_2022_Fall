PROBLEM = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,10,19,23,2,9,23,27,1,6,27,31,1,10,31,35,1,35,10,39,1,9,39,43,1,6,43,47,1,10,47,51,1,6,51,55,2,13,55,59,1,6,59,63,1,10,63,67,2,67,9,71,1,71,5,75,1,13,75,79,2,79,13,83,1,83,9,87,2,10,87,91,2,91,6,95,2,13,95,99,1,10,99,103,2,9,103,107,1,107,5,111,2,9,111,115,1,5,115,119,1,9,119,123,2,123,6,127,1,5,127,131,1,10,131,135,1,135,6,139,1,139,5,143,1,143,9,147,1,5,147,151,1,151,13,155,1,5,155,159,1,2,159,163,1,163,6,0,99,2,0,14,0]
DIAGNOSTIC = [3,225,1,225,6,6,1100,1,238,225,104,0,1002,43,69,224,101,-483,224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,1101,67,60,225,1102,5,59,225,1101,7,16,225,1102,49,72,225,101,93,39,224,101,-98,224,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,1102,35,82,225,2,166,36,224,101,-4260,224,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,102,66,48,224,1001,224,-4752,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1001,73,20,224,1001,224,-55,224,4,224,102,8,223,223,101,7,224,224,1,223,224,223,1102,18,41,224,1001,224,-738,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,1101,68,71,225,1102,5,66,225,1101,27,5,225,1101,54,63,224,1001,224,-117,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1,170,174,224,101,-71,224,224,4,224,1002,223,8,223,1001,224,4,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1007,226,226,224,1002,223,2,223,1006,224,329,1001,223,1,223,1007,226,677,224,102,2,223,223,1006,224,344,1001,223,1,223,108,677,677,224,102,2,223,223,1005,224,359,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,374,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,389,101,1,223,223,7,226,226,224,1002,223,2,223,1005,224,404,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,419,1001,223,1,223,8,226,677,224,1002,223,2,223,1005,224,434,101,1,223,223,1008,226,677,224,102,2,223,223,1006,224,449,1001,223,1,223,7,226,677,224,1002,223,2,223,1006,224,464,1001,223,1,223,108,677,226,224,102,2,223,223,1005,224,479,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,494,101,1,223,223,8,226,226,224,1002,223,2,223,1005,224,509,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,1107,226,226,224,102,2,223,223,1005,224,539,1001,223,1,223,1108,677,677,224,1002,223,2,223,1006,224,554,101,1,223,223,107,226,677,224,102,2,223,223,1005,224,569,1001,223,1,223,1108,226,677,224,1002,223,2,223,1005,224,584,1001,223,1,223,1107,226,677,224,1002,223,2,223,1005,224,599,1001,223,1,223,1008,226,226,224,1002,223,2,223,1005,224,614,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,629,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,644,101,1,223,223,107,677,677,224,1002,223,2,223,1005,224,659,101,1,223,223,1108,677,226,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226]

class ShipComputer:
    def __init__(self, codes) -> None:
        self.codes = codes
        self.ptr = 0

        # assign computer functions to codes
        self.optcodes = { 1: self.add, 2: self.mul, 3: self.prompt, 4: self.output, 
                          5: self.jump_if_true, 6: self.jump_if_false, 
                          7: self.less_than, 8: self.equal }
    
    def execute(self):
        while (self.codes[self.ptr] != 99): # 99 quit code
            self.optcodes[self.codes[self.ptr]%100]()
    
    # mode helper function
    def get_args_with_mode(self, argc):
        args = self.codes[self.ptr+1:self.ptr+argc+1] # get instruction
        # mode
        mode = str(self.codes[self.ptr]).zfill(argc+2)[-3::-1]
        return list(map(lambda x, y: x if y == '1' else self.codes[x], args, mode))

    # computer functions 
    def add(self):
        x,y = self.get_args_with_mode(2)
        out = self.codes[self.ptr + 3]

        self.codes[out] = x + y
        self.ptr += 4
    
    def mul(self):
        x,y = self.get_args_with_mode(2)
        out = self.codes[self.ptr + 3]

        self.codes[out] = x * y
        self.ptr += 4
    
    def prompt(self):
        out = self.codes[self.ptr+1]
        self.codes[out] = int(input())
        self.ptr += 2
    
    def output(self):
        x, = self.get_args_with_mode(1)
        print(x)
        self.ptr += 2

    def jump_if_true(self):
        x,y = self.get_args_with_mode(2)
        self.ptr += y - self.ptr if x != 0 else 3

    def jump_if_false(self):
        x,y = self.get_args_with_mode(2)
        self.ptr += y - self.ptr if x == 0 else 3
    
    def less_than(self):
        x,y = self.get_args_with_mode(2)
        out = self.codes[self.ptr + 3]

        self.codes[out] = int(x < y)
        self.ptr += 4
    
    def equal(self):
        x,y = self.get_args_with_mode(2)
        out = self.codes[self.ptr + 3]

        self.codes[out] = int(x == y)
        self.ptr += 4
 

def part1():
    computer = ShipComputer(PROBLEM.copy())
    computer.codes[1] = 12
    computer.codes[2] = 2

    computer.execute()
    return computer.codes[0]

def part2():
    for i in range(100):
        for j in range(100):
            computer = ShipComputer(PROBLEM.copy())
            computer.codes[1] = i
            computer.codes[2] = j

            computer.execute()
            if computer.codes[0] == 19690720:
                return 100 * i + j
    return "Not Found"

def bonus1():
    # enter 1
    computer = ShipComputer(DIAGNOSTIC.copy())
    computer.execute()

def bonus2():
    # enter 5
    computer = ShipComputer(DIAGNOSTIC.copy())
    computer.execute()


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())

    print("bonus 1 (Enter 1): ")
    bonus1()
    
    print("bonus 2 (Enter 5): ")
    bonus2()

if __name__ == "__main__":
    main()
