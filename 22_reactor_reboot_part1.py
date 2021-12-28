# from youtube user: 0xdf
# https://www.youtube.com/watch?v=3bbREeww9w8


import re

file = "input_files/problem22.txt"

with open(file, "r") as f:
    lines = f.readlines()

g = set()
for line in lines:
    status, coords = line.split()
    x0, x1, y0, y1, z0, z1 = list(map(int, re.findall("-?\d+", coords)))
    print(status, x0, x1, y0, y1, z0, z1)
    x0 = max(x0, -50)
    x1 = min(x1, 50)
    y0 = max(y0, -50)
    y1 = min(y1, 50)
    z0 = max(z0, -50)
    z1 = min(z1, 50)
    print(status, x0, x1, y0, y1, z0, z1)

    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            for z in range(z0, z1+1):
                if status == "on":
                    g.add((x,y,z))
                else:
                    g.discard((x,y,z))


print(f"the answer to part 1 is {len(g)}")



