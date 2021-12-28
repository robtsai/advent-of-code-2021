# from anthony writes code
# https://www.youtube.com/watch?v=rEyAbeV48tI

import itertools
from functools import lru_cache


# use itertools.cycle to simulate a die - much better than what i did on part 1

INPUT_S = '''\
Player 1 starting position: 9
Player 2 starting position: 10 
'''

lines = INPUT_S.splitlines()
_, _, _, _, p1_s = lines[0].split()
_, _, _, _, p2_s = lines[1].split()

p1, p2 = int(p1_s), int(p2_s)


def weird_mod(n: int) -> int:
    while n > 10:
        n -= 10
    return n 


@lru_cache(maxsize=None)
def compute_wins(
    p1: int,
    p1_score: int,
    p2: int,
    p2_score: int,
    p1_turn: bool,
) -> tuple[int, int]:

    if p1_turn:
        p1_wins = p2_wins = 0 
        # overlapping dies here - could be optimized with a counter
        for i, j, k in itertools.product((1,2,3), (1,2,3), (1,2,3)):
            new_p1 = weird_mod(p1 + i + j + k)
            new_p1_score = p1_score + new_p1

            if new_p1_score >= 21:
                p1_wins += 1
            else:
                tmp_p1_wins, tmp_p2_wins = compute_wins(
                    new_p1,
                    new_p1_score,
                    p2,
                    p2_score,
                    p1_turn = False
                )
                p1_wins += tmp_p1_wins
                p2_wins += tmp_p2_wins
        return p1_wins, p2_wins

    else:
        p1_wins = p2_wins = 0 
        for i, j, k in itertools.product((1,2,3), (1,2,3), (1,2,3)):
            new_p2 = weird_mod(p2 + i + j + k)
            new_p2_score = p2_score + new_p2

            if new_p2_score >= 21:
                p2_wins += 1
            else:
                tmp_p1_wins, tmp_p2_wins = compute_wins(
                    p1,
                    p1_score,
                    new_p2,
                    new_p2_score,
                    p1_turn = True
                )
                p1_wins += tmp_p1_wins
                p2_wins += tmp_p2_wins
        return p1_wins, p2_wins

wincounts = compute_wins(p1, 0, p2, 0, p1_turn=True)
largest = max(wincounts)

print(f"part2: {largest}")