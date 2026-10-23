def sum_list(llist):
	total = 0
	for i in range(0, len(llist)):
		total = total + llist[i]
	return total

print(sum_list([2, 5, 7, 1]))