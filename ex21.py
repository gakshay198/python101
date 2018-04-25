def add(a, b):  # function to add two numbers.
    print(f"Adding {a} + {b}")
    return a + b  # Return addition


def sub(a, b):  # substract two numbers.
    print(f"Substracting {a} - {b}")
    return a - b  # Return substraction


def mult(a, b):  # multiply two numbers.
    print(f"Multiplying {a} * {b}")
    return a * b  # Return multiplication


def divide(a, b):  # Divide two numbers.
    print(f"Dividing {a} / {b}")
    return a / b  # return division


print("Let's do some math with just functions")

# Take two float numbers from user.
first = float(input("Enter first number "))
second = float(input("Enter second number "))

age = add(first, second)  # Pass two variables as arguments

# Pass two numbers to functions
height = sub(78, 4)
weight = mult(90, 2)
iq = divide(100, 2)

# Print returned values.
print(f"Age : {age}, Height : {height}, Weight : {weight}, IQ : {iq}")

print("Here is a puzzle")
# Functions can also be passed as arguments.
# It works "inside out"
what = add(age, sub(height, mult(weight, mult(iq, 2))))


print("That becomes:", what, "Can you do it by hand??")
