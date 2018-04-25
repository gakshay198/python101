from sys import argv

script, file = argv  # Unpacking arguments passed through command line.

print(f"We are going to erase {file}")
print("If you don't want that then hit Ctrl-C.")
print("If you want that then hit Enter.")

input('?')  # Take user input.

print("Opening the file...")
# Open file to write it.
# Always asign it to a variable whenever opening a file.
target = open(file, 'w')

print("Truncating the file.. Goodbye!!")
# Deleting contents of the file.
target.truncate()

# Take 3 Line input
print("Now I'm going to ask you for 3 lines...")

line1 = input('Line 1:')
line2 = input('Line 2:')
line3 = input('Line 3:')

# multiple lines using multiple write()
print("I'm goint to write these lines to the files...")
target.write(line1)  # Write first line.
target.write('\n')  # newline character
target.write(line2)  # Write second line.
target.write("\n")  # newline character.
target.write(line3)  # Write third line.
target.write('\n')  # newline character

# Single write() to write multiple lines at once.
target.write(" %s \n %s \n %s \n" % (line1, line2, line3))


print("And now we close the file")
target.close()  # Closing the file.

target = open(file)
print("Let's read the file now")
print(target.read())
