from collections import defaultdict


def get_data(file):
    with open(file, "r") as f:
        polymer = f.readline().replace("\n", "")
        blank = f.readline()
        rules_raw = []
        for line in f:
            rules_raw.append(line.replace("\n", ""))
    return polymer, rules_raw


def rules_raw_to_dict(rules_raw):
    d = {}
    for r in rules_raw:
        k, v = r.split(" -> ")
        d[k] = v
    return d


def initial_hash(polymer):
    h = defaultdict(lambda: 0)
    for i in range(len(polymer) - 1):
        k = polymer[i : i + 2]
        h[k] += 1
    return h


def apply_rules(h, rules):
    """modifies mutable h dictionary, reads the current entries, applies rules, then modifies h"""
    to_insert = defaultdict(lambda: 0)
    to_remove = defaultdict(lambda: 0)

    for k, v in h.items():
        insertion_char = rules[k]
        pattern1, pattern2 = k[0] + rules[k], rules[k] + k[1]
        to_insert[pattern1] += v
        to_insert[pattern2] += v
        to_remove[k] += v

    for k, v in to_insert.items():
        h[k] += v

    for k, v in to_remove.items():
        h[k] -= v

    remove_these = [k for k, v in h.items() if v == 0]
    for k in remove_these:
        del h[k]


def h_to_elements(h, polymer):
    # this is tricky, as imagine you have HNNBBCHNCCCBBNBC
    # HN: 2, NN: 1, NB:2, BB:2, BC:2, CH:1, NC: 1, CC:2, CB: 1, BN:1
    elements = defaultdict(lambda: 0)

    # lets make it a list of tuples first, we want to order it and take the largest one first
    t = sorted([(k, v) for k, v in h.items()], key=lambda x: x[1], reverse=True)

    # lets always just count first letters, because second letters always become first letters of the
    # next pair, but remember we have to add one extra last letter
    answer = defaultdict(lambda: 0)
    while t:
        pair, counter = t.pop(0)
        firstletter = pair[0]
        answer[firstletter] += counter

    extra = polymer[-1]
    answer[extra] += 1
    sorted_answer = sorted(
        [(k, v) for k, v in answer.items()], key=lambda x: x[1], reverse=True
    )
    largest = sorted_answer[0][1]
    smallest = sorted_answer[-1][1]
    return largest - smallest


def calc_answer(polymer, rules_raw, rounds):
    rules = rules_raw_to_dict(rules_raw)
    h = initial_hash(polymer)
    for i in range(rounds):
        apply_rules(h, rules)
    answer = h_to_elements(h, polymer)
    return answer




if __name__ == "__main__":
    file = "input_files/problem14.txt"
    polymer, rules_raw = get_data(file)

    choice = input("pick 1 or 2\n")
    if not choice in ("1", "2"):
        raise ValueError("invalid choice")

    if choice == '1':
        answer1 = calc_answer(polymer, rules_raw, 10)
        print(f"the answer to part 1 is {answer1}")
    else:
        answer2 = calc_answer(polymer, rules_raw, 40)
        print(f"the answer to part 2 is {answer2}")
