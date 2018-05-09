ten_things = "Apple Oranges Crows Telephone Light Sugar"

print(f"There are 10 things in this list:\n{ten_things}")
print("\nWait... There are not 10 things in that list. Let's fix that.\n")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding", next_one)
    stuff.append(next_one)  # append item
    print(f"There are {len(stuff)} items now.\n")

print("There we go :\n", stuff, "\n")

print("Let's do some things with stuff...")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())  # pop last item
# Join elements by ' '
print(' '.join(stuff))  # See output of the script
# join elements by #
print('#'.join(stuff[3:6]))
