def product_list(llist):
	total = 1
	for i in range(0, len(llist)):
		total = total * llist[i]
	return total

print(product_list([2, 5, 7, 1]))