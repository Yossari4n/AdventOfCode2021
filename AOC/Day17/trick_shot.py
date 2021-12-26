def trick_shot():
    with open('Day17/input.txt', 'r') as file:
        x_target, y_target = read_target_area(file.readline())
        # highest_trajectory = find_highest_trajectory(-y_target[1], -y_target[0])

        tmp = find_initial_trajectories((x_target, y_target))
        print(len(tmp))

        return 1


def read_target_area(line):
    def get_range(token):
        token = token[token.index('=') + 1:].replace(',', '')
        range_tokens = token.split('..')
        return int(range_tokens[0]), int(range_tokens[1])

    tokens = line[13:].split(' ')
    return get_range(tokens[0]), get_range(tokens[1])


def partial_sum(index):
    return index * (index + 1) / 2


def find_highest_trajectory(min_y, max_y):
    velocity = 0
    max_velocity = None
    while True:
        if min_y < partial_sum(velocity) - partial_sum(velocity - 1) < max_y:
            max_velocity = partial_sum(velocity)
        else:
            if max_velocity is not None:
                return max_velocity

        velocity += 1


def find_initial_trajectories(target_area):
    def test_velocity(x, y, range_x, range_y):
        position = (0, 0)
        while position[0] <= range_x[1]:
            if y < 0 and position[1] < range_y[0]:
                return False

            position = position[0] + x, position[1] + y
            if range_x[0] <= position[0] <= range_x[1] and range_y[0] <= position[1] <= range_y[1]:
                return True

            x = max(0, x - 1)
            y -= 1

    min_x, max_x = target_area[0][0], target_area[0][1]
    min_y, max_y = target_area[1][0], target_area[1][1]
    velocities = []
    for x in range(max_x + 1):
        for y in range(min_y, abs(max_y) + 1):
            if test_velocity(x, y, target_area[0], target_area[1]):
                velocities.append((x, y))

    return velocities
