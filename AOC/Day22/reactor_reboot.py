from collections import namedtuple

Cuboid = namedtuple('Cuboid', 'value, x_min, x_max, y_min, y_max, z_min, z_max')


def reactor_reboot():
    with open('Day22/input.txt') as file:
        cuboids = create_commands(file.readlines())
        # reactor = initialize_reboot(commands)
        print(cuboids)
        print(common_cuboid(cuboids[0], cuboids[1]))


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


def common_cuboid(a, b):
    value = b.value
    x2, x1 = min(a.x_max, b.x_max), max(a.x_min, b.x_min)
    y2, y1 = min(a.y_max, b.y_max), max(a.y_min, b.y_min)
    z2, z1 = min(a.z_max, b.z_max), max(a.z_min, b.z_min)
    return Cuboid(value, x1, x2, y1, y2, z1, z2)



