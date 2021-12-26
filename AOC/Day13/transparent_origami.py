import numpy as np
from operator import itemgetter


def transparent_origami():
    with open('Day13/input.txt', 'r') as file:
        lines = file.readlines()
        empty_line = lines.index('\n')
        paper = create_transparent_paper(lines[:empty_line])
        fold_commands = create_fold_commands(lines[empty_line:])

        result1 = fold_commands[0](paper).sum()

        for command in fold_commands:
            paper = command(paper)
        result2 = decode_result(paper)

        return result1, result2


def create_transparent_paper(lines):
    coordinates = [tuple(map(int, line.replace('\n', '').split(','))) for line in lines]
    max_x = max(coordinates, key=itemgetter(0))[0]
    max_y = max(coordinates, key=itemgetter(1))[1]

    transparent_paper = np.zeros((max_y + 1, max_x + 1))
    for coord in coordinates:
        transparent_paper[coord[1], coord[0]] = 1

    return transparent_paper


def fold_up(paper, row):
    up = paper[0:row, :]
    down = paper[row + 1:paper.shape[0], :]

    for r in range(down.shape[0]):
        for c in range(down.shape[1]):
            if down[r, c] == 1:
                up[row - r - 1, c] = 1

    return up


def fold_left(paper, column):
    left = paper[:, 0:column]
    right = paper[:, column+1:paper.shape[1]]

    for r in range(right.shape[0]):
        for c in range(right.shape[1]):
            if right[r, c] == 1:
                left[r, column - c - 1] = 1

    return left


def create_fold_commands(lines):
    def fold_up_closure(number):
        return lambda paper: fold_up(paper, number)

    def fold_left_closure(number):
        return lambda paper: fold_left(paper, number)

    commands = []
    for line in lines:
        args = line.split(' ')[-1].replace('\n', '').split('=')
        if args[0] == 'y':
            commands.append(fold_up_closure(int(args[1])))
        elif args[0] == 'x':
            commands.append(fold_left_closure(int(args[1])))
    return commands


def decode_result(paper):
    result = ''
    for r in range(paper.shape[0]):
        for c in range(paper.shape[1]):
            if paper[r, c] == 1:
                result += '# '
            else:
                result += '. '
        result += '\n'
    return result
