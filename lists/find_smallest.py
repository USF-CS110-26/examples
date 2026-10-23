def find_smallest(numbers):
	smallest = numbers[0]
	for i in range(1, len(numbers)):
		if numbers[i] < smallest:
			smallest = numbers[i]
	return smallest

l = [1, 6, 5, 8, 2, 9]
res = find_smallest(l)
print(res)