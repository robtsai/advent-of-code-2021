# from https://www.youtube.com/watch?v=kXvVwvykwQw&t=71s


file = "input_files/problem20.txt"

with open(file, "r") as f:
    data = f.read()

algo, img = data.strip().split("\n\n")


g = set()

for r, line in enumerate(img.strip().split("\n")):
    for c, char in enumerate(line):
        if char == "#":
            g.add((r, c))


def print_grid(g):
    rvals = [p[0] for p in g]
    minr, maxr = min(rvals), max(rvals)
    cvals = [p[1] for p in g]
    minc, maxc = min(cvals), max(cvals)
    for r in range(minr - 2, maxr + 3):
        for c in range(minc - 2, maxc + 3):
            if (r, c) in g:
                print("#", end="")
            else:
                print(".", end="")
        print()


print_grid(g)


def enhance(g, light):
    g2 = set()
    rvals = [p[0] for p in g]
    minr, maxr = min(rvals), max(rvals)
    cvals = [p[1] for p in g]
    minc, maxc = min(cvals), max(cvals)
    for r in range(minr - 2, maxr + 3):
        for c in range(minc - 2, maxc + 3):
            binstr = ""
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if light:
                        binstr += "0" if (r + dr, c + dc) in g else "1"
                    else:
                        binstr += "1" if (r + dr, c + dc) in g else "0"
            if light and algo[int(binstr, 2)] == "#":
                g2.add((r,c))
            if not light and algo[int(binstr, 2)] == ".":
                g2.add((r,c))
    return g2



for t in range(50):
    if t == 2:
        print(f"part 1 is {len(g)}")
    g = enhance(g, t%2)
    
print(f"part 2 is {len(g)}")    
