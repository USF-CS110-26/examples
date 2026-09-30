def	f1(x): 
	return	x-1

def	f2(y):
	return	y+3

def f3(z):
	res1 = f1(z)
	res2 = f2(z)
	return res1 + res2

print(f3(2))