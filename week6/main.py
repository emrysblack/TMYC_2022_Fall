import re
from functools import reduce
from math import gcd
import copy

# complex type
positionList = tuple[tuple[int],tuple[int],tuple[int]]

class Orbits:
    def __init__(self, path) -> None:
         self._read_orbit_file(path)
         self.vel = [[0,0,0]] * len(self.moons)
    
    def _read_orbit_file(self, path) -> None:
        # read in orbits
        with open(path, mode ='r') as file:
            # grab numbers in order from line
            self.moons = [list(map(int, re.findall("-?\\d+", s))) for s in file.readlines()]
    
    @property
    def potential_energy(self) -> list[int]:
        return [sum(map(lambda item: abs(item), x)) for x in self.moons]
    
    @property
    def kinetic_energy(self) -> list[int]:
        return [sum(map(lambda item: abs(item), x)) for x in self.vel]

    @property
    def _positions(self) -> positionList:
        """
        rearranges moon positions grouped by x,y,z coordinates
        """
        return tuple(tuple(self.moons[j][i] for j in range(len(self.moons))) for i in range(3))
    
    @property
    def orbital_loops(self):
        """
        returns orbital loop periods for x,y,z of current system
        restores state afterward so can be used without side-effects
        """
        # save current state
        moons = copy.deepcopy(self.moons)
        vel = copy.deepcopy(self.vel)
        # save starting positions to track orbits
        init_x, init_y, init_z = self._positions
        loops = {'x':0,'y':0,'z':0}

        i = 1
        while 0 in loops.values(): # go until we have found all position loops
            self.step()
            
            # see which positions have looped
            x,y,z = self._positions
            if not loops['x'] and x == init_x: loops['x'] = i + 1
            if not loops['y'] and y == init_y: loops['y'] = i + 1
            if not loops['z'] and z == init_z: loops['z'] = i + 1
            i+=1
        
        # restore state
        self.moons = moons
        self.vel = vel

        return loops.values()
        
    @staticmethod
    def get_gravity(moon_a: list[int], moon_b: list[int]) -> list[int]:
        """
        computes x,y,z pull between two moons
        """
        gravity = [0,0,0]
        for index, (a,b) in enumerate(zip(moon_a, moon_b)):
            if a != b: gravity[index] += 1 if a < b else -1
        return gravity
    
    def _step_velocities(self) -> None:
        """
        computes moons velocities based on gravtitational pull between moons
        """
        for index, moon_a in enumerate(self.moons):
            for moon_b in self.moons: # modify velocity by gravity pull between moons
                self.vel[index] = list(map(sum, zip(self.vel[index], self.get_gravity(moon_a,moon_b))))

    def _step_positions(self) -> None:
        """
        updates moon positions based on current moon velocity
        """
        for i, (moon, speed) in enumerate(zip(self.moons,self.vel)):
            for j, (position,velocity) in enumerate(zip(moon, speed)):
                self.moons[i][j] = position + velocity
    
    def step(self, steps=1):
        for _ in range(steps):
            self._step_velocities()
            self._step_positions()


def part1(path: str):
    """
    computes total energy in an orbital system after 1000 cycles
    """
    orbits = Orbits(path)
    orbits.step(1000)

    energy = sum(map(lambda x: x[0]*x[1], zip(orbits.potential_energy,orbits.kinetic_energy)))

    return energy

def part2(path: str):
    """
    computes number of cycles before a reset on an orbital system
    """
    orbits = Orbits(path)
    orbital_loops = orbits.orbital_loops

    # we need the least common multiple of the 3 loops so we know when
    # the positions will all loop at the same time
    return reduce(lambda x,y: int(abs(x*y) / gcd(x,y)), orbital_loops)

def main():
    moons_file = "week6/test_orbits.txt"
    print("part 1: ", part1(moons_file))
    print("part 2: ", part2(moons_file))

if __name__ == "__main__":
    main()
