from sys import argv

script, file = argv  # Taking filename from command line.

# Opening a file.
txt = open(file)

print(f"Here's your file {file}")

# read() is used to read the opened file.
# So we call read() function on txt to read the file.
print(txt.read())  # Reading the file and printing it.
txt.close()  # Closing the file.

print("Type the filename again")
file1 = input(">")  # Taking filename from user

txt1 = open(file1)  # Opening the file

print(txt1.read())  # Reading the file and printing it.


txt1.close()
