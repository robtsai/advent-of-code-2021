def get_board(file):
    output = []
    with open(file, "r") as f:
        for line in f:
            output.append(line.replace("\n", ""))
    return output


def board_nums(board):
    return [[int(char) for char in row] for row in board]


def simulate(board, numsteps):
    d = {"flashes": 0}
    rows = len(board)
    cols = len(board[0])

    def transition(board, d):
        flashed = [[False for _ in range(cols)] for _ in range(rows)]
        to_flash = []

        # first round
        for i in range(rows):
            for j in range(cols):
                if flashed[i][j]:  # if already flashed
                    continue
                if board[i][j] == 9:
                    flashed[i][j] = True
                    board[i][j] = 0
                    d["flashes"] += 1
                    to_flash.append((i, j))
                else:
                    board[i][j] += 1

        while len(to_flash) > 0:
            f1, f2 = to_flash.pop()
            incr = [
                (f1 - 1, f2 - 1),
                (f1 - 1, f2),
                (f1 - 1, f2 + 1),
                (f1, f2 - 1),
                (f1, f2 + 1),
                (f1 + 1, f2 - 1),
                (f1 + 1, f2),
                (f1 + 1, f2 + 1),
            ]

            incr = [
                (i, j) for i, j in incr if i >= 0 and i < rows and j >= 0 and j < cols
            ]
            incr = [(i, j) for i, j in incr if not flashed[i][j]]
            # try to increment
            for i, j in incr:
                if board[i][j] == 9:
                    flashed[i][j] = True
                    board[i][j] = 0
                    d["flashes"] += 1
                    to_flash.append((i, j))
                else:
                    board[i][j] += 1
        # board and d are modified in place
        return

    for n in range(numsteps):
        transition(board, d)
    print(board)
    return d["flashes"]


if __name__ == "__main__":
    choice = input("pick 1 or 2\n")
    if not choice in ('1', '2'):
        raise ValueError("invalid choice")

    if choice == "1":
        file = "input_files/problem11.txt"
        board = get_board(file)
        b = board_nums(board)
        answer = simulate(b, 100)
        print(f"The asnwer for part 1 is {answer} flashes")
