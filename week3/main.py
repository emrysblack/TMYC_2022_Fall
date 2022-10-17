
def is_possible(number):
    # prep data for comparisons
    number = str(number)
    possible = list(number)
    possible.sort()
    possible = ''.join(possible)

    return len(possible) == 6 and len(set(possible)) < 6 and possible == number

def is_possible_with_double(number):
    # prep data for comparisons
    number = str(number)
    possible = list(number)
    possible.sort()
    possible = ''.join(possible)
    frequencies = [possible.count(i) for i in set(possible)]

    return len(possible) == 6 and 2 in frequencies and possible == number
    

def part1():
    min, max = 357253,892942
    possibles = (x for x in range(min,max+1) if is_possible(x))
    return len(list(possibles))

def part2():
    min, max = 357253,892942
    possibles = (x for x in range(min,max+1) if is_possible_with_double(x))
    return len(list(possibles))

def main():
    print("part 1: ", part1())
    print("part 2: ", part2())

if __name__ == "__main__":
    main()
