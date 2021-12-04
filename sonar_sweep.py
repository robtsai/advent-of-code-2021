
depths = []

with open('./input_files/problem1.txt', 'r') as f:
	for line in f:
		depths.append(line.replace('\n', ''))


# part 1

depth_nums = [int(x) for x in depths]

diffs = [depth_nums[x] - depth_nums[x-1] for x in range(1, len(depth_nums))]

increasing = [x for x in diffs if x > 0]


# part 2

trailing = [sum(depth_nums[x:x+3]) for x in range(len(depth_nums)-2)]
zipped_trailing = list(zip(trailing, trailing[1:]))
inc_decr = [ x[1] - x[0] for x in zipped_trailing]
increasing_2 = [x for x in inc_decr if x > 0]

#### answers ####
print(f"part 1 answer is {len(increasing)}")
print(f"part 2 answer is {len(increasing_2)}")
