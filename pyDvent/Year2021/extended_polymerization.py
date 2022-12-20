def extended_polymerization(file_path):
    with open(file_path, 'r') as input_file:
        lines = input_file.readlines()
        template = lines[0].replace('\n', '')
        rules = create_rules(lines[2:])

        return score_polymer(create_polymer(template, rules, 10)), score_polymer(create_polymer(template, rules, 40))


def create_rules(lines):
    return {args[0]: args[1] for args in [line.replace('\n', '').split(' -> ') for line in lines]}


def create_polymer(template, rules, steps):
    polymer = dict()
    for key in [template[index] + template[index + 1] for index in range(len(template) - 1)]:
        polymer[key] = polymer.get(key, 0) + 1

    for _ in range(steps):
        new_polymer = dict()
        for key, value in polymer.items():
            middle = rules[key]

            to_add = key[0] + middle
            new_polymer[to_add] = new_polymer.get(to_add, 0) + value

            to_add = middle + key[1]
            new_polymer[to_add] = new_polymer.get(to_add, 0) + value
        polymer = new_polymer

    return polymer


def score_polymer(polymer):
    scores = dict()
    for key, value in list(polymer.items()):
        scores[key[0]] = scores.get(key[0], 0) + value

    return max(scores.values()) - min(scores.values())
