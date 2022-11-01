def get_ancestors(x, data):
    while x in data:
        yield x
        x = data[x]
    yield x

def get_common_ancestor(a,b,data):
    # make ancestor maps
    a_map = [x for x in get_ancestors(a,data)][::-1]
    b_map = [x for x in get_ancestors(b,data)][::-1]

    # find closest ancestor
    return [x for x,y in zip(a_map,b_map) if x == y][-1]

def get_orbits(key, data, total = 0):
    if key not in data:
        return total
    return get_orbits(data[key], data, total + 1)
    

def part1(data):
    return sum(get_orbits(orbit, data) for orbit in data)

def part2(data):
    # get ancestor distance
    ancestor = get_orbits(get_common_ancestor("YOU","SAN", data), data)
    # get distance of parents
    distance = (get_orbits(data["YOU"], data) - ancestor) + (get_orbits(data["SAN"], data) - ancestor)
    return distance

def read_orbit_file(path):
    # read in orbits
    data = {}
    with open(path, mode ='r') as file:
        for line in file.readlines():
            rock, orbits = line.strip().split(")")
            data[orbits] = rock
    return data

def main():
    data = read_orbit_file("week5/orbits.txt")    
    print("part 1: ", part1(data))
    print("part 2: ", part2(data))

if __name__ == "__main__":
    main()
