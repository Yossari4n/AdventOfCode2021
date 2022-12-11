from pyDvent.commons import clamp
import math


def cartesian_neg(a):
    return -a[0], -a[1]


def cartesian_add(a, b):
    return a[0] + b[0], a[1] + b[1]


def cartesian_sub(a, b):
    return cartesian_add(a, cartesian_neg(b))


def cartesian_length(a):
    return math.sqrt(a[0]**2 + a[1]**2)


def follow_tail(moves, length):
    head_position = (0, 0)
    tail_positions = [(0, 0)] * length
    tail_history = {
        tail_positions[-1]: 1
    }

    for head_direction, steps in moves:
        for step in range(steps):
            head_position = cartesian_add(head_position, head_direction)

            prev_direction = head_position
            for index, curr_tail in reversed(list(enumerate(tail_positions))):
                curr_tail_direction = cartesian_sub(prev_direction, curr_tail)
                if cartesian_length(curr_tail_direction) >= 2:
                    curr_tail_direction = (clamp(curr_tail_direction[0], -1, 1), clamp(curr_tail_direction[1], -1, 1))
                    tail_positions[index] = cartesian_add(curr_tail, curr_tail_direction)
                prev_direction = tail_positions[index]

            tail_history[tail_positions[0]] = tail_history.get(tail_positions[0], 0) + 1

    return tail_history


def rope_bridge(input_path):
    directions_decoder = {
        'U': (1, 0),
        'D': (-1, 0),
        'L': (0, -1),
        'R': (0, 1),
    }

    with open(input_path, 'r') as input_file:
        moves = [(directions_decoder[move[0]], int(move.split()[1])) for move in input_file.readlines()]

    result1 = follow_tail(moves, 1)
    result2 = follow_tail(moves, 9)

    return len(result1.values()), len(result2.values())
