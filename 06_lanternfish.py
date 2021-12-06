file = "input_files/problem6.txt"


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
    for day in range(1, days+1):
        school = process_line(school)
    return len(school)



if __name__ == "__main__":
    school = get_school(file)

    choice = input("choose part 1 or 2\n")
    if not choice in ('1', '2'):
        raise ValueError("pick 1 or 2")

    if choice == "1":
        numdays = 80
        print(f"part 1: there are {fish_after_days(numdays, school)} fish after {numdays} days")
  
