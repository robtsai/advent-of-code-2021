import math
import copy
import pprint

pp = pprint.PrettyPrinter(indent=4)

rules = []


maxx = 0
maxy = 0

inputfile = "input_files/problem5.txt"

with open(inputfile, "r") as f:
    for line in f:
        l, r = line.strip().split(" -> ")
        t = (l.split(","), r.split(","))
        tl, tr = ([int(x) for x in t[0]], [int(x) for x in t[1]])
        x1, y1 = tl
        x2, y2 = tr
        maxx = max(maxx, x1, x2)
        maxy = max(maxy, y1, y2)
        rules.append((x1, y1, x2, y2))


# confusing - y is row index, x is col index
# matrix iter i, j : i is row, j is col
# x, y coord - x is col index, y is row offset
samplerow = [0 for _ in range(maxx + 1)]

board = [samplerow[:] for _ in range(maxy + 1)]

board2 = copy.deepcopy(board)


def traverse(board, x1, y1, x2, y2):
    if y1 == y2:
        horizontal(board, x1, x2, y1)
    elif x1 == x2:
        vertical(board, y1, y2, x1)


def traverse_diag(board, x1, y1, x2, y2):
    if y1 == y2:
        horizontal(board, x1, x2, y1)
    elif x1 == x2:
        vertical(board, y1, y2, x1)
    else:
        diagonal(board, x1, y1, x2, y2)


def horizontal(board, x1, x2, y):
    x1, x2 = min(x1, x2), max(x1, x2)
    for j in range(x1, x2 + 1):
        board[y][j] += 1


def vertical(board, y1, y2, x):
    y1, y2 = min(y1, y2), max(y1, y2)
    for i in range(y1, y2 + 1):
        board[i][x] += 1


def diagonal(board, x1, y1, x2, y2):
    """this is buggy - don't use it"""
    points = []

    if x1 < x2 and y1 < y2:
        step_tuple = (1, 1)
    elif x1 < x2 and y1 > y2:
        step_tuple = (1, -1)
    elif x1 > x2 and y1 < y2:
        step_tuple = (-1, 1)
    else:
        step_tuple = (-1, -1)

    cur_x = x1
    cur_y = y1
    while cur_x != x2:
        points.append((cur_x, cur_y))
        x_step, y_step = step_tuple
        cur_x += x_step
        cur_y += y_step
    points.append((cur_x, cur_y))

    for i, j in points:
        board[i][j] += 1


#  part 1

for x1, y1, x2, y2 in rules:
    traverse(board, x1, y1, x2, y2)


overlaps = 0

for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] > 1:
            overlaps += 1

print(f"part 1 overlaps is {overlaps}")


# part 2 - there is a bug here - use answer from bottom sections

for x1, y1, x2, y2 in rules:
    traverse_diag(board2, x1, y1, x2, y2)

overlaps2 = 0

for i in range(len(board2)):
    for j in range(len(board2[0])):
        if board2[i][j] > 1:
            overlaps2 += 1

print(f"part 2 overlaps is {overlaps2}")
# pp.pprint(board2)

# part 2 try again
# let's iterate through the rules
# and use the rule to generate a list of points to be filled


def gen_points(x1, y1, x2, y2):
    ystep = 1 if y2 > y1 else -1
    xstep = 1 if x2 > x1 else -1

    if x1 == x2:
        direction = "horizontal"
        points = [(x1, y) for y in range(y1, y2 + ystep, ystep)]
    elif y1 == y2:
        direction = "vertical"
        points = [(x, y1) for x in range(x1, x2 + xstep, xstep)]
    else:
        direction = "diagonal"
        curr_x = x1
        curr_y = y1
        points = []
        while curr_x != x2 + xstep:
            points.append((curr_x, curr_y))
            curr_x += xstep
            curr_y += ystep
    return x1, y1, x2, y2, direction, points


enhanced_rules = []
for x1, y1, x2, y2 in rules:
    enhanced_rules.append((gen_points(x1, y1, x2, y2)))

# now just iterat through rules, use a hash set to count number of points

board2_dict = {}
for _, _, _, _, _, points in enhanced_rules:
    for point in points:
        board2_dict[point] = board2_dict.get(point, 0) + 1


# number of points
answer2 = sum([1 for v in board2_dict.values() if v > 1])
print(f"the answer for part 2 - trying to fix bug is {answer2}")

