def cheese_and_crackers(cheese_count, box_of_crackers):
    print (f"You have {cheese_count} chesses")
    print (f"You have {box_of_crackers} boxes of crackers.")
    print ("Man that's enough for a party!!")
    print ("let's get a blanket. \n")


# type 1 - passing numbers as arguments to the function
print ("We can just give the function numbers directly")
cheese_and_crackers(20, 30)  # Calling the function


# type 2 - passing variables as arguments to the function
print("Or we can use varibles instead")

# declaring varibles
amount_of_cheese = 20
amount_of_crackers = 30

# Calling function
cheese_and_crackers(20, 30)

# type 3 - math as an arguments
print("We can even do math inside too :")
cheese_and_crackers(10 + 20, 6 + 7)  # Calling function

# type 3 - variables and math as arguments
print ("And we can combine both varibles and math too")
# Calling function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# type 4 - Taking input from the user
cheese = input(" How much cheese do you have?")
cheese = int(cheese)  # Converting user input into integer

# another way to convert user input to float
crackers = int(input("How many boxes of crackers do you have?"))

cheese_and_crackers(cheese, crackers)
