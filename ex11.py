# end=' ' tells	print to not end the line with a newline character
# if end=' ' is not used then control will go to newline and user input will
# be taken on newline.
print("How old are you?", end=' ')
age = input()

# Prints the text in "" and also takes input.

height = input("How tall are you?")


#  Input is taken on next newline.
print("How much do you weigh?")

weight = int(input())  # Take integer as an input

print(f"So, you're {age} years old, {height} tall and {weight} heavy.")
