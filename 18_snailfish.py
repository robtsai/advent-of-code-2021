# copied from hyperneutrino
# https://www.youtube.com/watch?v=Vl26b-QXsS8
import sys
from copy import deepcopy

m = []

def convert(x):
    if isinstance(x, int):
        return [x]
    else:
        return [convert(e) for e in x]



with open("input_files/problem18.txt") as f:
    for line in f:
        m.append(convert(eval(line)))


def addleft(x, v):
    if x is None: return
    if len(x) == 1:
        x[0] += v 
    else:
        addleft(x[0], v)

def addright(x, v):
    if x is None: return 
    if len(x) == 1:
        x[0] += v 
    else:
        addright(x[1], v)


def split(x):
    if len(x) == 1:
        if x[0] >= 10:
            x[:] = [[x[0] // 2], [-(-x[0] // 2)]]
            return True
        else:
            return False
    else:
        return split(x[0]) or split(x[1])


def explode(x, l=None, r=None, d=0):
    if len(x) == 1:
        return False
    if d >= 4 and len(x[0]) == len(x[1]) == 1:
        addright(l, x[0][0])
        addleft(r, x[1][0])
        x[:] = [0] 
        return True
    return explode(x[0], l, x[1], d+1) or explode(x[1], x[0], r, d+1)


def reduce(x):
    while explode(x) or split(x):
        pass

def mag(x):
    if len(x) == 1:
        return x[0]
    else:
        return 3 * mag(x[0]) + 2 * mag(x[1])

a = m[0]
for k in m[1:]:
    a = [a, k]
    reduce(a)

print(a)
print(mag(a))

