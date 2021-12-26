import numpy as np
import operator


def dumbo_octopus():
    with open('Day11/input.txt', 'r') as file:
        data = " ".join(file.read().replace('\n', ';'))
        matrix = np.matrix(data)
        print(count_flashes(matrix, 500))


def get_adjacent_indices(index, grid):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    indices = []
    for direction in directions:
        new_index = tuple(map(operator.add, index, direction))
        if 0 <= new_index[0] < grid.shape[0] and 0 <= new_index[1] < grid.shape[1]:
            indices.append(new_index)

    return indices


def count_flashes(grid, steps):
    def process_flashes(point):
        grid[point[0], point[1]] += 1
        if point not in flashed and grid[point[0], point[1]] > 9:
            flashed.append(point)
            for adjacent in get_adjacent_indices(point, grid):
                process_flashes(adjacent)

    result = 0
    for step in range(steps):
        current_result = 0
        flashed = []
        for row in range(grid.shape[0]):
            for col in range(grid[row].shape[1]):
                grid[row, col] += 1
                if grid[row, col] > 9:
                    process_flashes((row, col))
        for row in range(grid.shape[0]):
            for col in range(grid[row].shape[1]):
                if grid[row, col] > 9:
                    grid[row, col] = 0
                    current_result += 1
        if np.all(grid == 0):
            print(step)
        result += current_result

    return result
