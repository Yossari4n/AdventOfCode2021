import numpy as np
from pyDvent import commons


def chiton(file_path):
    with open(file_path, 'r') as file:
        data = ' '.join(file.read().replace('\n', ';'))
        cave = np.matrix(data)

        path = find_path(cave, (0, 0), (cave.shape[0] - 1, cave.shape[1] - 1))
        result1 = sum(cave[point[0], point[1]] for point in path) - cave[0, 0]

        full_cave = np.zeros([cave.shape[0] * 5, cave.shape[1] * 5])
        for row in range(cave.shape[0]):
            for col in range(cave.shape[1]):
                full_cave[row, col] = cave[row, col]

        for row in range(0, full_cave.shape[0]):
            for col in range(0, full_cave.shape[1]):
                mul = (row // cave.shape[0], col // cave.shape[1])
                rest = (row % cave.shape[0], col % cave.shape[1])
                new_value = cave[rest[0], rest[1]] + mul[0] + mul[1]
                full_cave[row, col] = new_value if new_value <= 9 else new_value % 9

        path = find_path(full_cave, (0, 0), (full_cave.shape[0] - 1, full_cave.shape[1] - 1))
        result2 = sum(full_cave[point[0], point[1]] for point in path) - full_cave[0, 0]

        return result1, result2


def find_path(cave, start, end):
    """
    A* algorithm from https://en.wikipedia.org/wiki/A*_search_algorithm
    """
    def h(point):
        return cave[point[0], point[1]]

    def reconstruct_path(came_from, current):
        total_path = {current}
        while current in came_from.keys():
            current = came_from[current]
            total_path.add(current)
        return total_path

    open_set = {start}
    came_from = dict()

    g_score = dict()
    g_score[start] = 0

    f_score = dict()
    f_score[start] = 0

    while len(open_set) != 0:
        current = min(open_set, key=lambda p: f_score[p])
        if current == end:
            return reconstruct_path(came_from, current)

        open_set.remove(current)
        for neighbor in commons.get_adjacent_indices(current, cave, include_diagonal=False):
            tentative_g_score = g_score[current] + h(neighbor)
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score
                if neighbor not in open_set:
                    open_set.add(neighbor)

    return None


def print_path(path, cave):
    for row in range(cave.shape[0]):
        for col in range(cave.shape[1]):
            symbol = '#' if (row, col) in path else '.'
            print(symbol, end='')
        print()
