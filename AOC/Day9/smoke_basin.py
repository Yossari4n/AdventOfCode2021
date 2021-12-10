import numpy as np
from functools import reduce


def smoke_basin():
    with open('Day9/input.txt', 'r') as file:
        data = " ".join(file.read().rstrip()).replace('\n', ';')
        heightmap = np.matrix(data)

        score1 = 0
        for point in find_low_points(heightmap):
            score1 += heightmap[point[0], point[1]] + 1

        score2 = 1
        for point in find_largest_basins(heightmap)[-3:]:
            score2 *= len(point)

        return score1, score2


def get_adjacent_indices(index, heightmap):
    result = []
    if index[0] - 1 >= 0:
        result.append(tuple([index[0] - 1, index[1]]))
    if index[1] - 1 >= 0:
        result.append(tuple([index[0], index[1] - 1]))
    if index[0] + 1 < heightmap.shape[0]:
        result.append(tuple([index[0] + 1, index[1]]))
    if index[1] + 1 < heightmap.shape[1]:
        result.append(tuple([index[0], index[1] + 1]))
    return result


def get_adjacent(index, heightmap):
    values = []
    for adjacent_index in get_adjacent_indices(index, heightmap):
        values.append(heightmap[adjacent_index[0], adjacent_index[1]])
    return values


def find_low_points(heightmap):
    points = []
    for row in range(heightmap.shape[0]):
        for col in range(heightmap[row].shape[1]):
            adjacent = get_adjacent((row, col), heightmap)
            if heightmap[row, col] < min(adjacent):
                points.append((row, col))
    return points


def find_largest_basins(heightmap):
    def find_basin(point, visited):
        if heightmap[point[0], point[1]] == 9 or point in visited:
            return []

        visited.append(point)
        result = [point]
        for adjacent in get_adjacent_indices(point, heightmap):
            adjacent_result = find_basin(adjacent, visited)
            if len(adjacent_result) > 0:
                result += adjacent_result

        return result

    result = []
    for point in find_low_points(heightmap):
        visited = []
        result.append(find_basin(point, visited))

    return list(sorted(result, key=len))
