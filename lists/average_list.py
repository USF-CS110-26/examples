def average_list(numbers):
	
	total = 0
	for i in range(0, len(numbers)):
		total = total + numbers[i]

	return total / len(numbers)

print(average_list([2, 5, 7, 1]))