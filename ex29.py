dogs = 15
cats = 30
# Taking user input.
people = int(input("How many people are there? "))

# Indenting is must while creating block of code in python,

if (people < cats) and (people < dogs):  # True and False = False
    print("Too many cats. The world is doomed..!!")

if people > cats:
    if people > dogs:
        print("Not many cats and dogs. The worls is saved.")

if people < dogs:
    print("The world is drooled on..")

if people > dogs:
    print("The world is dry.")

# dogs = dogs + 5
dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")
