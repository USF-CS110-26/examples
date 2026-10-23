def print_pairs(numbers, target):
	for i in range(len(numbers)):
		for j in range(i + 1, len(numbers)):
			if numbers[i] + numbers[j] == target:
				print(numbers[i], numbers[j])


				
print_pairs([2, 5, 3, 7, 4, 1], 8)
