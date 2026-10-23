 # Does the list contain a negative number?
 # Return True or False
def contains_negative(numbers):
	found = False
	for i in range(len(numbers)):
		if numbers[i] < 0:
			found = True
	return found


numbers = [6, 0, 8, 2, 4]
print(contains_negative(numbers))