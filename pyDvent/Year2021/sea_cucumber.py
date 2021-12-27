def sea_cucumber():
    with open('pyDvent/Year2021/input/Day25.txt', 'r') as file:
        seafloor = [list(line.replace('\n', '')) for line in file.readlines()]
        result = simulate(seafloor)
        return result, None


def simulate(seafloor):
    can_land = False
    steps = 0
    while not can_land:
        can_land = True

        new_seafloor = [['.'] * len(row) for row in seafloor]
        for row in range(len(seafloor)):
            for col in range(len(seafloor[row])):
                ceil = seafloor[row][col]
                if ceil == '>':
                    direction = (0, 1)
                    position = ((row + direction[0]) % len(seafloor), (col + direction[1]) % len(seafloor[row]))
                    if seafloor[position[0]][position[1]] == '.':
                        new_seafloor[position[0]][position[1]] = ceil
                        can_land = False
                    else:
                        new_seafloor[row][col] = ceil
                elif ceil == 'v':
                    new_seafloor[row][col] = ceil
        seafloor = new_seafloor

        new_seafloor = [['.'] * len(row) for row in seafloor]
        for row in range(len(seafloor)):
            for col in range(len(seafloor[row])):
                ceil = seafloor[row][col]
                if ceil == 'v':
                    direction = (1, 0)
                    position = ((row + direction[0]) % len(seafloor), (col + direction[1]) % len(seafloor[row]))
                    if seafloor[position[0]][position[1]] == '.':
                        new_seafloor[position[0]][position[1]] = ceil
                        can_land = False
                    else:
                        new_seafloor[row][col] = ceil
                elif ceil == '>':
                    new_seafloor[row][col] = ceil
        seafloor = new_seafloor

        steps += 1

    return steps
