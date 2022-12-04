def calorie_counting(file_path):
    all_records = []
    with open(file_path, 'r') as calories:
        total = 0
        for entry in calories:
            if entry == '\n':
                all_records.append(total)
                total = 0
            else:
                total += int(entry)

    all_records.sort(reverse=True)
    result1 = all_records[0]
    result2 = sum(all_records[0:3:1])

    return result1, result2


