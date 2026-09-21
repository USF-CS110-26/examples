attempts = 0
while attempts < 3:
    password = input("Enter password: ")
    if password == "python":
        print("Correct!")
        break
    attempts = attempts + 1
else:
    print("Too many incorrect attempts")
