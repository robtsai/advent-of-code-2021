# part 2

# dive - using collector

#  horizontal, depth, aim
collector = [0, 0, 0]


def parse_line(command_line, collector):
    """
    takes a command, and parses it
    """
    horizontal, depth, aim = collector
    direction, units_str = command_line.strip().replace("\n", "").split(" ")
    units = int(units_str)
    if direction == "forward":
        horizontal += units
        depth += aim * units
    elif direction == "down":
        aim += units
    elif direction == "up":
        aim -= units
    else:
        raise ValueError("invalid line")

    collector[0], collector[1], collector[2] = horizontal, depth, aim
    return


with open("input_files/problem2.txt", "r") as f:
    for line in f:
        parse_line(line, collector)

forward, depth, aim = collector

print(f"forward is {forward}, depth is {depth}")
print(f"the answer is {forward * depth}")
