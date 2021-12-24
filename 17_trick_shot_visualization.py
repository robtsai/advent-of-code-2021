# this script just does visualization on the 17th day test problem

import re
import pprint
from collections import namedtuple
import time

pp = pprint.PrettyPrinter(indent=2)

Target = namedtuple("Target", "xl xh yl yh")
Board = namedtuple("Board", "board xtrarows")

instr = "target area: x=253..280, y=-73..-46"

test = "target area: x=20..30, y=-10..-5"

re_x = re.compile("x=(-?[0-9]+\.{2}-?[0-9]+),")
re_y = re.compile("y=(-?[0-9]+\.{2}-?[0-9]+)")


def parse_rule(rule):
    x = re_x.search(rule)
    x_low, x_high = x.group(1).split("..")
    y = re_y.search(rule)
    y_low, y_high = y.group(1).split("..")
    return Target(int(x_low), int(x_high), int(y_low), int(y_high))


def gen_board(target: Target, extrarows: int) -> str:
    output = []
    for y in range(0, target.yl - 1, -1):
        blank_row = ["." for _ in range(target.xh + 1)]
        output.append(blank_row)
    output[0][0] = "S"
    for r in range(-target.yh, -target.yl + 1):
        for c in range(target.xl, target.xh + 1):
            output[r][c] = "T"

    extra_rows = [["." for _ in range(target.xh + 1)] for _ in range(extrarows)]
    newboard = extra_rows + output

    return Board(newboard, extrarows)


def printboard(board):
    pp.pprint(["".join(row) for row in board.board])




def simulate(board, target, xv, yv, printbool):
    """simulate board with xv and yv"""
    # y velocity always decreases by 1, so 5, 4, 3, 2, 1
    # 1, 3, 6, 10, 15, 21

    r, c = 0 + board.xtrarows, 0
    while True:
        r, c = r + -yv, c + xv
        if c >= target.xh + 1 or r >= -target.yl + board.xtrarows:
            break
        try:  # haccky - index out of range
            if board.board[r][c] == "T":
                board.board[r][c] = "#"
                if printbool:
                    printboard(board)
                    print("hit target!")
                return True
        except IndexError:
            return False
        board.board[r][c] = "#"
        if printbool:
            printboard(board)
            print("------next step -----" * 3)
            time.sleep(1)
        yv = yv - 1
        if xv > 0:
            xv -= 1
        elif xv < 0:
            xv += 1
        else:
            xv = 0
    if printbool:
        print(f"missed target. final position {r-board.xtrarows} {c}")
    return False


target = parse_rule(test)
board = gen_board(target, 10)

simulate(board, target, 6, 3, True)

