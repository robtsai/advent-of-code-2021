import re
import pprint

pp = pprint.PrettyPrinter(indent=2)

point = re.compile("([0-9]+),([0-9]+)")
instr = re.compile("fold along (x|y)=([0-9]+)")


# remember - always convert strings to ints!!!
def get_data(file):
    output = []

    points = []
    folds = []

    with open(file, "r") as f:
        for line in f:
            p = point.match(line)
            i = instr.match(line)
            if p:
                newpoint = (int(p.group(1)), int(p.group(2)))
                points.append(newpoint)
            elif i:
                newinstr = (i.group(1), int(i.group(2)))
                folds.append(newinstr)
    return points, folds


def max_x_y(points):
    """returns largest offset in x (horiz-row) and y (vert-col)"""
    x = max([p[0] for p in points])
    y = max(p[1] for p in points)
    return (x, y)


def gen_board(points):
    maxx, maxy = max_x_y(points)
    board = []
    row = [0 for _ in range(maxx + 1)]
    for j in range(maxy + 1):
        # careful you need to copy a new row each time or it keeps reference
        board.append(row[:])
    return board


def pretty_print(board):
    m = {0: ".", 1: "#", -1: "-"}
    rows, cols = len(board), len(board[0])
    b = [[None for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            b[i][j] = m[board[i][j]]
    for r in b:
        pp.pprint("".join(r))


def fill_points(board, points):
    """points are x, y where x is horiz offset and y is vert offset"""
    for p in points:
        x, y = p
        board[y][x] = 1
    return board


def blank_board(board, orientation, divider):
    """orientation is x , y, divider is index to fold on
    e.g. y=7 means fold up on vertical offset 7"""
    new_board = []
    # gen blank board
    if orientation == "y":
        # keep row length
        row = [-1 for _ in range(len(board[0]))]
        for j in range(divider):
            new_board.append(row[:])
    elif orientation == "x":
        # gen row of length divider to fold left
        row = [-1 for _ in range(divider)]
        for j in range(len(board)):
            new_board.append(row[:])
    return new_board

# assumes square folds (works on part 1 not on part 2)
# we get index out of range on part 2
def fold_board(board, orientation, divider):
    print(f"folding {orientation}={divider}")
    new_board = blank_board(board, orientation, divider)
    if orientation == "x":
        for i in range(len(board)):
            l, r = 0, divider + divider
            while l < divider:
                new_board[i][l] = board[i][l] | board[i][r]
                l += 1
                r -= 1
    elif orientation == "y":
        toprow = 0
        bottomrow = divider + divider
        print(bottomrow)
        print(len(board))
        while toprow < divider:
            for j in range(len(board[0])):
                new_board[toprow][j] = board[toprow][j] | board[bottomrow][j]
            toprow += 1
            bottomrow -= 1
    pretty_print(new_board)
    return new_board


# better to set pointers from divider and move outward?
def better_board(board, orientation, divider):
    print(f"folding {orientation}={divider}")
    new_board = blank_board(board, orientation, divider)

    if orientation == "x":
        for i in range(len(board)):
            l, r = divider-1, divider+1
            while l >=0:
                if r < len(board[0]):
                    new_board[i][l] = board[i][l] | board[i][r]
                else:
                    new_board[i][l] = board[i][l]
                l -= 1
                r += 1
    elif orientation == "y":
        for j in range(len(board[0])):
            t, b = divider -1, divider+1
            while t >=0:
                if b < len(board):
                    new_board[t][j] = board[t][j] | board[b][j]
                else:
                    new_board[t][j] = board[t][j]
                t -= 1
                b += 1
    pretty_print(new_board)
    return new_board





def count_dots(board):
    return sum(sum(row) for row in board)

def run_part_1(points, folds):
    board = gen_board(points)
    filled_board = fill_points(board,points)
    first_fold = folds.pop(0)
    orientation, divider = first_fold
    filled_board = fold_board(filled_board, orientation, divider)
    return count_dots(filled_board)
    

def run_part_2(points, folds):
    board = gen_board(points)
    filled_board = fill_points(board,points)
    while folds:
        fold = folds.pop(0)
        orientation, divider = fold
        filled_board = better_board(filled_board, orientation, divider)
    


if __name__ == "__main__":
    choice = input("pick 1 or 2\n")
    if choice == "1":
        file = "input_files/problem13.txt"
        points, folds = get_data(file)
        answer = run_part_1(points, folds)
        print(f"answer to part 1 is {answer}")
    elif choice == "2":
        file = "input_files/problem13.txt"
        points, folds = get_data(file)
        answer = run_part_2(points, folds)
