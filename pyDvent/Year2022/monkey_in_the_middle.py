import operator
from functools import reduce


class Monkey:
    def __init__(self, starting_items, operation_desc, divider, on_true, on_false):
        self.divider = int(divider)
        self.items = list(map(int, starting_items.split(', ')))
        self.on_true = int(on_true)
        self.on_false = int(on_false)
        self.inspections_count = 0

        ops = {'+': operator.add, '*': operator.mul}
        match operation_desc.split(' '):
            case ['old', op, 'old']:
                self.operation = lambda old: ops[op](old, old)
            case ['old', op, c]:
                self.operation = lambda old: ops[op](old, int(c))
            case [c, op, 'old']:
                self.operation = lambda old: ops[op](int(c), old)


def parse_input(input_file):
    monkeys = dict()
    for desc in input_file.read().split('\n\n'):
        desc = desc.split('\n')
        monkeys[int(desc[0][len('Monkey'):-1])] = Monkey(
            desc[1][len('  Starting items: '):],
            desc[2][len('  Operation: new = '):],
            desc[3][len('  Test: divisible by '):],
            desc[4][len('    If true: throw to monkey '):],
            desc[5][len('    If false: throw to monkey '):]
        )
    return monkeys


def monkey_business(monkeys, rounds_number, worry_level_divider):
    lcm = reduce(operator.mul, list(map(lambda m: m.divider, monkeys.values())))
    for _ in range(1, rounds_number + 1):
        for monkey in monkeys.values():
            monkey.items = list(map(lambda item: monkey.operation(item % lcm) // worry_level_divider, monkey.items))
            monkey.inspections_count += len(monkey.items)
            monkeys[monkey.on_true].items.extend(list(filter(lambda item: (item % monkey.divider) == 0, monkey.items)))
            monkeys[monkey.on_false].items.extend(list(filter(lambda item: (item % monkey.divider) != 0, monkey.items)))
            monkey.items = []


def monkey_in_the_middle(input_path):
    with open(input_path, 'r') as input_file:
        monkeys = parse_input(input_file)
        monkey_business(monkeys, 20, 3)
        result1 = sorted(map(lambda m: m.inspections_count, monkeys.values()), reverse=True)

    with open(input_path, 'r') as input_file:
        monkeys = parse_input(input_file)
        monkey_business(monkeys, 10000, 1)
        result2 = sorted(map(lambda m: m.inspections_count, monkeys.values()), reverse=True)

    return result1[0] * result1[1], result2[0] * result2[1]
