from collections import deque


def syntax_scoring(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        result1 = sum(score_syntax_error(line) for line in lines)
        scores = list(filter(
            lambda fix_score: fix_score > 0,
            list(map(score_fix, [fix_syntax(line.replace('\n', '')) for line in lines]))
        ))
        result2 = list(sorted(scores))[len(scores) // 2]

        return result1, result2


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
