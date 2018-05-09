# Creating list
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This for loop goes through a list.
for number in the_count:
    print(f"This is count : {number}")  # printing list

# same as above
for fruit in fruits:
    print(f"The fruit is : {fruit}")  # printing list

# similar as the both given above
for i in change:
    print(f"I got {i}")  # printing list

# Creating an empty list
elements = []

# Adding items to the list
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

# Adding more items to existing list
for i in range(0, 4):
    elements.append(i)

for i in elements:
    print(f"element was : {i}")  # printing list.


# Trying new operations on lists from python documentation

print(fruits[0])  # Prints first item
print(fruits[-1])  # Print last item
print(fruits[-3:])  # print last 3 items as list. It's called slicing.
# We can print entire list by slicing. i.e without passing number and only by :
print(fruits[:])

# List concatenation

fruits = fruits + ['banana', 'mango', 'strawberry']
print(fruits[:])

# changing existing item by index
fruits[0] = 'coconut'
print(fruits[:])

# append can take operations also
fruits.append('apple' * 2)
print(fruits[:])


# altering list by slices i.e by using :

fruits[1:4] = ['ORANGES', 'PEARS', 'APRICOTS']  # changing items 1, 2, and 3
print(fruits[:])

fruits[1:4] = []  # removing item 1, 2, and 3
print(fruits[:])

# counting elements in list
x = 0
for i in fruits:
    x += 1
print("There are", x, 'items in the list.')

# another and better and easy way
print(f"There are {len(fruits)} items in the list.")

# Creating nested lists

nest_list = [fruits, the_count]
print(nest_list[0])  # Print first list
print(nest_list[-1])  # print last list
print(nest_list[1][3])  # 2nd list, 4th item
print(nest_list[:])  # print entire nested list
