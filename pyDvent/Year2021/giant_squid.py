import numpy as np


def giant_squid(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        numbers = list(map(int, lines[0].split(",")))

        boards = []
        for i in range(2, len(lines), 6):
            data = ''.join(lines[i: i + 5])[:-1].replace('\n', ' ; ')
            boards.append(np.matrix(data))

        return find_first_score(numbers, boards), find_last_score(numbers, boards)


def find_first_score(numbers, boards):
    for number in numbers:
        for board in boards:
            score = calculate_board_score(number, board)
            if score != -1:
                return score


def find_last_score(numbers, boards):
    last_score = 0
    for number in numbers:
        new_boards = []
        for board in boards:
            board_score = calculate_board_score(number, board)
            if board_score != -1:
                last_score = board_score
            else:
                new_boards.append(board)
        boards = new_boards
    return last_score


def calculate_board_score(number, board):
    index = np.where(board == number)
    if len(index[0]) > 0 and len(index[1]) > 0:
        board[index] = -1
        row = board[index[0][0]]
        col = board[:, index[1][0]]
        if np.all(row == -1) or np.all(col == -1):
            return board[board != -1].sum() * number

    return -1
