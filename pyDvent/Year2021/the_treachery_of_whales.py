from pyDvent import commons
from functools import reduce


def the_treachery_of_whales(file_path):
    with open(file_path, 'r') as file:
        positions = list(map(int, file.read().split(',')))

        return calculate_fuel(positions), calculate_fuel_partial_sum(positions)


def calculate_fuel(ships_positions):
    min_fuel = float('inf')
    for i in range(min(ships_positions), max(ships_positions)):
        fuel_used = reduce(lambda a, b: a + abs(b - i), ships_positions, 0)
        for pos in ships_positions:
            fuel_used += abs(pos - i)

        min_fuel = min(min_fuel, fuel_used)
    return min_fuel


def calculate_fuel_partial_sum(ships_positions):
    min_fuel = float('inf')
    for position in range(min(ships_positions), max(ships_positions)):
        fuel_used = 0
        for ship_position in ships_positions:
            fuel_used += commons.partial_sum(abs(ship_position - position))

        min_fuel = min(min_fuel, fuel_used)
    return min_fuel
