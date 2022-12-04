from collections import Counter


def lanternfish(file_path):
    with open(file_path, 'r') as file:
        fish_list = list(map(int, file.read().split(',')))
        return simulate(fish_list, 80), simulate(fish_list, 256)


def simulate(fish_list, days):
    buckets = [0] * 9

    counter = Counter(fish_list)
    for key, value in zip(counter.keys(), counter.values()):
        buckets[key] = value

    for _ in range(days):
        first_value = buckets[0]
        for i in range(len(buckets) - 1):
            buckets[i] = buckets[i + 1]
        buckets[6] += first_value
        buckets[8] = first_value

    return sum(buckets)
