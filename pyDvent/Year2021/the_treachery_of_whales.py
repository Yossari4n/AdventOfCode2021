from pyDvent import commons
from functools import reduce
import sys


def the_treachery_of_whales(file_path):
    with open(file_path, 'r') as file:
        positions = list(map(int, file.read().split(',')))
        return calculate_fuel(positions), calculate_fuel_partial_sum(positions)


def calculate_fuel(ships_positions):
    min_fuel = sys.maxsize
    for position in range(min(ships_positions), max(ships_positions)):
        fuel_used = reduce(lambda a, b: a + abs(b - position), ships_positions, 0)
        min_fuel = min(min_fuel, fuel_used)
    return min_fuel


def calculate_fuel_partial_sum(ships_positions):
    min_fuel = sys.maxsize
    for position in range(min(ships_positions), max(ships_positions)):
        fuel_used = reduce(lambda a, b: a + int(commons.partial_sum(abs(b - position))), ships_positions, 0)
        min_fuel = min(min_fuel, fuel_used)
    return min_fuel
