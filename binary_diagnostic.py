
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