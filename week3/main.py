"""
composable password check rules
"""
def six_digits(possible: str) -> bool: # six digits long
    return len(possible) == 6

def increasing(possible: str) -> bool: # no digits decreasing from left to right
    return possible == ''.join(sorted(possible))

def has_duplicates(possible: str) -> bool: # has a repeating value
    return len(set(possible)) < len(possible)

def has_double(possible: str) -> bool: # has exactly 2 of a value
    return 2 in [possible.count(i) for i in set(possible)]

def check(possible: str, *rules) -> bool:
    """
    checks a possible password against all given rules
    """
    return all(map(lambda x: x(possible), rules))
    

def part1(min: int, max: int) -> int:
    possibles = (x for x in range(min,max+1) if check(str(x), six_digits, increasing, has_duplicates))    
    return len(list(possibles))

def part2(min: int, max: int) -> int:
    possibles = (x for x in range(min,max+1) if check(str(x), six_digits, increasing, has_double))    
    return len(list(possibles))

def main():
    print("part 1: ", part1(357253,892942))
    print("part 2: ", part2(357253,892942))

if __name__ == "__main__":
    main()
