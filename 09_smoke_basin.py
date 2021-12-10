import math


def read_data(file):
    output = []
    with open(file, "r") as f:
        for line in f:
            nums = [int(x) for x in line.replace("\n", "")]
            output.append(nums)
    return output


def add_borders(board):
    """since we need to test for mins, lets add borders of inf"""
    board_len = len(board[0])
    output = []
    inf_row = [math.inf for _ in range(board_len + 2)]
    output.append(inf_row)
    for row in board:
        output.append([math.inf] + row + [math.inf])
    output.append(inf_row)
    return output


def lower_than_neighbor(i, j, b):
    """b is a bordered board"""
    val = b[i][j]
    if (
        val < b[i - 1][j]
        and val < b[i + 1][j]
        and val < b[i][j - 1]
        and val < b[i][j + 1]
    ):
        return True
    else:
        return False


def find_lowest(bordered_board):
    row_len = len(bordered_board[0])
    board_height = len(bordered_board)
    min_arr = []
    for i in range(1, board_height - 1):
        for j in range(1, row_len - 1):
            if lower_than_neighbor(i, j, bordered_board):
                min_arr.append(bordered_board[i][j])
    # strip out borders before returning
    return min_arr


def risk_level(arr):
    return sum(x + 1 for x in arr)


if __name__ == "__main__":
    inputfile = "input_files/problem9.txt"
    board = read_data(inputfile)

    choice = input("enter 1 or 2 for answer\n")
    if not choice in ("1", "2"):
        raise ValueError("pick 1 or 2")

    if choice == "1":
        board_with_borders = add_borders(board)
        lowest = find_lowest(board_with_borders)
        score = risk_level(lowest)
        print(f"the answer to part 1 is {score}")
