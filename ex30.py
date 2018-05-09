people = 30
cars = 40
trucks = 15

""" In if-else only one condition is checked. As soon as first condtion is
found true, control goes out of loop once it is executed """

# block 1
if cars > people:
    print("We should take the cars.")  # if cars > people = True
elif cars < people:
    print("We shouldn't take the cars.")  # if cars < people = True
else:
    print("We can't decide.")  # if both if and elif are not true.

# block 2
if trucks > cars:
    print("That's too many trucks.")  # id trucks > cars = true
elif trucks < cars:
    print("Maybe we could take the trucks.")  # if trucks < cars = true
else:
    print("We still can't decide,")  # if both if and elif are not true then.

# block 3
if people > trucks and cars < trucks:
    # both conditions need to be true since 'and' is used
    print("Alright, let's just take the trucks then.")
else:
    # if one of the condtion is false then.
    print("Fine, let's just stay home then.")
