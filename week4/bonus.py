from shared.file_reader import read_chars_multiple_lines as file_read
from shared.asteroids import Asteroids


def bonus1():
    visibility = Asteroids(file_read('week4/asteroids.txt')).get_visibility_map()
    return max(visibility)

def bonus2():
    asteroids = Asteroids(file_read('week4/asteroids.txt'))
    visibility = asteroids.get_visibility_map()

    outpost = visibility.index(max(visibility))
    asteroids_destroyed = asteroids.fire_laser(outpost)
    x,y = asteroids_destroyed[199] # 200th asteroid

    return x * 100 + y

def main():
    print("bonus1: ", bonus1())
    print("bonus2: ", bonus2())

if __name__ == "__main__":
    main()