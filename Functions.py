print("The print function takes an input and prints it to the screen.")
print("Each call to print starts on a new line.")
print("You'll often call print with strings, but you can pass any kind of value. For example, a number:")
print(2 + 2)
print("If print is called with multiple arguments...", "it joins them",
      "(with spaces in between)", "before printing.")
print('But', 'this', 'is', 'configurable', sep='&&')
print(2,4,5,6,sep='+')
print("^^^ print can also be called with no arguments to print a blank line.")
print()

# to know about any in build function of python use help
# only pass function name
help(hash)

help(print)

def least_diff(a,b,c):
	# for help method
	""" Return smallest value """
	diff1 = abs(a - b)
	diff2 = abs(b - c)
	diff3 = abs(c - a)
	return min(diff1,diff2,diff3)

print(least_diff(10,4,6), least_diff(12,5,7), sep="**")
# called method needs to define first

help(least_diff)

# when there is no value python refer is as None instead of null as in Java

mystery = print()
print(mystery)

# default value of sep in print is a single space

def greet(who="Akash"):
	print("Hello",who)

greet()
greet(who="Ketan")
greet("Sanket")

variable = greet()
print(type(greet),type(variable))

# class of None is NoneType

# lambda function in python

mod_5 = lambda x : x % 5
print(mod_5(1))

help(max)

# key of max
print(max(100,24,13, key = mod_5))

names = ['jacques', 'Ty', 'Mia', 'pui-wa']
print("Longest name is:", max(names, key=lambda name: len(name)))

# round 
print(round(344.556,2))
print(round(344.55,-2))

# time 
from time import *
t = time()
print(t, "seconds since the Epoch")


#sleep

duration = 5
print("Getting sleepy. See you in", duration, "seconds")
sleep(duration)
print("I'm back. What did I miss?")





