def sonar_sweep():
    with open('Year2021/input/Day1.txt', 'r') as input_file:
        measurements = input_file.readlines()
        measurements = list(map(int, measurements))
        result1 = count_increases(measurements)

        measurements = sliding_window(measurements, 3)
        result2 = count_increases(measurements)
        return result1, result2


def count_increases(collection):
    count = 0
    previous = collection[0]
    for current in collection[1:]:
        if current > previous:
            count += 1
        previous = current
    return count


def sliding_window(collection, window_size):
    sums = []
    for i in range(len(collection) - window_size + 1):
        sums.append(sum(collection[i: i + window_size]))
    return sums
