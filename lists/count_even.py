def count_even(numbers):
	# count how many even elements are in the list
	counter = 0
	for i in range(len(numbers)):
		if numbers[i] % 2  == 0:
			counter  = counter + 1

	return counter	

