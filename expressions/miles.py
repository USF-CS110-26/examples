miles = float(input("How many miles did you run? ")) # if they used int, give a warning, but no deduction
hours = float(input("How long did it take? ")) # if they used int, give a warning, but no deduction

average_speed = miles / hours
average_speed_km = miles * 1.6 / hours
print(average_speed)
print(average_speed_km)

'''
How many miles did you run? 5
How long did it take? 1.2
Your average speed in miles per hour is 4.166666666666667
Your average speed in km per hour is 6.666666666666667
'''