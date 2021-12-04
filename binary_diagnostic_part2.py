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