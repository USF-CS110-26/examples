llist = ["cat", "dog", "cat", "fox", "cat", "fox"]
d = {}
for word in llist:
	if d.get(word) == None:
		d[word] = 1
	else:
		d[word] = d[word] + 1
print(d)
