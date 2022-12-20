from operator import add
from re import split
from functools import reduce
from collections import namedtuple

Procedure = namedtuple('Procedure', 'amount source target')


def supply_stacks(input_path):
    with open(input_path, 'r') as input_file:
        stacks, procedures = read_input(input_file)
        for procedure in procedures:
            to_move = stacks[procedure.source][-procedure.amount:]
            to_move.reverse()
            stacks[procedure.target].extend(to_move)
            del stacks[procedure.source][-procedure.amount:]
        result1 = ''.join([value[-1] for _, value in stacks.items()])

    with open(input_path, 'r') as input_file:
        stacks, procedures = read_input(input_file)
        for procedure in procedures:
            stacks[procedure.target].extend(stacks[procedure.source][-procedure.amount:])
            del stacks[procedure.source][-procedure.amount:]
        result2 = ''.join([value[-1] for _, value in stacks.items()])

    return result1, result2


def read_input(input_file):
    stacks = dict()
    procedures = list()

    crates = list()
    indices = list()

    lines = input_file.readlines()
    for line in lines:
        line.replace('\n', '')
        if '[' in line:
            crates.append(line)
        elif line[0] == ' ':
            for el in line:
                if el != ' ' and el != '\n':
                    indices.append(line.index(el))
            for index in indices:
                el = int(line[index])
                stacks[el] = list()
                for crates_line in crates:
                    if index < len(crates_line) and crates_line[index].isalpha():
                        stacks[el].insert(0, crates_line[index])
        elif line[0] != '\n':
            values = list(map(int, split('move | from | to ', line)[1:]))
            procedures.append(Procedure(values[0], values[1], values[2]))

    return stacks, procedures
