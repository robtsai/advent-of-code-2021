# from anthony writes code
# https://www.youtube.com/watch?v=KFwI1r3KDFQ


instr = "target area: x=253..280, y=-73..-46"

_, _, xs, ys = instr.split()
xs = xs[2:-1]
ys = ys[2:]

x1_s, x2_s = xs.split('..')
y1_s, y2_s = ys.split('..')

x1, x2, y1, y2 = int(x1_s), int(x2_s), int(y1_s), int(y2_s)

print(x1, x2, y1, y2)

max_y = 0
ways = []

for y in range(y1, abs(y1)):
    for x in range(1, x2 + 1):
        vx, vy = x, y
        x_p = y_p = 0
        max_y_path = 0
        for t in range(2 * abs(y1) + 2):
            x_p += vx
            y_p += vy
            vx = max(vx-1, 0)
            vy -= 1

            max_y_path = max(max_y_path, y_p)

            if x1 <= x_p <= x2 and y1 <= y_p <= y2:
                max_y = max(max_y, max_y_path)
                ways.append((x,y))
                break
            elif x_p > x2 or y_p < y1:
                break

print(f"part 1: {max_y}")


print(f"part 2: {len(ways)}")

