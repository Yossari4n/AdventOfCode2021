import itertools


class Cave:
    def __init__(self, name):
        self.name = name
        self.is_big = name.isupper()
        self.neighbours = []


def create_cave_system(lines):
    cave_system = dict()
    for line in lines:
        caves = line.replace('\n', '').split('-')
        left_cave, right_cave = caves[0], caves[1]
        if left_cave not in cave_system:
            cave_system[left_cave] = Cave(left_cave)
        if right_cave not in cave_system:
            cave_system[right_cave] = Cave(right_cave)
        cave_system[left_cave].neighbours.append(cave_system[right_cave])
        cave_system[right_cave].neighbours.append(cave_system[left_cave])
    return cave_system


def passage_pathing(file_path):
    with open(file_path, 'r') as file:
        cave_system = create_cave_system(file.readlines())
        result1 = len(find_paths(cave_system))
        result2 = len(find_paths2(cave_system))

        return result1, result2


def find_paths(cave_system):
    def find_paths(cave, path, visited):
        if not cave.is_big and cave.name in visited:
            return
        else:
            visited.append(cave.name)

        path.append(cave.name)

        if cave.name == 'end':
            paths.append(path)
            return

        for neighbour in cave.neighbours:
            find_paths(neighbour, path.copy(), visited.copy())

    paths = []
    find_paths(cave_system['start'], [], [])
    return paths


def find_paths2(cave_system):
    def find_paths2(cave, path, visited, small_cave):
        if cave.name == small_cave[0]:
            if small_cave[1] == 2:
                return

            small_cave = (small_cave[0], small_cave[1] + 1)
        else:
            if not cave.is_big and cave.name in visited:
                return
            else:
                visited.append(cave.name)

        path.append(cave.name)

        if cave.name == 'end':
            paths.append(path)
            return

        for neighbour in cave.neighbours:
            find_paths2(neighbour, path.copy(), visited.copy(), small_cave)

    paths = []
    find_paths2(cave_system['start'], [], [], ('', 0))
    for key, value in cave_system.items():
        if not value.is_big and value.name != 'start' and value.name != 'end':
            find_paths2(cave_system['start'], [], [], (value.name, 0))

    paths.sort()
    paths = list(k for k, _ in itertools.groupby(paths))
    return paths
