from utils.csv_reader import import_csv_flat


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

    # TODO: refactor into something cleaner and shorter
    
    # much more complicated working with lines than points, but also much faster
    for i in range(len(wire1)-1):
        for j in range(len(wire2)-1):
            # find low, mid, high points
            if wire1[i][0] == wire1[i+1][0]: # first line vertical
                mid1 = wire1[i][0]
                low_high1 = [wire2[j][0], wire2[j+1][0]]
                low_high1.sort()
                mid2 = wire2[j][1]
                low_high2 = [wire1[i][1], wire1[i+1][1]]
                low_high2.sort()
                if (mid1 >= low_high1[0] and mid1 <= low_high1[1] and
                    mid2 >= low_high2[0] and mid2 <= low_high2[1]):
                    crossings.append((mid1,mid2))
            else: # first line horizontal
                mid1 = wire1[i][1]
                low_high1 = [wire2[j][1], wire2[j+1][1]]
                low_high1.sort()
                mid2 = wire2[j][0]
                low_high2 = [wire1[i][0], wire1[i+1][0]]
                low_high2.sort()
                if (mid1 >= low_high1[0] and mid1 <= low_high1[1] and
                    mid2 >= low_high2[0] and mid2 <= low_high2[1]):
                    crossings.append((mid2,mid1))

    return crossings[1:]


def get_distance_manhattan(coord, origin=None):
    if origin is None:
        origin=(0,0)
    # pair coordinates with origin
    x,y = ([origin[0],coord[0]],[origin[1],coord[1]])

    # reorder for max/min
    x.sort()
    y.sort()

    # get absolute distance
    return x[1] - x[0] + y[1] - y[0]

def get_intersection_steps(intersection, wire):

    # is point on the line?
    def contains(point, start, end):
        x = [start[0], end[0]]
        y = [start[1], end[1]]
        x.sort()
        y.sort()
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
    steps = [sum(get_intersection_steps(step, wire1)) + sum(get_intersection_steps(step, wire2)) for step in crossings]
    steps.sort()

    return steps[0]

def main():
    print("part 1: ", part1())
    print("part 2: ", part2())

if __name__ == "__main__":
    main()
