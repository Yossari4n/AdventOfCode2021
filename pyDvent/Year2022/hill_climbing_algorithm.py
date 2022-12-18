import math
import re


def hill_climbing_algorithm(input_path):
    with open(input_path, 'r') as input_file:
        input_file = input_file.read()
        width, height = input_file.find('\n'), len(input_file) // input_file.find('\n')
        start = input_file.replace('\n', '').find('S')
        end = input_file.replace('\n', '').find('E')
        matrix = [list(map(ord, line)) for line in input_file.replace('S', 'a').replace('E', 'z').split('\n')]

        graph = dict()
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                keys = get_adjacent_indices((row, col), (height, width), include_diagonal=False)
                for index in list(filter(lambda i: matrix[i[0]][i[1]] - matrix[row][col] <= 1, keys)):
                    graph[(row * width + col, index[0] * width + index[1])] = 1

        result1 = dijkstra(graph, start)[end]

    with open(input_path, 'r') as input_file:
        input_file = input_file.read().replace('\n', '')
        starting_points = [starting_point.start() for starting_point in re.finditer('[a]', input_file)]
        paths = [dijkstra(graph, start)[end] for start in starting_points]

    return result1, min(paths)


# TODO move to commons
def dijkstra(graph, start):
    from queue import PriorityQueue

    costs = {v[0]: math.inf for v in graph.keys()}
    costs[start] = 0

    v = len(graph)
    visited = []

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        (_, current_vertex) = pq.get()
        visited.append(current_vertex)
        for neighbor in list(filter(lambda n: (current_vertex, n) in graph, range(v))):
            distance = graph[(current_vertex, neighbor)]
            if neighbor in costs and neighbor not in visited:
                old_cost = costs[neighbor]
                new_cost = costs[current_vertex] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, neighbor))
                    costs[neighbor] = new_cost

    return costs


# TODO move to commons
def get_adjacent_indices(index, shape, include_diagonal):
    from operator import add

    if include_diagonal:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    else:
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    indices = []
    for new_index in [tuple(map(add, index, direction)) for direction in directions]:
        if 0 <= new_index[0] < shape[0] and 0 <= new_index[1] < shape[1]:
            indices.append(new_index)

    return indices

