homes	=	{
 "12 Maple St" : (450000, 2, 2),	
 "45 Clement St":(630500, 3, 2),	
 "123 Fulton" :(700500,	2, 1)}

# Print information about homes that cost	< 500K
# Iterating over homes
# For each address, access the value
# Access the price of the home
# Compare the price with 500000 and print
for address in homes.keys():
	val = homes[address]
	price = val[0]
	if price < 500000:
		print(address, price)

