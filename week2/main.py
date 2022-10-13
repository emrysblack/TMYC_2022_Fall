from utils.csv_reader import import_csv_flat as read_csv
from utils.math import RightAngleMath as Math # we could use SymPy, but it's too slow here


def trace_wire(path):
    coordinates = [(0,0)]
    directions = {"U":(0,1), "D":(0,-1), "R":(1,0), "L":(-1,0)}
    x,y = (0,1)

    for segment in path:
        position = coordinates[-1]
        direction, magnitude = directions[segment[0]], int(segment[1:])
        next_position = (position[x]+direction[x] * magnitude, 
                         position[y]+direction[y] * magnitude)
        coordinates.append(next_position)
    
    return coordinates


def find_crossings(wire1, wire2):
    crossings = []

    for i in range(len(wire1)-1):
        for j in range(len(wire2)-1):
            if intersection := Math.intersects((wire1[i], wire1[i+1]),(wire2[j], wire2[j+1])):
                crossings.append(intersection)
    
    return crossings[1:] # exclude intersection at origin


def get_steps(intersection, points):    
    i = 0
    while not Math.contains((points[i], points[i+1]), intersection):
       yield Math.get_distance_manhattan(points[i], points[i+1])
       i += 1
    
    yield Math.get_distance_manhattan(points[i], intersection)


def part1():
    wire1 = trace_wire(read_csv('week2/wire1.csv'))
    wire2 = trace_wire(read_csv('week2/wire2.csv'))

    crossings = find_crossings(wire1, wire2)
    crossings.sort(key=lambda x: Math.get_distance_manhattan(x))

    return Math.get_distance_manhattan(crossings[0])


def part2():
    wire1 = trace_wire(read_csv('week2/wire1.csv'))
    wire2 = trace_wire(read_csv('week2/wire2.csv'))

    crossings = find_crossings(wire1, wire2)
    steps = [sum(get_steps(x, wire1)) + sum(get_steps(x, wire2)) for x in crossings]
    steps.sort()

    return steps[0]


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
