from collections import namedtuple

Cuboid = namedtuple('Cuboid', 'value, x_min, x_max, y_min, y_max, z_min, z_max')


def reactor_reboot():
    with open('pyDvent/Year2021/input/Day22.txt') as file:
        cuboids = create_commands(file.readlines())
        return None, None


def create_commands(lines):
    cuboids = []
    for line in lines:
        tokens = line.split(' ')
        state = 1 if tokens[0] == 'on' else 0
        tokens = tokens[1].split(',')

        range_tokens = tokens[0].split('=')[1].split('..')
        x_min, x_max = int(range_tokens[0]), int(range_tokens[1])
        range_tokens = tokens[1].split('=')[1].split('..')
        y_min, y_max = int(range_tokens[0]), int(range_tokens[1])
        range_tokens = tokens[2].split('=')[1].split('..')
        z_min, z_max = int(range_tokens[0]), int(range_tokens[1])
        cuboids.append(Cuboid(state, x_min, x_max, y_min, y_max, z_min, z_max))
    return cuboids
