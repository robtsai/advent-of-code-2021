# solution taken from reddit
# https://www.reddit.com/r/adventofcode/comments/rhj2hm/2021_day_16_solutions/

bs = bin(int('1'+open("input_files/problem16.txt").read(),16))[3:]

def ps1(startbit):
    i = startbit # index into bs
    tv = int(bs[i:i+3],2) # total version
    ID = int(bs[i+3:i+6],2) # packet type ID
    i += 6
    if ID == 4: #literal value
        while True:
            i += 5
            if bs[i-5] == '0': #last value packet
                break
    else:
        if bs[i] == '0':
            endi = i + 16 + int(bs[i+1:i+16],2)
            i += 16
            while i < endi:
                i,v = ps1(i)
                tv += v
        else:
            np = int(bs[i+1:i+12],2)
            i += 12
            for _ in range(np):
                i,v = ps1(i)
                tv += v

    return i,tv

print("Total of version numbers:",ps1(0)[1])


### PART 2 ###

import math

op = [sum, math.prod, min, max,
      lambda ls: ls[0], # literal
      lambda ls: 1 if ls[0] > ls[1] else 0,  # gt
      lambda ls: 1 if ls[0] < ls[1] else 0,  # lt
      lambda ls: 1 if ls[0] == ls[1] else 0] # eq

def ps2(startbit):
    i = startbit # index into bs
    ID = int(bs[i+3:i+6],2) # packet type ID
    i += 6
    if ID == 4: #literal value
        vals = [0]
        while True:
            vals[0] = 16*vals[0] + int(bs[i+1:i+5],2)
            i += 5
            if bs[i-5] == '0': #last value packet
                break
    else:
        vals = []
        if bs[i] == '0': # subpacket length in bits
            endi = i + 16 + int(bs[i+1:i+16],2)
            i += 16
            while i < endi:
                i,v = ps2(i)
                vals.append(v)
        else:
            np = int(bs[i+1:i+12],2) # number of subpackets
            i += 12
            for _ in range(np):
                i,v = ps2(i)
                vals.append(v)

    return i,op[ID](vals)

print('Total value:',ps2(0)[1])