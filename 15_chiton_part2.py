
import heapq
import pprint

pp = pprint.PrettyPrinter(indent=2)


board = []
with open("input_files/problem15.txt", "r") as f:
    for line in f:
        board.append([int(x) for x in line.replace("\n", "")])

orig = board[:]


# 10 -> 1, 11 -> 2
# n - 1 mod 9 + 1

def expand(board, n):
    # takes board and makes it n times larger
    rows = len(board)
    cols = len(board[0])
    newboard = [[0 for _ in range(cols*n)] for _ in range(rows*n)]
    for i in range(rows*n):
        for j in range(cols*n):
            ii = i % rows
            jj = j % cols
            startval = board[ii][jj]
            i_offset = i // rows
            j_offset = j // cols
            newval = (startval + i_offset + j_offset - 1) % 9 + 1
            newboard[i][j] = newval
    return newboard


board = expand(board, 5)

rows = len(board)
cols = len(board[0])
target = (rows - 1, cols - 1)

# running cost, row, col
explore = [(0, 0, 0)]
heapq.heapify(explore)
visited = set()


while len(explore) > 0:
    lowest = heapq.heappop(explore)
    cost, r, c = lowest
    if (r, c) in visited:
        continue
    if (r, c) == target:
        print("found target")
        break

    visited.add((r,c))

    for r_offset, c_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_r, new_c = r + r_offset, c + c_offset
        if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
            continue
        heapq.heappush(explore, (cost + board[new_r][new_c], new_r, new_c))


print(f"The answer to part 2 is {cost}")

