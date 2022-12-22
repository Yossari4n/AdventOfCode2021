import ast
from pyDvent import commons
from functools import cmp_to_key


def distress_signal(input_path):
    with open(input_path, 'r') as input_file:
        packets = [pair.split('\n') for pair in input_file.read().split('\n\n')]
        packet_pairs = [list(map(ast.literal_eval, pair)) for pair in packets]

        right_order = [index + 1 for index, pair in enumerate(packet_pairs) if compare(pair[0], pair[1]) == 1]

        packets = [packet for packet_pair in packet_pairs for packet in packet_pair] + [[[2]]] + [[[6]]]
        packets = sorted(packets, key=cmp_to_key(compare), reverse=True)

        return sum(right_order), (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


def compare(left, right):
    match left, right:
        case int(left), int(right):
            return commons.three_way_comparison(right, left)
        case list(left), list(right):
            for a, b in zip(left, right):
                result = compare(a, b)
                if result != 0:
                    return result
            return commons.three_way_comparison(len(right), len(left))
        case (int(left), list(right)) | (list(left), int(right)):
            left = [left] if type(left) is not list else left
            right = [right] if type(right) is not list else right
            return compare(left, right)
