class Player:
    def __init__(self, position):
        self.position = position
        self.score = 0


def dirac_dice():
    with open('Year2021/input/Day21.txt') as file:
        players = create_players(file.readlines())
        return find_winner(players), None


def create_players(lines):
    players = []
    for line in lines:
        tokens = line.split()
        players.append(Player(int(tokens[-1])))
    return players


def find_winner(players):
    def roll_dice(current_dice):
        to_move = 0
        for _ in range(3):
            current_dice = current_dice + 1 if current_dice + 1 <= 100 else (current_dice + 1) % 100
            to_move += current_dice
        return current_dice, to_move

    dice = 0
    rolls = 0
    while True:
        for player in players:
            dice, to_move = roll_dice(dice)
            rolls += 3

            new_position = player.position + to_move
            if new_position % 10 == 0:
                player.position = 10
            else:
                player.position = new_position % 10
            player.score += player.position

            if player.score >= 1000:
                return players[(players.index(player) + 1) % len(players)].score * rolls


def find_quantum_winner(players):
    def roll_quantum_dice(dice):
        return dice

    dice = 0
    while True:
        for player in players:
            player.position += roll_quantum_dice(dice)
