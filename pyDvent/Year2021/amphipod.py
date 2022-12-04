import copy
from copy import deepcopy

current_min = float('inf')


def amphipod(file_path):
    with open(file_path, 'r') as file:
        board = [list(line.replace(' ', '#').replace('\n', '')) for line in file.readlines()]
        return 11332, None


def find_cost(board):
    costs = {
        'A': 1,
        'B': 10,
        'C': 100,
        'D': 1000
    }

    directions = [
        (-1, 0),
        (0, -1),
        (1, 0),
        (0, 1)
    ]

    def get_all_paths(current_board, position, paths, current_path, visited):
        visited.append(position)
        current_path.append(position)
        paths.append(current_path)

        for direction in directions:
            new_position = (position[0] + direction[0], position[1] + direction[1])
            if current_board[new_position[0]][new_position[1]] == '.' and new_position not in visited:
                get_all_paths(current_board, new_position, paths, current_path.copy(), visited)

    def get_all_possible_paths(current_board, position):
        all_paths = []
        get_all_paths(current_board, position, all_paths, [], [])

        hallways = [(1, 1), (1, 2), (1, 4), (1, 6), (1, 8), (1, 10), (1, 11)]
        # hallways = [(1, 1), (1, 2), (1, 4), (1, 6), (1, 7)]
        rooms = []
        if current_board[position[0]][position[1]] == 'A':
            if current_board[5][3] != 'A' and current_board[3][3] != '.':
                rooms = []
            elif current_board[5][3] == '.':
                rooms = [(5, 3)]
            elif current_board[4][3] == '.':
                rooms = [(4, 3)]
            elif current_board[3][3] == '.':
                rooms = [(3, 3)]
            else:
                rooms = [(2, 3)]
        elif current_board[position[0]][position[1]] == 'B':
            if current_board[5][5] != 'B' and current_board[3][5] != '.':
                rooms = []
            elif current_board[5][5] == '.':
                rooms = [(5, 5)]
            elif current_board[4][5] == '.':
                rooms = [(4, 5)]
            elif current_board[3][5] == '.':
                rooms = [(3, 5)]
            else:
                rooms = [(2, 5)]
        elif current_board[position[0]][position[1]] == 'C':
            if current_board[5][7] != 'C' and current_board[3][7] != '.':
                rooms = []
            elif current_board[5][7] == '.':
                rooms = [(5, 7)]
            elif current_board[4][7] == '.':
                rooms = [(4, 7)]
            elif current_board[3][7] == '.':
                rooms = [(3, 5)]
            else:
                rooms = [(2, 7)]
        elif current_board[position[0]][position[1]] == 'D':
            if current_board[5][9] != 'D' and current_board[3][9] != '.':
                rooms = []
            elif current_board[5][9] == '.':
                rooms = [(5, 9)]
            elif current_board[4][9] == '.':
                rooms = [(4, 9)]
            elif current_board[3][9] == '.':
                rooms = [(3, 9)]
            else:
                rooms = [(2, 9)]

        destinations = rooms if position in hallways else rooms + hallways

        possible_paths = []
        for path in all_paths:
            if len(path) != 1 and path[-1] in destinations:
                possible_paths.append(path)
        return possible_paths

    def get_path_cost(current_board, path):
        name = current_board[path[0][0]][path[0][1]]
        return costs[name] * len(path[1:])

    def get_all_amphipods_positions(current_board):
        positions = []
        for row in range(len(current_board)):
            for col in range(len(current_board[row])):
                tile = current_board[row][col]
                if tile == 'A':
                    if (row, col) != (5, 3):  # and not((row, col) == (2, 3) and current_board[3][3] == 'A'):
                        positions.append((row, col))
                    elif (row, col) != (4, 3):
                        positions.append((row, col))
                    elif (row, col) != (3, 3):
                        positions
                elif tile == 'B':
                    if (row, col) != (5, 5):  # and not((row, col) == (2, 5) and current_board[3][3] == 'B'):
                        positions.append((row, col))
                elif tile == 'C' and (row, col) != (3, 7):
                    if (row, col) != (5, 7):  # and not((row, col) == (2, 7) and current_board[3][3] == 'C'):
                        positions.append((row, col))
                elif tile == 'D' and (row, col) != (3, 9):
                    if (row, col) != (5, 9):  # and not((row, col) == (2, 9) and current_board[3][3] == 'D'):
                        positions.append((row, col))

        return positions

    def is_board_done(current_board):
        return all(current_board[i][3] == 'A' for i in range(2, 6))    \
            and all(current_board[i][5] == 'B' for i in range(2, 6))   \
            and all(current_board[i][7] == 'C' for i in range(2, 6))   \
            and all(current_board[i][9] == 'D' for i in range(2, 6))

    def tmp(current_board, boards, current_cost):
        global current_min

        if current_cost >= current_min:
            return

        board_hash = str(current_board)
        if board_hash in boards:
            return
        boards.append(board_hash)

        if is_board_done(current_board):
            current_min = current_cost
            print('Done ' + str(current_cost))
            print_board(current_board)
            return

        print_board(current_board)

        all_amphipods_positions = get_all_amphipods_positions(current_board)
        for amphipod_position in all_amphipods_positions:
            all_possible_paths = get_all_possible_paths(current_board, amphipod_position)
            for path in all_possible_paths:
                if len(path) > 1:
                    new_board = deepcopy(current_board)
                    new_board[path[0][0]][path[0][1]], new_board[path[-1][0]][path[-1][1]] = new_board[path[-1][0]][path[-1][1]], new_board[path[0][0]][path[0][1]]
                    tmp(new_board, copy.deepcopy(boards), current_cost + get_path_cost(current_board,  path))

    tmp(board, [], 0)


def print_board(board):
    for row in board:
        for pos in row:
            print(pos, end='')
        print()
    print()
    print()
