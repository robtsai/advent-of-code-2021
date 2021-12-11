from collections import deque
from functools import reduce


def read_data(file):
    output = []
    with open(file, "r") as f:
        for line in f:
            output.append(line.replace("\n", ""))
    return output


def find_illegal_char(line):
    q = []
    opening = ["[", "(", "<", "{"]
    closing = {"]": "[", ")": "(", ">": "<", "}": "{"}

    for char in line:
        if char in opening:
            q.append(char)
        else:
            if not q:
                raise ValueError("can't push closing on empty list")
            last = q.pop()
            if last != closing[char]:
                return char
    return None


def is_corrupt(line):
    q = []
    opening = ["[", "(", "<", "{"]
    closing = {"]": "[", ")": "(", ">": "<", "}": "{"}

    for char in line:
        if char in opening:
            q.append(char)
        else:
            if not q:
                raise ValueError("cant push closing bracket on empty list")
            last = q.pop()
            if last != closing[char]:
                return True
    return False


def get_incomplete_lines(data):
    return [line for line in data if not is_corrupt(line)]


def complete_a_line(line):
    opening = ["[", "(", "<", "{"]
    closing = {"]": "[", ")": "(", ">": "<", "}": "{"}

    line = line
    q = []

    for char in line:
        if char in opening:
            q.append(char)
        else:
            if not q:
                raise ValueError("cant push closing bracket on empty list")
            last = q.pop()
            if last != closing[char]:
                break

    r = list(reversed(q))
    # m is map of cost to close an opening bracket
    m = {"(": 1, "[": 2, "{": 3, "<": 4}
    points = [m[x] for x in r]
    score = reduce(lambda a, b: 5 * a + b, points, 0)
    return score


def score_part1(data):
    total = 0
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    for row in data:
        bad_char = find_illegal_char(row)
        if bad_char:
            total += points[bad_char]
    return total


def score_part2(data):
    incomplete_lines = get_incomplete_lines(data)
    scores = [complete_a_line(line) for line in incomplete_lines]
    sorted_scores = sorted(scores)
    return sorted_scores[len(sorted_scores) // 2]


if __name__ == "__main__":
    file = "input_files/problem10.txt"
    data = read_data(file)

    choice = input("press 1 or 2\n")
    if not choice in ("1", "2"):
        raise ValueError("invalid choice")

    if choice == "1":
        answer = score_part1(data)
        print(f"the answer to part 1 is {answer}")
    else:
        answer = score_part2(data)
        print(f"the answer to part 2 is {answer}")
