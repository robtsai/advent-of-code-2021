def get_data(file):
    output = []
    with open(file, "r") as f:
        for line in f:
            signal, result = line.replace("\n", "").split("|")
            signal = signal.strip().split(" ")
            result = result.strip().split(" ")
            output.append((signal, result))
    return output


# maps num digits to digit value, ie if result has len 2 then it is 1
unique_digits = {2: 1, 3: 7, 4: 4, 7: 8}

master = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}


letter_index = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6}

letters = "abcdefg"
letter_counts = {k: sum([1 for word in master.values() if k in word]) for k in letters}
# we know f is in 9 patterms, and one pattern without f is number 2


def return_f(signal):
    letter_counts = {k: sum([1 for word in signal if k in word]) for k in letters}
    letter_f = [k for k, v in letter_counts.items() if v == 9]
    return letter_f[0]


def count_known_numbers(data):
    known = 0
    for _, result in data:
        for num in result:
            if len(num) in unique_digits.keys():
                known += 1
    return known


def convert_letter_to_arr(wire_letters):
    arr = [0 for _ in range(7)]
    for char in wire_letters:
        arr[letter_index[char]] = 1
    return arr


wire_lookup = {k: convert_letter_to_arr(v) for k, v in master.items()}
wire_reverse = {tuple(v): k for k,v in wire_lookup.items()}

def calc_output(line):
    print('calling output')
    signal, result = line
    # d maps the real letter to our scrambled letter in signal
    d = {}

    num_map = {}
    print(signal)
    m = {}
    for k, v in unique_digits.items():
        m[v] = set(*[i for i in signal if len(i) == k])

    # a:  1 has 2 values, 7 has 3 values, a is the value in 7 but not in 1
    d["a"] = (m[7] - m[1]).pop()
    print("da", d)

    letter_f = return_f(signal)
    d["f"] = letter_f
    print(m)

    reverse_d = {v: k for k, v in d.items()}

    # we know c is the third letter in m[7] that hasn't been mapped
    c = (m[7]) - set(d.values())
    d["c"] = c.pop()
    # b or d are m[4] but not in m[1]
    b_or_d = m[4] - m[1]

    m_2 = [x for x in signal if not letter_f in x][0]
    num_map[2] = set(*[m_2])
    print('calling nummap')
    print(num_map)
    b = [x for x in b_or_d if not x in num_map[2]][0]
    letter_d = [x for x in b_or_d if x in num_map[2]][0]
    d["b"] = b
    d["d"] = letter_d

    print("good")
    print(d)
    print(m)

    # we know m[9] is the one pattern in signal that is length 6
    # and contains our keys in d
    l6 = [x for x in signal if len(x) == 6]
    print("l6", l6)

    dset = set(d.keys())
    print(dset)
    l6_set = [set(x) for x in l6]
    print(l6_set)

    remaining  = [ s - dset for s in l6_set]

    num_9 = [x for x in l6 if sum([1 for char in x if char in d]) == 5]
    print(d)
    print("9", num_9)
    print(signal)
    m[9] = set(*num_9)

    g = (m[9] - set(d.values())).pop()
    d["g"] = g

    # e is the last letter
    e = (set("abcdefg") - set(d.values())).pop()
    d["e"] = e

    reverse_d = {v: k for k, v in d.items()}

    # lets use array 7 to represent wires
    def convert_result(pattern):
        new_word = "".join([reverse_d[char] for char in pattern])
        arr = convert_letter_to_arr(new_word)
        return tuple(arr)

    transformed = []
    for number in result:
        letters_as_arr = convert_result(number)
        digit = wire_reverse[letters_as_arr]
        transformed.append(digit)
    print(transformed)
    return ''.join([str(x) for x in transformed])


def sum_all_outputs(data):
    answers = []
    for line in data:
        answers.append(calc_output(line))
    print(answers)


# part 2 not working....

if __name__ == "__main__":
    choice = input("pick 1 or 2\n")
    if not choice in ("1", "2"):
        raise ValueError("invalid choice")

    file = "input_files/problem8.txt"
    testfile = "input_files/problem8.txt"
    if choice == "1":
        data = get_data(file)
        known = count_known_numbers(data)
        print(f"answer to part 1 is {known}")
    else:
        data = get_data(file)
        for line in data:
            calc_output(line)
