with open("numbers.txt") as file:
    for line in file:
        line = line.strip()
        row = line.split(" ")
        print(row)