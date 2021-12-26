import operator


def get_adjacent_indices(index, grid, include_diagonal):
    if include_diagonal:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    else:
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    indices = []
    for direction in directions:
        new_index = tuple(map(operator.add, index, direction))
        if 0 <= new_index[0] < grid.shape[0] and 0 <= new_index[1] < grid.shape[1]:
            indices.append(new_index)

    return indices


def get_adjacent_values(index, grid, include_diagonal, default=None):
    if include_diagonal:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    else:
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    values = []
    for direction in directions:
        new_index = tuple(map(operator.add, index, direction))
        if 0 <= new_index[0] < grid.shape[0] and 0 <= new_index[1] < grid.shape[1]:
            values.append(grid[new_index[0], new_index[1]])
        else:
            if default is not None:
                values.append(default)

    return values


def partial_sum(n):
    return n * (n + 1) / 2


def clamp(n, a, b):
    return max(min(b, n), a)
