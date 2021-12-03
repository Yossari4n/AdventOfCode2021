def sonar_sweep1():
    with open('Day1/input.txt', 'r') as input_file:
        measurements = input_file.readlines()
        measurements = list(map(int, measurements))
        print(count_increases(measurements))
        pass


def sonar_sweep2():
    with open('Day1/input.txt', 'r') as input_file:
        measurements = input_file.readlines()
        measurements = list(map(int, measurements))
        measurements = sliding_window(measurements, 3)
        print(count_increases(measurements))
        pass


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
