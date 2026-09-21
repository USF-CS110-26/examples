movie_name = "The Odyssey"
ticket_price = 17.50
snack_price = 6.75
name = input("Enter your name: ")
num_tickets = int(input("Enter how many movie tickets you want to buy: "))
print("Movie name: ", movie_name)
print("User name: ", name)
print(num_tickets)
print(ticket_price)
print(snack_price)
print(type(movie_name))
print(type(name))
print(type(num_tickets))
print(type(ticket_price))
print(type(snack_price))
total_ticket_cost = num_tickets * ticket_price
total = total_ticket_cost + num_tickets * snack_price
print(total)
