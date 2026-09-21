m = input("Enter miles or q to stop: ")
while m != "q":
	km = 1.609 * float(m)
	print(f"In km it is {km}")
	m = input("Enter miles or q to stop: ")
print("Ok, done")

'''
m = " "
while m != "q":
	m = input("Enter miles: ")
	if m != "q":
		km = 1.609 * float(m)
		print(f"In km it is {km}")
print("Ok, done")
'''