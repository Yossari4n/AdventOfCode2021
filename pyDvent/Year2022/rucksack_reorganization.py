def rucksack_reorganization(file_path):
    def score_item(item):
        return ord(item) - 96 if item >= 'a' else ord(item) - 64 + 26

    with open(file_path, 'r') as input_file:
        commons = [(set(line[0:len(line)//2]) & set(line[len(line)//2:])).pop() for line in input_file.readlines()]
        prio_sum = sum(map(score_item, commons))

    with open(file_path, 'r') as input_file:
        score = 0
        lines = input_file.read().splitlines()
        for i in range(0, len(lines), 3):
            sets = [set(x) for x in lines[i:i+3]]
            score += score_item(set.intersection(*sets).pop())

    return prio_sum, score
