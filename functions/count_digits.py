#Write a program that computes the number of digits in the #string
s = "cat2dog57"
count = 0
for letter in s:
	if letter.isdigit():
		count = count + 1
print(count)