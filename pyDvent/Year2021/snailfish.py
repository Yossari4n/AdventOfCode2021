import math
import re
import ast
from functools import reduce


def snailfish(file_path):
    with open(file_path, 'r') as file:
        snailfish_numbers = create_snailfish_numbers(file.readlines())
        result = reduce(lambda a, b: reduce_snailfish_number(add_snailfish_numbers(a, b)), snailfish_numbers)
        magnitude = calculate_snailfish_number_magnitude(result)

        max_magnitude = -float('inf')
        for index, first in enumerate(snailfish_numbers):
            for second in snailfish_numbers[index:]:
                new_number = add_snailfish_numbers(first, second)
                new_number = reduce_snailfish_number(new_number)
                max_magnitude = max(max_magnitude, calculate_snailfish_number_magnitude(new_number))

        return magnitude, max_magnitude


def create_snailfish_numbers(numbers):
    snailfish_numbers = []
    for number in numbers:
        # snailfish_numbers.append(ast.literal_eval(number.replace('\n', '')))
        snailfish_numbers.append(number.replace('\n', ''))
    return snailfish_numbers


def add_snailfish_numbers(a, b):
    return '[' + a + ',' + b + ']'


def reduce_snailfish_number(number):
    def find_numbers(string):
        return [(m.group(), m.start(), m.end()) for m in re.finditer(r'[0-9]+', string)]

    def explode_snailfish_number(number):
        bracket_index = 0
        for index, char in enumerate(number):
            if char == '[':
                bracket_index += 1
            elif char == ']':
                bracket_index -= 1

            if bracket_index == 5:
                opening_bracket_index = index
                closing_bracket_index = index + number[index:].index(']')

                left_side = number[:opening_bracket_index]
                right_side = number[closing_bracket_index + 1:]
                middle = number[opening_bracket_index + 1:closing_bracket_index]
                paired_numbers = list(map(int, middle.split(',')))

                left_numbers = find_numbers(left_side)
                if len(left_numbers) != 0:
                    new_left_value = int(left_numbers[-1][0]) + paired_numbers[0]
                    left_side = left_side[:left_numbers[-1][1]] + str(new_left_value) + left_side[left_numbers[-1][2]:]

                right_numbers = find_numbers(right_side)
                if len(right_numbers) != 0:
                    new_right_value = int(right_numbers[0][0]) + paired_numbers[1]
                    right_side = right_side[:right_numbers[0][1]] + str(new_right_value) + right_side[right_numbers[0][2]:]

                return left_side + '0' + right_side
        return None

    def slice_snailfish_number(number):
        found_results = find_numbers(number)
        for result in found_results:
            value = int(result[0])
            if value > 9:
                new_pair = '[' + str(value // 2) + ',' + str(math.ceil(value / 2.0)) + ']'
                return number[:result[1]] + new_pair + number[result[2]:]
        return None

    new_value = explode_snailfish_number(number)
    if new_value is not None:
        return reduce_snailfish_number(new_value)
    else:
        new_value = slice_snailfish_number(number)
        if new_value is not None:
            return reduce_snailfish_number(new_value)
        else:
            return number


def calculate_snailfish_number_magnitude(number):
    def inner_calculate_snailfish_number_magnitude(lst):
        if isinstance(lst[0], list):
            left = inner_calculate_snailfish_number_magnitude(lst[0])
        else:
            left = int(lst[0])

        if isinstance(lst[1], list):
            right = inner_calculate_snailfish_number_magnitude(lst[1])
        else:
            right = int(lst[1])

        return 3 * left + 2 * right

    list_representation = ast.literal_eval(number)
    return inner_calculate_snailfish_number_magnitude(list_representation)
