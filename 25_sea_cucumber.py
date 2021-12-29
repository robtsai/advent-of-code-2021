import pprint

file = "input_files/problem25.txt"

pp = pprint.PrettyPrinter(indent=2)

board = []

with open(file, "r") as f:
    for line in f:
        board.append([char for char in line.replace("\n", "")])


rows = len(board)
cols = len(board[0])
pp.pprint(board)

print(rows)
print(cols)


def find(animal, board):
    locs = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == animal:
                locs.append((i,j))
    return locs


def move(board, step=0, keepgoing=True):
    """takes a board, makes a step, mutates the board and increments step
    will keep going until no valid moves"""
    step += 1
    e = find(">", board)
    s = find("v", board)
    e_to_move = [(r,c) for r,c in e if movable(">", r, c, e, s)]
    move_animals(">", e_to_move, board)
    e = find(">", board)    
    s_to_move = [(r,c) for r,c in s if movable("v", r, c, e, s)]
    move_animals("v", s_to_move, board)
    if len(e_to_move) + len(s_to_move) == 0:
        keepgoing = False
    print(f"we moved {len(e_to_move) + len(s_to_move)} animals on step {step}")
    return step, keepgoing



def move_animals(animal, movableanimals, board):
    if animal == ">":
        for i,j in movableanimals:
            nexti = i 
            nextj = (j+1) % cols 
            board[nexti][nextj] = ">"
            board[i][j] = "."
    elif animal == "v":
        for i,j in movableanimals:
            nexti = (i + 1) % rows 
            nextj = j
            board[nexti][nextj] = "v"
            board[i][j] = "."
    else:
        raise ValueError("invalid animal")
    return




def movable(animal, i, j, e, s):
    """for an animal type at i, j and a board check to see if it can move next turn"""
    if animal == ">":
        nexti = i 
        nextj = (j + 1) % cols
    elif animal == "v":
        nexti = (i+1) % rows
        nextj = j
    else:
        raise ValueError("invalid animal")
    return (nexti, nextj) not in (e + s)


keepgoing = True
step = 0
while keepgoing:
    step, keepgoing = move(board, step, keepgoing)
    print(step, keepgoing)
    
pp.pprint(board)


print(f"The answer to part 1 is {step}")

