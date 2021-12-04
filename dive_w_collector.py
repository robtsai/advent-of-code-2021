# dive - using collector

#  forward, depth
collector = [0, 0]


def parse_line(command_line, collector):
    """
    takes a command, and parses it
    """
    forward, depth = collector
    direction, units_str = command_line.strip().replace("\n", "").split(" ")
    units = int(units_str)
    if direction == "forward":
        forward += units
    elif direction == "down":
        depth += units
    elif direction == "up":
        depth -= units
    else:
        raise ValueError("invalid line")

    collector[0], collector[1] = forward, depth
    return


with open("input_files/problem2.txt", "r") as f:
    for line in f:
        parse_line(line, collector)

forward, depth = collector

print(f"forward is {forward}, depth is {depth}")
print(f"the answer is {forward * depth}")
