l = ["cat", "dog", "pets", "a", "animal"]
d = {}
for word in l:
	d[word] = len(word)
print(d)

for key in d.keys():
	print(key, "->", d.get(key))
