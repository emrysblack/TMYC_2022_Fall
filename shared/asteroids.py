from itertools import chain
from math import gcd, atan2, degrees, pi

class Asteroids():
    def __init__(self, asteroids):
        self.asteroids = asteroids
        self.asteroid_positions = [index for (index, item) in enumerate(list(chain(*asteroids))) if item == "#"]
        self.width, self.height = len(asteroids[0]), len(asteroids)

        # math helper functions
        self.get_index = lambda x,y: self.width * y + x
        self.get_coordinates = lambda i: (i % self.width, int(i / self.width))
        self.valid_coord = lambda x,y: y >= 0 and x >= 0 and x < self.width and self.get_index(x,y) < self.width * self.height

    def _get_slope(a,b):
            x,y = b[0] - a[0], b[1] - a[1]
            div = gcd(x,y)
            x /= div
            y /= div
            return (int(x), int(y))
    
    def _angle_between(p1, p2):
        ang1 = atan2(*p1[::-1])
        ang2 = atan2(*p2[::-1])
        return degrees((ang1 - ang2) % (2 * pi))
    
    def get_visibility(self, positions: list, index: int) -> list:
        get_distance = lambda a,b: (max(b[0], a[0]) - min(b[0],a[0])) + (max(b[1],a[1]) - min(b[1],a[1]))
        # get distances for each asteroid from target
        asteroids = dict(zip(positions, map(lambda k: get_distance(self.get_coordinates(index), self.get_coordinates(k)), positions)))
        asteroids.pop(index) # cannot see ourselves
        visible = []
        while(len(asteroids)):
            # find closest asteroid
            x,y = self.get_coordinates(list(asteroids.keys())[list(asteroids.values()).index(min(asteroids.values()))])
            dx, dy = Asteroids._get_slope(self.get_coordinates(index), (x,y))
            visible.append((x,y))
            
            # hide all asteroids behind it
            while(self.valid_coord(x,y)):
                if (i := self.get_index(x,y)) in asteroids:
                    asteroids.pop(i)
                y += dy
                x += dx
        
        return visible

    def get_visibility_map(self):
        visibility_map = list(chain(*self.asteroids))
        for position in self.asteroid_positions:
            visibility_map[position] = str(len(self.get_visibility(self.asteroid_positions.copy(), position)))

        return visibility_map
    
    def fire_laser(self, outpost):

        def target_asteroids(rock):
            """
            gets targeting order of a single asteroid by computing
            the vertical angle between it and the outpost station firing
            the laser
            """
            # adjust points to origin
            origin = self.get_coordinates(outpost)
            laser = (origin[0], 0) # straight up from outpost
            laser = (laser[0] - origin[0], -(laser[1] - origin[1]))
            rock = (rock[0] - origin[0], -(rock[1] - origin[1]))
            return Asteroids._angle_between(laser, rock)

        destroyed = []
        asteroid_positions = self.asteroid_positions.copy()

        # keep shooting until all asteroids have been destroyed
        while len(visible := self.get_visibility(asteroid_positions.copy(), outpost)):
            visible.sort(key=target_asteroids) # get lock-on asteroids
            for rock in visible: # destroy asteroids
                asteroid_positions.remove(self.get_index(*rock))
            destroyed.extend(visible)

        return destroyed
