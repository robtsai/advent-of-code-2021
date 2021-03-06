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



def count_known_numbers(data):
    known = 0
    for _, result in data:
        for num in result:
            if len(num) in unique_digits.keys():
                known += 1
    return known



if __name__ == "__main__":
   
    file = "input_files/problem8.txt"
    data = get_data(file)
    known = count_known_numbers(data)
    print(f"answer to part 1 is {known}")
   