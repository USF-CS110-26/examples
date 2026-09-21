hours = 48
base_pay = 20
if hours > 40:
	print("You worked overtime")
	total = 40 * base_pay + (hours - 40)* 2 * base_pay
else:
	total = hours * base_pay
print(total)
