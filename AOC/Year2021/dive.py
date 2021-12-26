def dive():
    with open('Year2021/input/Day2.txt', 'r') as input_file:
        commands = input_file.readlines()
        return calculate_position(commands), calculate_position_with_aim(commands)


def calculate_position(commands):
    horizontal = 0
    depth = 0
    for command in commands:
        dimension, value = extract(command)
        if dimension == "forward":
            horizontal += value
        elif dimension == "up":
            depth -= value
        elif dimension == "down":
            depth += value

    return horizontal * depth


def calculate_position_with_aim(commands):
    horizontal = 0
    depth = 0
    aim = 0
    for command in commands:
        dimension, value = extract(command)
        if dimension == "forward":
            horizontal += value
            depth += value * aim
        elif dimension == "up":
            aim -= value
        elif dimension == "down":
            aim += value

    return horizontal * depth


def extract(command):
    tokens = command.split(" ")
    return tokens[0], int(tokens[1])
