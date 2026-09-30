def	compute_interest(d,	rate = 0.02): 
	for	years in range(1, 11):
		a =	d * (1 + rate) ** years 
		print(a)

compute_interest(1000)	#	default	rate 
compute_interest(1000,	0.01)	#	rate = 0.01
