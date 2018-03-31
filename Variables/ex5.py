# Working with Variables and String
import datetime
name = 'akshay'
age = 212314
height = 64  # inches
weight = 52  # kilos
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print "let's talk about %s." % name
print "he is %d years old." % age
print "He weighs %d." % weight

print "If I add %d , %d, and %d I get %d." % (age, height, weight, age + height + weight)

# To print hexadecimal value of a number
print "age is hex : %X" % age

# Difference between %r and %s format specifier.
x = datetime.date.today()
print "%r" % x    # uses repr() to print output
print "%s" % x    # uses str()
