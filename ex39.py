states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'SAN Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities.
print('-' * 10)
print("NY state has:", cities['NY'])
print("OR state has:", cities['OR'])

# Printing states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# printing cities by using states dictionary
print('-' * 10)
print("Michigan has:", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

# printing all items from states dict.
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbriviated as {abbrev}")


# printing all items from cities dict
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# printing both dictionaries
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated as {abbrev}")
    print(f"and has city {cities[abbrev]}")

# safely get abbreviation of state that might not be there in dictionary
print('-' * 10)
state = states.get('Texas')

if not state:
    print("Sorry, No Texas.")

# get city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
