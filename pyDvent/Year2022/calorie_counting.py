def calorie_counting(file_path):
    with open(file_path, 'r') as input_file:
        calories = [sum(list(map(int, x.split('\n')))) for x in input_file.read().split('\n\n')]

    calories.sort(reverse=True)
    return calories[0], sum(calories[0:3])
