from collections import deque


def arithmetic_logic_unit():
    with open('pyDvent/Year2021/input/Day24.txt', 'r') as file:
        program = file.readlines()
        input_buffer = deque(list('19999896149362'))
        register = run(program, input_buffer)
        return None, None


def run(program, input_buffer):
    def substitute(token):
        try:
            return int(token)
        except ValueError:
            return register[indices[token]]

    register = [0, 0, 0, 0]

    operations = {
        'inp': lambda args: int(input_buffer.popleft()),
        'add': lambda args: args[0] + args[1],
        'mul': lambda args: args[0] * args[1],
        'div': lambda args: args[0] // args[1],
        'mod': lambda args: args[0] % args[1],
        'eql': lambda args: int(args[0] == args[1])
    }

    indices = {
        'x': 0,
        'y': 1,
        'z': 2,
        'w': 3
    }

    for line in program:
        tokens = line.replace('\n', '').split(' ')
        instruction, destination, arguments = tokens[0], indices[tokens[1]], list(map(substitute, tokens[1:]))
        register[destination] = operations[instruction](arguments)

    return register
