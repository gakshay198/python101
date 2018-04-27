print("Let's practice everything.")
print("You\'d need to know \'bout escapes with \\ that do:")
print('\n newlines  and \t tabs')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the need of love
nor comprehenf passion from intuition
and requires an explanation
\n \twhere there is none.
"""

print("-----------------")

# The \n \t in """ """ will not be printed directlly but interpreted
print(poem)
print("-----------------")

five = 10 - 2 + 3 - 6
print(f"This should be five : {five} ")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# Two ways to format strings.
# first
print("With a starting point of : {}" .format(start_point))

# second
print(f"we'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way.")
formula = secret_formula(start_point)

# Easy way to apply list to format strings.
print("We'd have {} beans, {} jars, and {} crates" .format(*formula))
