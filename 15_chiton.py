import heapq
import pprint

pp = pprint.PrettyPrinter(indent=2)


def get_data(file):
    board = []
    with open(file, "r") as f:
        for line in f:
            board.append([int(x) for x in line.replace("\n", "")])
    return board


def find_adjacent(i, j, board, cost):
    rows = len(board)
    cols = len(board[0])

    adjacent = [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]
    valid = [(r, c) for r, c in adjacent if r >= 0 and r < rows and c >= 0 and c < cols]
    valid_with_cost = [(cost + board[r][c], r, c) for r, c in valid]
    return valid_with_cost


def findpath(board):
    rows = len(board)
    cols = len(board[0])
    target = (rows - 1, cols - 1)

    # running cost, row, col
    explore = [(0, 0, 0)]
    heapq.heapify(explore)
    visited = set()

    while explore:
        lowest = heapq.heappop(explore)
        cost, r, c = lowest
        if lowest in visited:
            continue
        if (r, c) == target:
            return cost

        visited.add(lowest)
        adjacent = find_adjacent(r, c, board, cost)
        for node in adjacent:
            heapq.heappush(explore, node)


# bigboard does not work - the modulo is off,
# and this is too slow - lets move on to next day and come back later

def bigboard(board, n):
    """takes a board and resizes it by n"""
    rows = len(board)
    cols = len(board[0])

    newrow = [0 for _ in range(cols * n)]
    newboard = [newrow[:] for _ in range(rows * n)]

    for i in range(rows * n):
        for j in range(cols * n):
            orig_i = i % rows
            orig_j = j % cols
            i_mult = i // rows
            j_mult = j // cols
            old_val = board[orig_i][orig_j]
            new_val = (old_val + i_mult + j_mult) % 10
            newboard[i][j] = new_val
    return newboard


if __name__ == "__main__":
    choice = input("choose 1 or 2\n")
    if not choice in ("1", "2"):
        raise ValueError("invalid choice")

    if choice == "1":
        file = "input_files/problem15.txt"
        board = get_data(file)
        cost = findpath(board)
        print(f"The answer to part 1 is {cost}")
    else:
        print("not implemented")

