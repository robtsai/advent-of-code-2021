import copy

with open("input_files/problem4.txt", 'r') as f:
	bingo_nums = [int(x) for x in f.readline().split(',')]

	remainder = f.read()


boardlines = remainder.split("\n")
boardlinesclean = [x for x in boardlines if x != ""]


# boards are in rows of 5
boards = []
currboard = []
counter = 0


def clean_line(someline):
	arr = someline.strip().split(' ')
	arr_no_empty = [int(x) for x in arr if x != '']
	return arr_no_empty

while counter < len(boardlinesclean):
	if counter % 5 == 0 and counter != 0:
		boards.append(currboard)
		currboard = []
	currboard.append(clean_line(boardlinesclean[counter]))
	counter += 1
boards.append(currboard)


def check_bingo(board):
	'''sums all rows and cols to check bingo
	'''
	rowsums = [sum(row) for row in board]
	numrows, numcols = len(board), len(board[0])
	colsums = [0 for _ in range(numcols)]
	for i in range(numrows):
		for j in range(numcols):
			colsums[j] += board[i][j]
	bingoval = -numrows
	if any([x == bingoval for x in rowsums]):
		return True
	if any([x == bingoval for x in colsums]):
		return True
	return False


def mark_board(board, num):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == num:
				board[i][j] = -1
	return


def calc_score(board):
	''' sums all rows ignores -1'''
	total = 0
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] != -1:
				total += board[i][j]
	return total

def play_game_part1(boards, bingo_nums):
	for num in bingo_nums:
		for board in boards:
			mark_board(board, num)
		for board in boards:
			if check_bingo(board):
				print("we have a winner")
				print(board)
				print(num)
				board_score = calc_score(board)
				print(f"answer is {board_score * num}")
				return
	return

def play_game_part2(boards, bingo_nums):
	boards = copy.deepcopy(boards)
	found_a_winner = False
	for num in bingo_nums:
		boards_to_play = [True for _ in range(len(boards))]
		for board in boards:
			mark_board(board, num)
		for i, board in enumerate(boards):
			if check_bingo(board):
				boards_to_play[i] = False  # don't play next round
		boards = [ board for i, board in enumerate(boards) if boards_to_play[i] ]
		if len(boards) == 1:
			print("we have a winner")
			winner = boards[0]
			return winner
	raise ValueError("no valid winnner! too many or too few")


if __name__ == '__main__':
	choice = input("enter 1 or 2 to execute part 1 or 2 solution\n")
	if not choice in ['1', '2']:
		raise ValueError("pick 1 or 2")

	if choice == '1':
		play_game_part1(boards, bingo_nums)
	if choice == '2':
		winning_board = play_game_part2(boards, bingo_nums)
		play_game_part1([winning_board], bingo_nums)
		
