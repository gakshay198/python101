# Study drill ex33.py

numbers = []  # declare list

x = int(input("Add increment"))  # Take increament from user
i, n = 0, 6


def add_item(i, increament):  # function to add items to list
    while i < n:
        numbers.append(i)  # append item to list
        print(numbers[:])  # print list
        i += increament  # increment item value


add_item(i, x)  # call function

print("the numbers list is")

# Print list
for num in numbers:
    print(num)

# another way to print list
print(numbers[:])
