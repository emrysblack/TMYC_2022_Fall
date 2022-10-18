
def is_possible(possible):
    """
    takes a number and checks it against password rules
    1. 6 digits long
    2. must have at least 1 digit with more than 1 occurance
    3. no digits decreasing going from left to right
    """
    # get expected number for rule 3
    possible = str(possible)
    expected = list(possible)
    expected.sort()
    expected = ''.join(expected)

    # check against all 3 rules
    return len(possible) == 6 and len(set(possible)) < 6 and possible == expected

def is_possible_with_double(possible):
    """
    takes a number and checks it against password rules
    1. 6 digits long
    2. must have at least 1 digit with exactly 2 occurances
    3. no digits decreasing going from left to right
    """
    # get expected number for rule 3
    possible = str(possible)
    expected = list(possible)
    expected.sort()
    expected = ''.join(expected)
    # get number frequency for rule 2
    frequencies = [possible.count(i) for i in set(possible)]
    
    # check against all 3 rules
    return len(possible) == 6 and 2 in frequencies and possible == expected
    

def part1(min, max):
    possibles = (x for x in range(min,max+1) if is_possible(x))
    return len(list(possibles))

def part2(min, max):
    possibles = (x for x in range(min,max+1) if is_possible_with_double(x))
    return len(list(possibles))

def main():
    print("part 1: ", part1(357253,892942))
    print("part 2: ", part2(357253,892942))

if __name__ == "__main__":
    main()
