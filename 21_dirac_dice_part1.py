with open("input_files/problem21.txt", "r") as f:
    player1 = int(f.readline().split(":")[-1])
    player2 = int(f.readline().split(":")[-1])


BOARD_SLOTS = 10
TARGET = 1000
ROLLS_PER_TURN = 3


class Die:
    # ie six sided rolls 1, 2, 3, 4, 5, 6, 1 ...
    def __init__(self, sides):
        self.sides = sides
        self.cur = 1
        self.val = (self.cur - 1) % (self.sides) + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.cur += 1
        self.val = (self.cur - 1) % (self.sides) + 1


class Player:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.score = 0

    def move_on_board(self, steps):
        """we are on a ten sided board, so we take steps mod 10 and add to cur pos.
        similar to our six sided die, we need to reset the position"""
        inc_steps = steps % BOARD_SLOTS
        self.pos = (self.pos - 1 + inc_steps) % BOARD_SLOTS + 1
        self.score += self.pos

    def __str__(self):
        return f"{self.name} has score {self.score} and is at {self.pos}"


def roll(die, numrolls):
    v = 0
    for i in range(numrolls):
        v += die.val
        next(die)
    return v


def playgame():
    d = Die(100)
    p1 = Player("p1", player1)
    p2 = Player("p2", player2)

    turns = 0
    winner = None
    loser = None

    while True:
        moves = roll(d, ROLLS_PER_TURN)
        p1.move_on_board(moves)
        print(p1)
        turns += 1

        if p1.score >= TARGET:
            winner = p1
            loser = p2
            break
        moves = roll(d, ROLLS_PER_TURN)
        p2.move_on_board(moves)
        turns += 1
        print(p2)

        if p2.score >= TARGET:
            winner = p2
            loser = p1
            break

    print(f"The winner is {winner.name}")
    print(f"The losing score {loser.score}")
    print(f"The number of turns is {turns}")
    print(f"The number of dice rolls is {turns * ROLLS_PER_TURN}")
    print(f"The answer to part 1 is {loser.score * turns * ROLLS_PER_TURN}")


playgame()
