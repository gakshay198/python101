people = 10  # Asign Value
x = f"There are {people} types of people" # Create a formatted string

binary = "Binary"
dont = "Don't"

y = f"Those who understand {binary} and those who {dont}"

# Print strings using variables
print(x)
print(y)

# Print strings within strings
print(f"I said : {x}")
print(f"I also said : {y}")

# Printing multiple strings in single print()

print(f"I also said : {y}",f"use {x}", "Using multiple strings")


hilarious = False  # Boolean value
joke = "Isn't that joke so funny ? {}" # Create a string format

# Use format() to print pre-formatted string with other variable.
print(joke.format(hilarious))

# string concatenation
w = "This is the left side of...."
e = "I string with right side"

print (w + e)
