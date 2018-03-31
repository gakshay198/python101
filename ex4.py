# Declare variables and asign values to them
cars = 100
# float can also be asigned as a value
space = 4
# 30 drivers available today.
drivers = 30
# There are 90 passengers.
passengers = 90
# Available cars minus drivers will give the cars not driven.
not_driven_cars = cars - drivers
# Numbers of driven cars is same as number of drivers.
drivencars = drivers
# The below line will give float output since one of the operand is float.
carpool_capacity = drivencars * space
# Total passengers divided by driven cars is average passengers per car.
average_passangers = passengers / drivencars

print "There are", cars, "available"
print "But there are only", drivers, "availble"
print "There willl be", not_driven_cars, "empty cars today"
print "we can transport", carpool_capacity, "people"
print "we have", passengers, "passengers to carpoool today"
print "we need to put about", average_passangers, "in each car today"
