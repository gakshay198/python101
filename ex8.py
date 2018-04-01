# Define a format for string.
formatter = "{} {} {} {} " # 4 arguments

a = "three" # asign string three to variable a.

# Print Various strings using the pre defined variable formatter
# .format() is function.
# Passing 4 argumengts to formatter using .format() function
print (formatter.format(1, 2, 3, "Akshay")) # Can pass nnumbers and strings together

print (formatter.format("one", "two", a , "four"))

# No double quotes needed to format boolean values.
# They are treated as keywords if we put "" then they are treated as strings
print (formatter.format(True, False, False, True))

# Passing the variable to itself as an argument.
print (formatter.format(formatter, formatter, formatter, formatter))

print (formatter.format(
"Akshay\n",  # Using \n for new line.
'G', # Can use single quotes along with double quotes in this.
"N",
"."))

# Use """ for multiline commentsself. eg. See below.

"""
If we had used only 3 {} in formatter variable and passed 4 arguments then
only first 3 arguments would have been printed.
But if we pass less argument than defined numbers thenm it gives
"tuple index out of range" error."""
