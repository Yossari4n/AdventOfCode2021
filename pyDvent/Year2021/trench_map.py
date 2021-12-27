from operator import itemgetter
from functools import reduce


def trench_map():
    with open('pyDvent/Year2021/input/Day20.txt', 'r') as file:
        lines = file.readlines()
        algorithm = lines[0].replace('\n', '')
        image = create_infinite_image(lines[2:])

        for i in range(0, 50):
            if i % 2 == 1:
                default = '0' if algorithm[0] == '.' else '1'
            else:
                default = '1' if algorithm[0] == '.' else '0'

            image = enhance_infinite_image(image, algorithm, default)
            if i == 1:
                result1 = reduce(lambda a, b: a + b, image.values())
        result2 = reduce(lambda a, b: a + b, image.values())

        return result1, result2


def create_infinite_image(lines):
    image = dict()
    for x, row in enumerate(lines):
        row = row.replace('\n', '')
        for y, value in enumerate(row):
            image[(x, y)] = 1 if value == '#' else 0
    return image


def enhance_infinite_image(image, algorithm, default):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

    enhanced_image = dict()
    max_x = max(image.keys(), key=itemgetter(0))[0]
    max_y = max(image.keys(), key=itemgetter(1))[1]

    for row in range(-1, max_x + 2):
        for col in range(-1, max_y + 2):
            index = ''
            for direction in directions:
                position = (row + direction[0], col + direction[1])
                index += str(image.get(position, default))
            index = int(index, 2)
            enhanced_image[row + 1, col + 1] = 1 if algorithm[index] == '#' else 0

    return enhanced_image
