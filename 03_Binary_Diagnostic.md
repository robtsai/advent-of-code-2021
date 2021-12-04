## --- Day 3: Binary Diagnostic ---

The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the _power consumption_.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the _gamma rate_ and the _epsilon rate_). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the _most common bit in the corresponding position_ of all numbers in the diagnostic report. For example, given the following diagnostic report:

```
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
```

Considering only the first bit of each number, there are five `0` bits and seven `1` bits. Since the most common bit is `1`, the first bit of the gamma rate is `1`.

The most common second bit of the numbers in the diagnostic report is `0`, so the second bit of the gamma rate is `0`.

The most common value of the third, fourth, and fifth bits are `1`, `1`, and `0`, respectively, and so the final three bits of the gamma rate are `110`.

So, the gamma rate is the binary number `10110`, or `_22_` in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is `01001`, or `_9_` in decimal. Multiplying the gamma rate (`22`) by the epsilon rate (`9`) produces the power consumption, `_198_`.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. _What is the power consumption of the submarine?_ (Be sure to represent your answer in decimal, not binary.)

```python

inputfile = "input_files/problem3.txt"

def read_first_line(inputfile):
	'''returns empty dicts
	'''
	with open(inputfile, 'r') as f:
		l = f.readline().strip().replace('\n', '')
		l_len = len(l)
		collector = [{'0': 0, '1': 0} for _ in range(l_len)]
		return collector


def process_file(inputfile, collector):
	with open(inputfile, 'r') as f:
		for line in f:
			cleanline = line.strip().replace('\n', '')
			for i, c in enumerate(cleanline):
				collector[i][c] += 1
	return

def sort_dict(somedict):
	'''takes a dict and sorts by values desc, returns the higher key
	'''
	l = [(k,v) for k,v in somedict.items()]
	sorted_l = sorted(l, key=lambda x: x[1], reverse=True)
	return sorted_l[0][0]


def reverse_bits(somestr):
	''' expects all 0s and 1s '''
	if not all(c in '01' for c in somestr):
		raise ValueError("string is not all zeroes and ones")
	l = [ '1' if char=='0' else '0' for char in somestr ]
	return ''.join(l)

collector = read_first_line(inputfile)
process_file(inputfile, collector)

gamma_str = ''.join([ sort_dict(c) for c in collector])
gamma_int = int(gamma_str, base=2)
gamma_bin = bin(gamma_int)
eps_str = reverse_bits(gamma_str)
eps_int = int(eps_str, base=2)

print(f"the answer is {gamma_int * eps_int}")
```


## --- Part Two ---

Next, you should verify the _life support rating_, which can be determined by multiplying the _oxygen generator rating_ by the _CO2 scrubber rating_.

Both the oxygen generator rating and the CO2 scrubber rating are values that can be found in your diagnostic report - finding them is the tricky part. Both values are located using a similar process that involves filtering out values until only one remains. Before searching for either rating value, start with the full list of binary numbers from your diagnostic report and _consider just the first bit_ of those numbers. Then:

-   Keep only numbers selected by the _bit criteria_ for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
-   If you only have one number left, stop; this is the rating value for which you are searching.
-   Otherwise, repeat the process, considering the next bit to the right.

The _bit criteria_ depends on which type of rating value you want to find:

-   To find _oxygen generator rating_, determine the _most common_ value (`0` or `1`) in the current bit position, and keep only numbers with that bit in that position. If `0` and `1` are equally common, keep values with a `_1_` in the position being considered.
-   To find _CO2 scrubber rating_, determine the _least common_ value (`0` or `1`) in the current bit position, and keep only numbers with that bit in that position. If `0` and `1` are equally common, keep values with a `_0_` in the position being considered.

For example, to determine the _oxygen generator rating_ value using the same example diagnostic report from above:

-   Start with all 12 numbers and consider only the first bit of each number. There are more `1` bits (7) than `0` bits (5), so keep only the 7 numbers with a `1` in the first position: `11110`, `10110`, `10111`, `10101`, `11100`, `10000`, and `11001`.
-   Then, consider the second bit of the 7 remaining numbers: there are more `0` bits (4) than `1` bits (3), so keep only the 4 numbers with a `0` in the second position: `10110`, `10111`, `10101`, and `10000`.
-   In the third position, three of the four numbers have a `1`, so keep those three: `10110`, `10111`, and `10101`.
-   In the fourth position, two of the three numbers have a `1`, so keep those two: `10110` and `10111`.
-   In the fifth position, there are an equal number of `0` bits and `1` bits (one each). So, to find the _oxygen generator rating_, keep the number with a `1` in that position: `10111`.
-   As there is only one number left, stop; the _oxygen generator rating_ is `10111`, or `_23_` in decimal.

Then, to determine the _CO2 scrubber rating_ value from the same example above:

-   Start again with all 12 numbers and consider only the first bit of each number. There are fewer `0` bits (5) than `1` bits (7), so keep only the 5 numbers with a `0` in the first position: `00100`, `01111`, `00111`, `00010`, and `01010`.
-   Then, consider the second bit of the 5 remaining numbers: there are fewer `1` bits (2) than `0` bits (3), so keep only the 2 numbers with a `1` in the second position: `01111` and `01010`.
-   In the third position, there are an equal number of `0` bits and `1` bits (one each). So, to find the _CO2 scrubber rating_, keep the number with a `0` in that position: `01010`.
-   As there is only one number left, stop; the _CO2 scrubber rating_ is `01010`, or `_10_` in decimal.

Finally, to find the life support rating, multiply the oxygen generator rating (`23`) by the CO2 scrubber rating (`10`) to get `_230_`.

Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together. _What is the life support rating of the submarine?_ (Be sure to represent your answer in decimal, not binary.)

```python
import copy

inputfile = "input_files/problem3.txt"

# we need a data structure now, like a 2-d array, list of lists

def generate_matrix(inputfile):
	'''takes an inputfile, and returns a matrix'''
	matrix = []
	with open(inputfile, 'r') as f:
		for line in f:
			clean_line = line.strip().replace('\n', '')
			matrix.append([int(x) for x in clean_line])
	return matrix


def number_of_bits(matrix, colindex):
	''' returns number of 0s and 1s as tuple in the col of matrix, starts at index 0'''
	arr = [matrix[i][colindex] for i in range(len(matrix))]
	numzeroes = len([x for x in arr if x == 0])
	numones = len([x for x in arr if x == 1])
	return (numzeroes, numones)

def most_common(numzeroes, numones):
	''' returns most common 0 or 1 and 1 if equally common'''
	if numzeroes > numones:
		return 0
	elif numzeroes < numones:
		return 1
	else:
		return 1

def least_common(numzeroes, numones):
	''' returns least common 0 or 1 and 0 if equally common'''
	if numzeroes > numones:
		return 1
	elif numzeroes < numones:
		return 0
	else:
		return 0

def traverse_submatrix(m, colindex, comparisonfunc):
	'''takes a matrix, returns num of bits in col
	'''
	numzeroes, numones = number_of_bits(m,colindex)
	vals_to_keep = comparisonfunc(numzeroes, numones)
	m_to_return = [ row for row in m if row[colindex] == vals_to_keep]
	return m_to_return


def traverse_matrix(m, comparisonfunc):
	numrows = len(m)
	numcols = len(m[0])
	submatrix = copy.deepcopy(m)
	colcounter = 0
	while len(submatrix) > 1 and colcounter < numcols:
		submatrix = traverse_submatrix(submatrix, colcounter, comparisonfunc)
		colcounter += 1
	if len(submatrix) != 1:
		raise ValueError("we expect one row!")
	lastval_str = ''.join([str(x) for x in submatrix[0]])
	lastval_int = int(lastval_str, base=2)
	return lastval_int



matrix = generate_matrix(inputfile)
oxygen_rating = traverse_matrix(matrix, most_common)
scrubber_rating = traverse_matrix(matrix, least_common)

print(f"The answer is {oxygen_rating * scrubber_rating}")
```