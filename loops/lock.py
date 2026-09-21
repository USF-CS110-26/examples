import random
digit1 = random.randint(0, 9)
digit2 = random.randint(0, 9)
digit3 = random.randint(0, 9)
print(digit1, digit2, digit3)

x = -1
y = -1
z = -1
print("Guess the code")
while x != digit1 or y != digit2 or z != digit3:
	x = int(input("Enter a digit from 0 to 9: "))
	y = int(input("Enter a digit from 0 to 9: "))
	z = int(input("Enter a digit from 0 to 9: "))
	print("-----------")
print("You guessed correctly!")