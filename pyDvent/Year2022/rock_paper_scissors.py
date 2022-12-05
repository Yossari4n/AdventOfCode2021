from enum import Enum


class Shape(Enum):
    Rock = 1,
    Paper = 2,
    Scissors = 3,


class RoundOutcome(Enum):
    Win = 1,
    Lose = 2,
    Tie = 3,


rules = {
    (Shape.Rock, Shape.Rock): RoundOutcome.Tie,
    (Shape.Rock, Shape.Paper): RoundOutcome.Lose,
    (Shape.Rock, Shape.Scissors): RoundOutcome.Win,
    (Shape.Paper, Shape.Rock): RoundOutcome.Win,
    (Shape.Paper, Shape.Paper): RoundOutcome.Tie,
    (Shape.Paper, Shape.Scissors): RoundOutcome.Lose,
    (Shape.Scissors, Shape.Rock): RoundOutcome.Lose,
    (Shape.Scissors, Shape.Paper): RoundOutcome.Win,
    (Shape.Scissors, Shape.Scissors): RoundOutcome.Tie
}


def rock_paper_scissors(input_path):
    shape_to_score = {
        Shape.Rock: 1,
        Shape.Paper: 2,
        Shape.Scissors: 3,
    }

    outcome_to_score = {
        RoundOutcome.Win: 6,
        RoundOutcome.Lose: 0,
        RoundOutcome.Tie: 3
    }

    shape_decrypted = {
        'A': Shape.Rock,
        'B': Shape.Paper,
        'C': Shape.Scissors,
        'X': Shape.Rock,
        'Y': Shape.Paper,
        'Z': Shape.Scissors,
    }

    output_decrypted = {
        'X': RoundOutcome.Lose,
        'Y': RoundOutcome.Tie,
        'Z': RoundOutcome.Win,
    }

    with open(input_path, 'r') as file:
        rounds = [(shape_decrypted[line[2]], shape_decrypted[line[0]]) for line in file.readlines()]
        score1 = sum(map(lambda round: outcome_to_score[rules[round]] + shape_to_score[round[0]], rounds))

    with open(input_path, 'r') as file:
        rounds = [(shape_decrypted[line[0]], output_decrypted[line[2]]) for line in file.readlines()]
        player_moves = map(lambda round: next(k[0] for k, v in rules.items() if v == round[1] and k[1] == round[0]), rounds)
        score2 = sum(map(lambda round: outcome_to_score[round[1]], rounds))
        score2 += sum(map(lambda move: shape_to_score[move], player_moves))

    return score1, score2
