import re
from functools import reduce
from math import gcd
from itertools import count


def get_positions(moons: list[list[int]]) -> tuple[tuple[int],tuple[int],tuple[int]]:
    """
    rearranges moon positions grouped by x,y,z coordinates
    """
    return tuple(tuple(moons[j][i] for j in range(len(moons))) for i in range(3))

def get_gravity(moon_a: list[int], moon_b: list[int]) -> list[int]:
    """
    computes x,y,z pulls between two moons
    """
    gravity = [0,0,0]
    for index, (a,b) in enumerate(zip(moon_a, moon_b)):
        if a != b: gravity[index] += 1 if a < b else -1
    return gravity

def step_velocities(moons: list[list[int]], velocities: list[list[int]]) -> None:
    for index, moon_a in enumerate(moons):
        for moon_b in moons:
            velocities[index] = list(map(sum, zip(velocities[index], get_gravity(moon_a,moon_b))))

def step_positions(moons: list[list[int]], velocities: list[list[int]]) -> None:
    for i, (moon, speed) in enumerate(zip(moons,velocities)):
        for j, (p,s) in enumerate(zip(moon, speed)):
            moons[i][j] = p + s

def part1(moons: list[list[int]]):
    velocities = [[0,0,0]] * len(moons)
    for _ in range(1000):
        step_velocities(moons, velocities)
        step_positions(moons, velocities)

    pot = [sum(map(lambda item: abs(item), x)) for x in moons]
    kin = [sum(map(lambda item: abs(item), x)) for x in velocities]

    energy = sum(map(lambda x: x[0]*x[1], zip(pot,kin)))

    return energy

def part2(moons: list[list[int]]):
    # save starting positions to track orbits
    init_x, init_y, init_z = get_positions(moons)
    loops = {'x':0,'y':0,'z':0}
    velocities = [[0,0,0]] * len(moons)

    for i in count(1):
        step_velocities(moons, velocities)
        step_positions(moons, velocities)
        
        # see which positions have looped
        x,y,z = get_positions(moons)
        if not loops['x'] and x == init_x: loops['x'] = i + 1
        if not loops['y'] and y == init_y: loops['y'] = i + 1
        if not loops['z'] and z == init_z: loops['z'] = i + 1
        
        # go until we have found all position loops
        if 0 not in loops.values(): 
            # we need the least common multiple of the 3 loops so we know when
            # the positions will all loop at the same time
            return reduce(lambda x,y: int(abs(x*y) / gcd(x,y)), loops.values())

def read_orbit_file(path):
    # read in orbits
    with open(path, mode ='r') as file:
        # grab numbers in order from line
        return [list(map(int, re.findall("-?\\d+", s))) for s in file.readlines()]

def main():
    print("part 1: ", part1(read_orbit_file("week6/test_orbits.txt")))
    print("part 2: ", part2(read_orbit_file("week6/test_orbits.txt")))

if __name__ == "__main__":
    main()
