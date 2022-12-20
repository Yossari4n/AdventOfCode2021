from pyDvent import commons
import numpy as np


def dumbo_octopus(file_path):
    with open(file_path, 'r') as file:
        data = " ".join(file.read().replace('\n', ';'))
        result1 = count_flashes(np.matrix(data), 100)
        result2 = find_first_full_flash(np.matrix(data))
        return result1, result2


def process_flashes(point, grid, flashed):
    grid[point[0], point[1]] += 1
    if point not in flashed and grid[point[0], point[1]] > 9:
        flashed.append(point)
        for adjacent in commons.get_adjacent_indices(point, grid, include_diagonal=True):
            process_flashes(adjacent, grid, flashed)


def count_flashes(grid, steps):
    result = 0
    for step in range(steps):
        flashed = []
        for row in range(grid.shape[0]):
            for col in range(grid[row].shape[1]):
                grid[row, col] += 1
                if grid[row, col] > 9:
                    process_flashes((row, col), grid, flashed)

        current_result = 0
        for row in range(grid.shape[0]):
            for col in range(grid[row].shape[1]):
                if grid[row, col] > 9:
                    grid[row, col] = 0
                    current_result += 1

        if np.all(grid == 0):
            print(step)
        result += current_result

    return result


def find_first_full_flash(grid):
    steps = 0
    while True:
        current_result = 0
        flashed = []
        for row in range(grid.shape[0]):
            for col in range(grid[row].shape[1]):
                grid[row, col] += 1
                if grid[row, col] > 9:
                    process_flashes((row, col), grid, flashed)
        for row in range(grid.shape[0]):
            for col in range(grid[row].shape[1]):
                if grid[row, col] > 9:
                    grid[row, col] = 0
                    current_result += 1

        steps += 1
        if np.all(grid == 0):
            return steps
