# sys is Package.
# argv is a module.

from sys import argv

script, first, second, third, fourth = argv
# command line argumnts are taken as strings

print("The script is called :", script)
print("The first variable is called:", first)
print("The second variable is called :", second)
print("The third variable is called : ", third)

print("The fourth variable passed is :", fourth)

number = int(input("Enter an integer"))  # Getting integer input

fourth = int(fourth)  # Converting passed argument from str to int.


# Adding one argument passed and an input taken from user.
addition = number + fourth

print(addition)


"""
Difference between argv and input() -
1. argv - input is given in command line.
is where the user gives input to the script.
2. input() - input is given when script is runnning.
"""
