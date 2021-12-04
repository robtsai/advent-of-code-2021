## --- Day 4: Giant Squid ---

You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you _can_ see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play [bingo](https://en.wikipedia.org/wiki/Bingo_(American_version))?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is _marked_ on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board _wins_. (Diagonals don't count.)

The submarine has a _bingo subsystem_ to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

```
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
```

After the first five numbers are drawn (`7`, `4`, `9`, `5`, and `11`), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

```
22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
```

After the next six numbers are drawn (`17`, `23`, `2`, `0`, `14`, and `21`), there are still no winners:

```
22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
```

Finally, `24` is drawn:

```
22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
```

At this point, the third board _wins_ because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: `_14 21 17 24 4_`).

The _score_ of the winning board can now be calculated. Start by finding the _sum of all unmarked numbers_ on that board; in this case, the sum is `188`. Then, multiply that sum by _the number that was just called_ when the board won, `24`, to get the final score, `188 * 24 = _4512_`.

To guarantee victory against the giant squid, figure out which board will win first. _What will your final score be if you choose that board?_

## --- Part Two ---

On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to _figure out which board will win last_ and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after `13` is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to `148` for a final score of `148 * 13 = _1924_`.

Figure out which board will win last. _Once it wins, what would its final score be?_

```python
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
		

```