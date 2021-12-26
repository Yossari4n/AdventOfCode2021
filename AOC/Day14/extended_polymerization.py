import operator


def extended_polymerization():
    with open('Day14/input.txt', 'r') as file:
        lines = file.readlines()
        template = lines[0].replace('\n', '')
        rules = create_rules(lines[2:])

        return score_polymer(create_polymer(template, rules, 10)), score_polymer(create_polymer(template, rules, 40))


def create_rules(lines):
    rules = dict()
    for line in lines:
        line = line.replace('\n', '')
        args = line.split(' -> ')
        rules[args[0]] = args[1]
    return rules


def create_polymer(template, rules, steps):
    polymer = dict()
    for index in range(0, len(template) - 1, 1):
        key = template[index] + template[index + 1]
        if key in polymer:
            polymer[key] += 1
        else:
            polymer[key] = 1

    for _ in range(steps):
        new_polymer = dict()
        for key, value in polymer.items():
            middle = rules[key]
            to_add = key[0] + middle

            if to_add not in new_polymer:
                new_polymer[to_add] = value
            else:
                new_polymer[to_add] += value

            to_add = middle + key[1]
            if to_add not in new_polymer:
                new_polymer[to_add] = value
            else:
                new_polymer[to_add] += value

        polymer = new_polymer

    return polymer


def score_polymer(polymer):
    scores = dict()
    items = list(polymer.items())
    for key, value in items:
        letter = key[0]
        if letter in scores:
            scores[letter] += value
        else:
            scores[letter] = value

    return max(scores.items(), key=operator.itemgetter(1))[1] - min(scores.items(), key=operator.itemgetter(1))[1]
