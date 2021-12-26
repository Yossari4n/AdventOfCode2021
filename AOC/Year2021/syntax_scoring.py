from collections import deque


def syntax_scoring():
    with open('Year2021/input/Day10.txt', 'r') as file:
        lines = file.readlines()

        score1 = 0
        for line in lines:
            score1 += score_syntax_error(line)

        scores = []
        for line in lines:
            fix = fix_syntax(line.replace('\n', ''))
            fix_score = score_fix(fix)
            if fix_score > 0:
                scores.append(fix_score)

        score2 = list(sorted(scores))[int(len(scores) / 2)]

        return score1, score2


def score_syntax_error(line):
    corresponding = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }

    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    stack = deque()
    for character in line:
        if character not in corresponding:
            stack.append(character)
        else:
            if stack.pop() != corresponding[character]:
                return scores[character]

    return 0


def fix_syntax(line):
    openings = {'(', '[', '{', '<'}

    corresponding = {
        ')': '(',
        '(': ')',
        ']': '[',
        '[': ']',
        '}': '{',
        '{': '}',
        '>': '<',
        '<': '>'
    }

    stack = deque()
    for character in line:
        if character in openings:
            stack.append(character)
        else:
            if stack.pop() != corresponding[character]:
                return ""

    result = ""
    while len(stack) > 0:
        result += corresponding[stack.pop()]

    return result


def score_fix(fix):
    scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    score = 0
    for character in fix:
        score = (score * 5) + scores[character]

    return score
