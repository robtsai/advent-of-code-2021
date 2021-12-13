import pprint
from collections import defaultdict

pp = pprint.PrettyPrinter(indent=1)


def get_data(file):
    output = []
    with open(file, "r") as f:
        for line in f:
            signal, result = line.replace("\n", "").split("|")
            signal = signal.strip().split(" ")
            result = result.strip().split(" ")
            output.append((signal, result))
    return output


testprint = True

#    a b c d e f g
# 0  1 1 1 0 1 1 1
# 1  0 0 1 0 0 1 0
# 2  1 0 1 1 1 0 1
# 3  1 0 1 1 0 1 1
# 4  0 1 1 1 0 1 0
# 5  1 1 0 1 0 1 1
# 6  1 1 0 1 1 1 1
# 7  1 0 1 0 0 1 0
# 8  1 1 1 1 1 1 1
# 9  1 1 1 1 0 1 1

m = {
    0: "1110111",
    1: "0010010",
    2: "1011101",
    3: "1011011",
    4: "0111010",
    5: "1101011",
    6: "1101111",
    7: "1010010",
    8: "1111111",
    9: "1111011",
}

# not needed
# m2 = {k: bin(int(v, base=2)) for k, v in m.items()}


chart = []

for i in range(10):
    chart.append([char for char in m[i]])


# convention word4 means word with 4 chars
# num4 means word representing number 4


def find_a_map(line):
    """derives the letter mapping to f"""
    signal, _ = line
    word2 = [x for x in signal if len(x) == 2]
    word3 = [x for x in signal if len(x) == 3]
    aas = set(*word3) - set(*word2)
    (a,) = aas
    return a


def word_in_list(word, wordlist):
    # returns first word from wordlist that matches
    s = set(word)
    subset_bools = [s.issubset(x) for x in wordlist]
    first_match_index = subset_bools.index(True)
    first_match = wordlist[first_match_index]
    return first_match


def find_e_map(line, nums):
    """derives e by using 4 and 9"""
    signal, _ = line
    words4 = [x for x in signal if len(x) == 4]
    word4 = words4[0]
    words6 = [x for x in signal if len(x) == 6]
    num_9 = word_in_list(word4, words6)
    e_set = set(nums[8]) - set(num_9)
    (e,) = e_set
    return e, num_9


def find_g_map(nums):
    g_set = set(nums[9]) - set(nums[4]) - set(nums[7])
    (g,) = g_set
    return g




def find_c_map(line, nums):
    signal, _ = line
    words6 = [x for x in signal if len(x) == 6]
    words6_no9 = [x for x in words6 if not set(x) == set(nums[9])]
    c_lookup = [set(nums[1]) - set(word) for word in words6_no9]
    c_boolean = [len(x) == 1 for x in c_lookup]
    c_set = c_lookup[c_boolean.index(True)]
    num_6 = words6_no9[c_boolean.index(True)]
    num_0 = words6_no9[c_boolean.index(False)]
    (c,) = c_set
    return c, num_6, num_0


def find_d_map(nums):
    d_set = set("abcdefg") - set(nums[0])
    (d,) = d_set
    return d


def find_f_map(line):
    signal, _ = line
    counter = defaultdict(lambda: 0)
    for word in signal:
        for char in word:
            counter[char] += 1
    # letter f maps to count of 9
    fs = {k for k,v in counter.items() if v == 9}
    (f,) = fs
    return f


def derive_number_from_chart(chart, whichnum, discovered):
    row = chart[whichnum]
    new_word = [discovered[i] for i,v in enumerate(row) if v == '1']
    return ''.join(new_word)


def decode_number(scrambled, nums):
    s = set(scrambled)
    for k, v in nums.items():
        if s == set(v):
            return k
    return




def process_line(line):
    signal, result = line
    nums = {}
    words2 = [x for x in signal if len(x) == 2]
    words4 = [x for x in signal if len(x) == 4]
    words3 = [x for x in signal if len(x) == 3]
    words7 = [x for x in signal if len(x) == 7]

    nums[1] = words2[0]
    nums[4] = words4[0]
    nums[7] = words3[0]
    nums[8] = words7[0]
    a = find_a_map(line)
    e, num_9 = find_e_map(line, nums)
    nums[9] = num_9
    g = find_g_map(nums)
    c, num_6, num_0 = find_c_map(line, nums)
    nums[6] = num_6
    nums[0] = num_0
    d = find_d_map(nums)
    f = find_f_map(line)
    known = ''.join([a, c, d, e, f, g])
    bs = set("abcdefg") - set(known)
    (b,) = bs
    discovered = [a, b, c, d, e, f, g]

    # we now know all the letters, need to derive 2, 3, 5
    nums[2] = derive_number_from_chart(chart, 2, discovered)
    nums[3] = derive_number_from_chart(chart, 3, discovered)
    nums[5] = derive_number_from_chart(chart, 5, discovered)

    decoded = [decode_number(x, nums) for x in result]
    if testprint:
        pprint_h(discovered)
        pp.pprint(nums)
        pp.pprint(decoded)

    outputval = ''.join([str(x) for x in decoded])
    return int(outputval)


def part2_answer(data):
    return sum([process_line(line) for line in data])


header1 = [["a", "b", "c", "d", "e", "f", "g"]]


def pprint_h(header):
    pp.pprint(header)
    pp.pprint(header1)
    pp.pprint(chart)


if __name__ == "__main__":
    file = "input_files/problem8.txt"
    data = get_data(file)
    answer = part2_answer(data)
    print(f"The answer to part 2 is {answer}")