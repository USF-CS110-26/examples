total = 0
with open("numbers.txt") as file:
    for line in file:
        number = int(line.strip())
        total += number
print("Sum:", total)
