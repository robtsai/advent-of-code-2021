import math

def get_crabs(path):
    with open(path, "r") as f:
        line = f.readline()
        arr = line.strip().replace("\n", "").split(",")
        arr_ints = [int(x) for x in arr]
        return arr_ints

def num_step(arr):
    s = sorted(arr)
    l = len(s)
    print(l)
    if l % 2 == 1:
        print('odd')
        mid1, mid2 = l // 2, None
    else:
        print('even')
        mid1, mid2 = l // 2, l // 2 - 1

    print(mid1,mid2)

    moves1 = [abs(s[i] - s[mid1]) for i, _ in enumerate(s)]
    steps1 = sum(moves1)

    if mid2 is None:
        steps2 = math.inf
    else:
        moves2 = [abs(s[i] - s[mid2]) for i, _ in enumerate(s)]
        steps2 = sum(moves2)
    print(steps1,steps2)
    return min(steps1, steps2)



if __name__ == "__main__":
    inputfile = "input_files/problem7.txt"
    crabs = get_crabs(inputfile)
    print(f"answer to part1 is {num_step(crabs)}")