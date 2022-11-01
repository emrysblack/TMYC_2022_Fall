def get_ancestors(x, data):
    while x in data:
        yield x
        x = data[x]
    yield x

def get_common_ancestor(a,b,data):
    # get ancestor paths
    a_path = reversed(list(get_ancestors(a,data)))
    b_path = reversed(list(get_ancestors(b,data)))

    # find closest ancestor
    return [x for x,y in zip(a_path,b_path) if x == y][-1]

def get_orbits(key, data):
    return len(list(get_ancestors(key,data))) - 1 # root has no orbits


def part1(data):
    return sum(get_orbits(orbit, data) for orbit in data)

def part2(data):
    # get parent and ancestor distances
    you = get_orbits(data["YOU"], data)
    santa = get_orbits(data["SAN"], data)
    ancestor = get_orbits(get_common_ancestor("YOU","SAN", data), data)
    # adjust distance to ancestor
    distance = you - ancestor + santa - ancestor
    return distance

def read_orbit_file(path):
    # read in orbits
    with open(path, mode ='r') as file:
        return {orbits:rock for rock,orbits in (line.strip().split(")") for line in file.readlines())}

def main():
    data = read_orbit_file("week5/orbits.txt")    
    print("part 1: ", part1(data))
    print("part 2: ", part2(data))

if __name__ == "__main__":
    main()
