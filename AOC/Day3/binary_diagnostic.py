import functools
import numpy as np


def binary_diagnostic1():
    with open("Day3/input.txt", 'r') as file:
        data = " ".join(file.read().rstrip()).replace('\n', ';')
        print(data)
        matrix = np.matrix(data)
        print(calculate_power_consumption(matrix))


def binary_diagnostic2():
    with open("Day3/input.txt", 'r') as file:
        binaries = file.readlines()
        oxygen_generator_rating = calculate_oxygen_generator_rating(binaries, 0)
        CO2_scrubber_rating = calculate_CO2_scrubber_rating(binaries, 0)
        print(int(oxygen_generator_rating, 2) * int(CO2_scrubber_rating, 2))


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


def calculate_CO2_scrubber_rating(binaries, position):
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
        return calculate_CO2_scrubber_rating(with_1, position + 1)
    else:
        return calculate_CO2_scrubber_rating(with_0, position + 1)
