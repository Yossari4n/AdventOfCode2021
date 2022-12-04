def rucksack_reorganization(file_path):
    def score_item(item):
        return ord(item) - 96 if item >= 'a' else ord(item) - 64 + 26

    with open(file_path, 'r') as input_file:
        prio_sum = 0
        for line in input_file:
            half = len(line)//2
            commons = set(line[0:half]) & set(line[half:])
            prio_sum += score_item(commons.pop())

    with open(file_path, 'r') as input_file:
        score = 0
        lines = input_file.read().splitlines()
        for i in range(0, len(lines), 3):
            sets = [set(x) for x in lines[i:i+3]]
            commons = set.intersection(*sets)
            score += score_item(commons.pop())

    return prio_sum, score
