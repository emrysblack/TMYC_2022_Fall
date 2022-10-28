"""
Library for various graphing calculations
that assumes line segments without diagonals
"""
class RightAngleMath():
    @staticmethod
    def intersects(line1, line2):
        """
        returns coordinates of intersection of lines
        or False if no intersection exists
        """
        is_vertical = line1[0][0] == line1[1][0] # first line vertical?

         # find low, mid, high points
        mid1 = line1[0][int(not is_vertical)]
        low1, high1 = sorted([line2[0][int(not is_vertical)], line2[1][int(not is_vertical)]])
            
        # find low, mid, high points
        mid2 = line2[0][int(is_vertical)]
        low2, high2 = sorted([line1[0][int(is_vertical)], line1[1][int(is_vertical)]])

        # does midpoint intersect
        if (mid1 >= low1 and mid1 <= high1 and
            mid2 >= low2 and mid2 <= high2):
                return (mid1,mid2) if is_vertical else (mid2,mid1)
        return False

    @staticmethod
    def contains(line, point):
        """
        returns True if point is on the line
        """
        start,end = line[0], line[1]
        x,y = sorted([start[0], end[0]]), sorted([start[1], end[1]])

        if start[0] == end[0]:
            return point[0] == start[0] and point[1] >= y[0] and point[1] <= y[1]
        return point[1] == start[1] and point[0] >= x[0] and point[0] <= x[1]
    
    @staticmethod
    def get_distance_manhattan(coord, origin=None):
        """
        returns taxicab distance between two points
        if no second point is given, (0,0) is assumed
        """
        if origin is None:
            origin=(0,0)
        # pair coordinates with origin
        x,y = sorted([origin[0],coord[0]]),sorted([origin[1],coord[1]])

        # get absolute distance
        return x[1] - x[0] + y[1] - y[0]