print("""You enter a dark room with two doors.
Do you go though door #1 or door #2??""")

door = input(">>>")

if door == "1":
    print("There is a giant bear eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    bear = input(">>>")
    if bear == "1":
        print("The bear eats your face off.\nGood Job..!!")
    elif bear == "2":
        print("The bear eats your legs off.\nGood Job..!!")
    else:
        print("You don't have that choice..!!")
elif door == "2":
    print("You stare into endless abyss of Cthulu's retina.")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    insanity = input(">>>")
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by mind of jello.")
        print("Good Job..!!")
    else:
        print("The instanity rots your eyes into a pool of muck.\nGood Job.!!")
elif door == "":
    print("Don't you just hit enter...!!! Choose 1 or 2..!!")
else:
    print("Wrong Choice.. No such door.. Sorry..\nGAME OVER...")
