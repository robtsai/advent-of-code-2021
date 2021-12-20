import heapq 


def get_data(file):
    board = []
    with open(file, 'r') as f:
        for line in f:
            board.append([int(x) for x in line.replace("\n", "")])
    return board



def find_adjacent(i, j, board, cost):
    rows = len(board)
    cols = len(board[0])

    adjacent = [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]
    valid = [(r, c) for r,c in adjacent if r >=0 and r < rows and c >= 0 and c < cols]
    valid_with_cost = [(cost+board[r][c], r,c) for r,c in valid]
    return valid_with_cost



def findpath(board):
    rows = len(board)
    cols = len(board[0])
    target = (rows-1, cols-1)

    # running cost, row, col
    explore = [(0,0,0)]
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




if __name__ == "__main__":
    file = "input_files/problem15.txt"
    board = get_data(file)
    cost = findpath(board)
    print(f"The answer to part 1 is {answer}")