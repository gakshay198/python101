cars = 100
space = 4.0
drivers = 30
passengers = 90
notdriven = cars - drivers
driven = drivers
carpool = driven * space
average = passengers / driven

print("There are", cars, "cars available.")
print("But there are only", drivers, "drivers.")
print("So cars not driven =", driven, "Cars not driven =", notdriven)
print("There are", passengers, "passengers.")
print("carpool is =", carpool)
print("There should be about", average, "in each car")
