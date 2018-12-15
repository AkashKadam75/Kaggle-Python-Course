planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
	print(planet,end ='\n')

multiplicands = (2, 2, 2, 3, 3, 5)
for multiplicand in multiplicands:
	print(multiplicand,end="\n")

# iteration over string
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')
# range in for loop
print()
for i in range(5):
	print(i,end=" ")
print()

# list of range
print(list(range(5)))

# iteration over length of list
nums = [1, 2, 4, 8, 16]
for i in range(len(nums)):
    nums[i] = nums[i] * 2

print(nums)

# enumarate in python
def double_odds(nums):
    for i, num in enumerate(nums):
        if num % 2 == 1:
            nums[i] = num * 2

# interation over three different type of value in tuples
nums = [
    ('one', 1, 'I'),
    ('two', 2, 'II'),
    ('three', 3, 'III'),
    ('four', 4, 'IV'),
]

for word, integer, roman_numeral in nums:
    print(integer, word, roman_numeral, sep=' = ', end='; ')

 # while loop in python
print()
i = 0
while i < 10:
	print(i,end=" ")
	i += 1
# list comprehension
print()
squares = [n**2 for n in range(10)]

print(squares)
# list comprehension with if condition
print()
short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)

