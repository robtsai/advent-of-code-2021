from collections import Counter
import copy


def get_school(file):
    with open(file, "r") as f:
        fish_raw = f.readline().split(",")
        fish = [int(x) for x in fish_raw]
        return fish


def transition(fish):
    if fish == 0:
        return 6
    else:
        return fish - 1


def process_line(school):
    # zerofish will spawn new fish
    numzeroes = sum([1 for fish in school if fish == 0])
    for i, fish in enumerate(school):
        school[i] = transition(fish)
    school.extend([8] * numzeroes)
    return school


def fish_after_days(days, school):
    for day in range(1, days + 1):
        school = process_line(school)
    return len(school)


# part 2
# represent fish as array
# 0 1 2 3 4 5 6 7 8
#


def get_school_arr(file):
    with open(file, "r") as f:
        fish_raw = f.readline().split(",")
        fish = [int(x) for x in fish_raw]
        fish_count = Counter(fish)
        arr = [0 for _ in range(9)]
        for k, v in fish_count.items():
            arr[k] = v
        return arr


def transition_arr(school_arr):
    newarr = [0 for _ in range(len(school_arr))]
    # this is tricky as if you assign newarr[6] in the zero iteration, it will
    # get overwritten by assignment with the day 7 fishes turn to 7-1
    for i, val in enumerate(school_arr):
        if i == 0:
            newarr[8] = val
        else:
            newarr[i - 1] = val
    # we also need to add to newarr[6] with the respawned fish (which are newarr[8])
    newarr[6] += newarr[8]
    return newarr


def fish_after_days_part2(days, school_arr):
    newarr = school_arr[:]
    for day in range(1, days + 1):
        newarr = transition_arr(newarr)
    print(newarr)
    return sum(newarr)


if __name__ == "__main__":
    file = "input_files/problem6.txt"

    school = get_school(file)

    choice = input("choose part 1 or 2\n")
    if not choice in ("1", "2"):
        raise ValueError("pick 1 or 2")

    if choice == "1":
        numdays = 80
        print(
            f"part 1: there are {fish_after_days(numdays, school)} fish after {numdays} days"
        )

    else:
        numdays = 256
        school_arr = get_school_arr(file)
        answer = fish_after_days_part2(numdays, school_arr)
        print(f"part 2: there are {answer} fish after {numdays} days")
