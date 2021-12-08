from enum import Enum
from collections import defaultdict


class SignalPart(Enum):
    TOP = 1
    TOP_LEFT = 2
    TOP_RIGHT = 3
    MIDDLE = 4
    BOTTOM_LEFT = 5
    BOTTOM_RIGHT = 6
    BOTTOM = 7


def tmp(len_signals, to_substract):
    signals = [None, None]
    for signal in len_signals:
        diff = signal - to_substract
        signals[len(diff) - 1] = diff
    return signals[0], signals[1] - signals[0]


class DigitDescriptor:
    def __init__(self, signals):
        descriptor = {i: i.value for i in SignalPart}

        len_dict = defaultdict(list)
        for signal in signals:
            len_dict[len(signal)].append(set(signal))

        descriptor[SignalPart.TOP] = len_dict[3][0] - len_dict[2][0]
        descriptor[SignalPart.BOTTOM], descriptor[SignalPart.BOTTOM_LEFT] = tmp(len_dict[6], len_dict[4][0] | len_dict[3][0])
        descriptor[SignalPart.MIDDLE], descriptor[SignalPart.TOP_LEFT] = tmp(len_dict[5], len_dict[3][0] | descriptor[SignalPart.BOTTOM] | descriptor[SignalPart.BOTTOM_LEFT])
        descriptor[SignalPart.BOTTOM_RIGHT], descriptor[SignalPart.TOP_RIGHT] = tmp(len_dict[6], len_dict[7][0] - len_dict[2][0])

        self.numbers = {
            ''.join(len_dict[7][0] - descriptor[SignalPart.MIDDLE]): 0,
            ''.join(len_dict[2][0]): 1,
            ''.join(descriptor[SignalPart.TOP] | descriptor[SignalPart.TOP_RIGHT] | descriptor[SignalPart.MIDDLE] | descriptor[SignalPart.BOTTOM_LEFT] | descriptor[SignalPart.BOTTOM]): 2,
            ''.join(len_dict[7][0] - (descriptor[SignalPart.TOP_LEFT] | descriptor[SignalPart.BOTTOM_LEFT])): 3,
            ''.join(len_dict[4][0]): 4,
            ''.join(descriptor[SignalPart.TOP] | descriptor[SignalPart.TOP_LEFT] | descriptor[SignalPart.MIDDLE] | descriptor[SignalPart.BOTTOM_RIGHT] | descriptor[SignalPart.BOTTOM]): 5,
            ''.join(len_dict[7][0] - descriptor[SignalPart.TOP_RIGHT]): 6,
            ''.join(len_dict[3][0]): 7,
            ''.join(len_dict[7][0]): 8,
            ''.join(len_dict[7][0] - descriptor[SignalPart.BOTTOM_LEFT]): 9
        }

    def signal_to_digit(self, signal):
        for i, (key, value) in enumerate(self.numbers.items()):
            if set(key) == set(signal):
                return value


def seven_segment_search():
    with open('Day8/input.txt', 'r') as file:
        segments = []
        digits = []
        for line in file.readlines():
            tokens = line.replace('\n', '').split(' | ')
            segments.append(tokens[0].split(' '))
            digits.append(tokens[1].split(' '))

        result1 = count_unique(digits)
        result2 = fix_signals(segments, digits)
        return result1, result2


def count_unique(digits_list):
    unique_lengths = [2, 4, 3, 7]

    counter = 0
    for digits in digits_list:
        for digit in digits:
            if len(digit) in unique_lengths:
                counter += 1

    return counter


def fix_signals(segments_list, digits_list):
    result = 0
    for segments, digits in zip(segments_list, digits_list):
        descriptor = DigitDescriptor(segments)

        number = ""
        for digit in digits:
            number += str(descriptor.signal_to_digit(digit))
        result += int(number)

    return result
