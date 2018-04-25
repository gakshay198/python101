from sys import argv

script, input_file = argv  # Unpacking argv


def print_all(f):
    print(f.read())  # Read entire file and print it.


def rewind(f):
    f.seek(0)  # Reset the file counter to beginning of file.


def print_a_line(line_count, f):
    print(f"current_line is : {current_line}")
    # Print one line at a time. And set the read head after next \n.
    print(line_count, f.readline())


# Open the file and asign it to current_file
current_file = open(input_file)

print("Let's print the whole file first:")
print_all(current_file)


print("Let's rewind now.")
rewind(current_file)

print("Let's print some lines now...")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
