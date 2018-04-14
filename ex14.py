from sys import argv

script, uname, lname = argv
prompt = '>>>'

print(f"Hi {uname} {lname}, I'm the {script} script.")
print("I would like to ask you few questions.")
print(f"Do you like me {uname} {lname}?")
likes = input(prompt)

print(f"Where do you live {uname}??")
live = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""So you said {likes} about liking me.
You live in {live}. I know where that is.
And you have a {computer} computer. Cool...""")
