def cathorode_tube(input_path):
    instruction_costs = {
        'noop': 1,
        'addx': 2,
    }

    clock = 0
    register = 1

    signal_strengths = [20, 60, 100, 140, 180, 220]
    result1 = 0

    crt = ""

    with open(input_path, 'r') as input_file:
        for instruction in input_file.readlines():
            match instruction.rstrip().split(' '):
                case ['noop']:
                    cycles = instruction_costs['noop']
                    register_next_state = register
                case ['addx', value]:
                    cycles = instruction_costs['addx']
                    register_next_state = register + int(value)

            for _ in range(cycles):
                clock += 1
                result1 = result1 + register * clock if clock in signal_strengths else result1
                crt += '#' if register <= clock % 40 <= (register + 2) else '.'

            register = register_next_state

    return result1, '\n' + crt[0:40] + '\n' + crt[40:80] + '\n' + crt[80:120] + '\n' + crt[120:160] + '\n' + crt[160:200] + '\n' + crt[200:240]
