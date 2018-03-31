i = 23
j = 12

# Overriding value of x multiple times and giving outputs
x = i + j
print "Addition : 23 + 12 is", x
x = i - j
print "Substraction: 23 - 12 is", x
x = i * j
print "Multiplication : 23 * 12 is", x
x = i / j
y = i % j
print "Division : 23 / 12 is", x, "and remainder : ", y

# To output dividion in floating point
i = 23.0
x = i / 1.36464
print "Division : 23 / 12", x
# round() is used to round the floating number
print "Division : 23 / 12", round(x)
print "Division : 23 / 12 %.0f" % round(x)
