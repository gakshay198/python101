# Indenting is very important when it comes to functions. VERY...!!!


# This one is like a script with argv.
def print_two(*args):
    arg1, arg2 = args  # unpacking arguments.
    print(f"arg1: {arg1}, arg2: {arg2}")


# *args is pointless. We can do this instead.
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# This function takes one argument only.
def print_one(arg1):
    print(f"arg1: {arg1}")


# This function takes no argument.
def print_none():
    print("I got nothin'.")


# Pass two arguments to print_two()
print_two("Akshay", "Girhepuje")

# Pass two arguments to print_two_again()
print_two_again("Akshay", "Girhepuje")

# Pass one argument only.
print_one("Akshay")

# Pass no argument.
print_none()
