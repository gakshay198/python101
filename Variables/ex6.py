x = "There are %d type of people" % 10
binary = "Binary"
dont = "don't"
# Print strings
# multiple variables are called using () and single are direvtly called
y = "Those who know %s and those who %s" % (binary, dont)
print x
print y

# %r prints the string using repr() that is using quotes.
# We use %r for debugging, since it displays the "raw" data of the variable
# but we use %s and others for displaying to users .

print "I said: %r" % x
print "I also said: '% s'  " % y
# assigns boolean vallue.First letter is capital. i.e. True OR False
hilarious = False
jokeevaluation = "Isn't that joke so funny ?! %r"

print jokeevaluation % hilarious

w = "This is left side of... "
e = "a string with right side"

print w + e
