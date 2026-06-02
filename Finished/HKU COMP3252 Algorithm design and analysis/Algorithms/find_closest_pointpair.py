from math import sqrt
from find_kth import find_approximate_median

data = [
    (1.2, 4.5), (7.8, 2.3), (3.4, 6.7), (9.1, 0.9), (5.5, 5.5),
    (2.1, 4.6), (8.0, 2.5), (3.6, 6.8), (0.5, 1.2), (6.3, 7.1),
    (4.4, 3.3), (9.9, 8.8), (1.0, 1.1), (7.2, 6.4), (2.9, 5.0),
    (8.7, 3.2), (5.0, 2.0), (3.1, 9.0), (6.6, 1.8), (4.0, 4.0),
    (0.8, 1.0), (7.5, 7.6), (2.5, 2.6), (9.3, 4.7), (5.8, 5.9),
    (1.9, 4.4), (8.2, 8.1), (3.3, 3.4), (6.9, 0.6), (4.8, 6.0), 
]



def find_closest_pointpair(points, axis = 0):
    def dist(a,b):
        return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    def brute(points):
        min_dist = float('inf')
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                min_dist = min(min_dist, dist(points[i], points[j]))
        return min_dist
    if len(points) < 5:
        return brute(points)
    coordinates = [points[i][axis] for i in range(len(points))]
    pivot = find_approximate_median(coordinates)
    L, Miss, R = [], [], []
    for point in points:
        if point[axis] <= pivot:
            L += [point]
        else:
            R += [point]
    min_dist = min(find_closest_pointpair(L, (axis + 1) % 2), find_closest_pointpair(R, (axis + 1) % 2))
    for point in R:
        if point[axis] - pivot <= min_dist:
            Miss += [point]
    for point in L:
        if pivot - point[axis] <= min_dist:
            Miss += [point]
    return min(min_dist, brute(Miss))

print(find_closest_pointpair(data))