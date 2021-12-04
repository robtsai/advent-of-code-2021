# dive - using function with return values


def parse_line(command_line, forward, depth):
	'''
	takes a command, and parses it
	'''
	direction, units_str = command_line.strip().replace('\n', '').split(" ")
	units = int(units_str)
	if direction == 'forward':
		forward += units
	elif direction == 'down':
		depth += units
	elif direction == 'up':
		depth -= units
	else:
		raise ValueError("invalid line")

	return (forward, depth)


with open('input_files/problem2.txt', 'r') as f:
	forward, depth = 0, 0
	for line in f:
		forward, depth = parse_line(line, forward, depth)

print(f"forward is {forward}, depth is {depth}")
print(f"the answer is {forward * depth}")

