from sys import argv
from os.path import exists  # to impirt exists()

script, file1, file2 = argv  # Unpacking the passed argumnts.

print(f"Copying from file {file1} to {file2}.")

# You always need varibale to open a file. eg. 'inline' in the line below.
infile = open(file1)  # Create a varibale and open file with it.

# Call read() on the variable to read the file opened with it.
indata = infile.read()


# Count length of file in bytes using len()
# Have to pass variable with which file is read to len().
print(f"The input file is {len(indata)} bytes long.")

# Check if file exists or not. Not mandatory
print(f"Does the output file exists?? {exists(file2)}")

print("Hit Enter to continue.")

outfile = open(file2, 'w')  # Open file with read permissions.

outfile.write(indata)  # Write to the file.

# Always close the files.
infile.close()
outfile.close()

# Opening the files again to print their content.
f1 = open(file1)
f2 = open(file2)

print("\nThis is source file:")
print(f1.read())

print("This is destination file.")
print(f2.read())
