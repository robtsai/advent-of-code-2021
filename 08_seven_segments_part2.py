def get_data(file):
    output = []
    with open(file, "r") as f:
        for line in f:
            signal, result = line.replace("\n", "").split("|")
            signal = signal.strip().split(" ")
            result = result.strip().split(" ")
            output.append((signal, result))
    return output




if __name__ == "__main__":
    file = "input_files/problem8.txt"
    data = get_data(file)
    print(data)
