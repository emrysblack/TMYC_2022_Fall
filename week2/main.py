from utils.csv_reader import import_csv_flat
"""
For simplicity and readability we could use SymPy, but it's just way too slow for this application
"""

def trace_wire(path):
    coordinates = [(0,0)]
    directions = {"U":(0,1), "D":(0,-1), "R":(1,0), "L":(-1,0)}

    for segment in path:
        last_position = coordinates[-1]
        direction = directions[segment[0]]
        magnitude = int(segment[1:])
        next_position = (last_position[0]+direction[0] * magnitude, 
                         last_position[1]+direction[1] * magnitude)
        coordinates.append(next_position)
    return coordinates

def find_crossings(wire1, wire2):
    crossings = []

    # much more complicated working with lines than points, but also much faster
    for i in range(len(wire1)-1):
        for j in range(len(wire2)-1):
            
            is_vertical = wire1[i][0] == wire1[i+1][0] # first line vertical?

            # find low, mid, high points
            mid1 = wire1[i][int(not is_vertical)]
            low_high1 = [wire2[j][int(not is_vertical)], wire2[j+1][int(not is_vertical)]]
            
            # find low, mid, high points
            mid2 = wire2[j][int(is_vertical)]
            low_high2 = [wire1[i][int(is_vertical)], wire1[i+1][int(is_vertical)]]
            
            low_high1.sort(), low_high2.sort()
            low1, high1 = low_high1
            low2, high2 = low_high2

            # does midpoint intersect
            if (mid1 >= low1 and mid1 <= high1 and
                mid2 >= low2 and mid2 <= high2):
                crossings.append((mid1,mid2) if is_vertical else (mid2,mid1))

    return crossings[1:]


def get_distance_manhattan(coord, origin=None):
    if origin is None:
        origin=(0,0)
    # pair coordinates with origin
    x,y = ([origin[0],coord[0]],[origin[1],coord[1]])

    # reorder for max/min
    x.sort(), y.sort()

    # get absolute distance
    return x[1] - x[0] + y[1] - y[0]

def get_steps(intersection, wire):

    # is point on the line?
    def contains(point, start, end):
        x = [start[0], end[0]]
        y = [start[1], end[1]]
        x.sort(), y.sort()
        if start[0] == end[0]:
            return point[0] == start[0] and point[1] >= y[0] and point[1] <= y[1]
        return point[1] == start[1] and point[0] >= x[0] and point[0] <= x[1]
    
    i = 0
    while not contains(intersection, wire[i], wire[i+1]):
       yield get_distance_manhattan(wire[i], wire[i+1])
       i += 1
    
    yield get_distance_manhattan(intersection, wire[i])


def part1():
    wire1 = trace_wire(import_csv_flat('week2/wire1.csv'))
    wire2 = trace_wire(import_csv_flat('week2/wire2.csv'))

    crossings = find_crossings(wire1, wire2)
    crossings.sort(key=lambda x: get_distance_manhattan(x))
    return get_distance_manhattan(crossings[0])

def part2():
    wire1 = trace_wire(import_csv_flat('week2/wire1.csv'))
    wire2 = trace_wire(import_csv_flat('week2/wire2.csv'))

    crossings = find_crossings(wire1, wire2)
    steps = [sum(get_steps(step, wire1)) + sum(get_steps(step, wire2)) for step in crossings]
    steps.sort()

    return steps[0]

def main():
    print("part 1: ", part1())
    print("part 2: ", part2())

if __name__ == "__main__":
    main()
