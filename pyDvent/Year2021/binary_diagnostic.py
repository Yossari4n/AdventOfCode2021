import functools
import numpy as np


def binary_diagnostic(input_file):
    with open(input_file, 'r') as file:
        data = " ".join(file.read().rstrip()).replace('\n', ';')
        power_consumption = calculate_power_consumption(np.matrix(data))

    with open(input_file, 'r') as file:
        binaries = file.readlines()
        life_support_rating = calculate_life_support_rating(binaries)

    return power_consumption, life_support_rating


def calculate_power_consumption(matrix):
    result = [np.bincount(np.ravel(col)).argmax() for col in matrix.T]
    gamma = functools.reduce(lambda acc, v: acc + 2**v[0] * v[1], enumerate(reversed(result)), 0)
    epsilon = functools.reduce(lambda acc, v: acc + 2**v[0] * abs(v[1] - 1), enumerate(reversed(result)), 0)
    return gamma * epsilon


def calculate_oxygen_generator_rating(binaries, position):
    if len(binaries) == 1:
        return binaries[0]

    with_1 = []
    with_0 = []
    for binary in binaries:
        if binary[position] == '1':
            with_1.append(binary)
        else:
            with_0.append(binary)

    if len(with_1) >= len(with_0):
        return calculate_oxygen_generator_rating(with_1, position + 1)
    else:
        return calculate_oxygen_generator_rating(with_0, position + 1)


def calculate_co2_scrubber_rating(binaries, position):
    if len(binaries) == 1:
        return binaries[0]

    with_1 = []
    with_0 = []
    for binary in binaries:
        if binary[position] == '1':
            with_1.append(binary)
        else:
            with_0.append(binary)

    if len(with_1) < len(with_0):
        return calculate_co2_scrubber_rating(with_1, position + 1)
    else:
        return calculate_co2_scrubber_rating(with_0, position + 1)


def calculate_life_support_rating(matrix):
    oxygen_generator_rating = calculate_oxygen_generator_rating(matrix, 0)
    co2_scrubber_rating = calculate_co2_scrubber_rating(matrix, 0)
    return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)
