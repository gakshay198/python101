cars = 100
space = 4.0
drivers = 30
passengers = 90
not_driven_cars = cars - drivers
drivencars = drivers
carpool_capacity = cars * space
average_passangers = passengers / drivencars

print "There are", cars, "available"
print "But there are only", drivers, "availble"
print "There willl be", not_driven_cars, "empty cars today"
print "we can transport", carpool_capacity, "people today"
print "we have", passengers, "passengers to carpoool today"
print "we need to put about", average_passangers, "in each car today"
