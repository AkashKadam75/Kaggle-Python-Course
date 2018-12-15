
primes = [2, 3, 5, 7]
print(primes)
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]
print(hands[0][-3])
print(hands[0:3])
print(hands[2][0:2])
print(hands[2][:2])
print(hands[2][1:])
print(hands[2][0:-1])
print(hands[2][-3:])

#list are mutable
hands[2][0] = 'V'
print(hands[2][0:2])

planets[:3] = ['Mur', 'Vee', 'Ur']

print(planets)
#length
print(len(planets))
# sorted version
print(sorted(planets))

# sum of list values
print(sum(primes))

# imaginary part img function
number = 1256
imaginary_number = 12 + 5j
print(number.imag)
print(imaginary_number.imag)

print(number.bit_length())

help(number.bit_length)

print(primes.append(23))
print(primes)

print(primes.pop())

print(primes.index(5))
print(5 in primes)

# Tuples are same as list with () brackets and can not modified immutable
tuplelist = (2,4,6)
print(tuplelist)
print(tuplelist.index(6))
# integer ratio
x = 1.25
print(x.as_integer_ratio())
#result (5,4)
#swap in python
a = 4
b = 5
a,b = b,a
print(a,b)

# name of captain of the worst team
def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[len(teams) - 1][1]

 # swap of first and last racer
 def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    racers[0],racers[-1] = racers[-1],racers[0]

 def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    if (arrivals.index(name) != len(arrivals) - 1) and (arrivals.index(name) >= (len(arrivals) / 2)):
        return True
    else:
        return False;

# number of negative numbers
 def count_negatives(nums):
    """Return the number of negative numbers in the given list.
    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    nums.append(0)
    var = sorted(nums)
    index = var.index(0)
    return index
