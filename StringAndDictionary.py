# single and double quotation permitted for String in python
x = 'Pluto is a planet'
y = "Pluto is a planet"
print(x == y)

print("Pluto's a planet!")
print('My dog is named "Pluto"')

# single quotation inside single quotation in python using back slash
print('Pluto\'s a planet!')

# String is similar to list of character, the mjor difference is string is immutable
# string upper case
claim = "Pluto is a planet!"

print(claim.upper())
print(claim.lower())

# first index of subString
print(claim.index("is"))

#starts with substring
print(claim.startswith('Pluto'))

# ends with substring
print(claim.endswith('planet!'))

# split string in small substrings at given character,if nothing is mention splits at space and return list
print(claim.split())
print(claim.split('a'))

# join
print(' '.join(['a','b','c']))
print('+'.join(claim.split()))

# concat
print(claim + 'something')

# dictionary
numbers = {'one': 1, 'two': 2, 'three': 3}
print(numbers)

print(numbers['one'])

numbers['four'] = 4

print(numbers)

numbers['four'] = 5

print(numbers)

# creating dict from list
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_planetInitials = {planet:planet[0] for planet in planets}
print(planet_to_planetInitials)

#check key is in the dict
print('Venus' in planet_to_planetInitials)

# interate over keys
for key in planet_to_planetInitials:
	print(key)

#another syntax
for key in planet_to_planetInitials.keys():
	print(key)

#iterate over values
for value in planet_to_planetInitials.values():
	print(value)

# iterate over keys and values at the same time of dict
for key,value in planet_to_planetInitials.items():
	print(key,value)
