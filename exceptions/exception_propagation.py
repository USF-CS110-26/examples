def	func(): 
	x =	1 / 0

try:
	func()
except	ZeroDivisionError as err: 
	print("Error: ", err)
