import numpy as np


def giant_squid(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().split('\n\n')
        numbers = list(map(int, lines[0].split(",")))
        boards = [np.matrix(data.replace('\n', ' ; ')) for data in lines[1:]]
        scores = play_bingo(numbers, boards)
        return scores[0], scores[-1]


def play_bingo(numbers, boards):
    scores = []
    for number in numbers:
        new_boards = []
        for board in boards:
            board_score = calculate_board_score(number, board)
            if board_score is not None:
                scores.append(board_score)
            else:
                new_boards.append(board)
        boards = new_boards
    return scores


def calculate_board_score(number, board):
    index = np.where(board == number)
    if len(index[0]) > 0 and len(index[1]) > 0:
        board[index] = -1
        row = board[index[0][0]]
        col = board[:, index[1][0]]
        if np.all(row == -1) or np.all(col == -1):
            return board[board != -1].sum() * number

    return None
