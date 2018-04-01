tab = "\tI'm a tabbed cat"
persian = "I'm split\non a line"
backslach = "I'm \\ a \\ cat"

fat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass"""
print tab
print persian
print backslach
print fat

# Multiple ways to print string are below

print "%r" % fat
print "%s" % fat
print "Will print at the end of this :", fat
