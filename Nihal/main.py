import os
import sys

print(
'''
------------------------------------------------------------------------------------------------------------------------
   _____    ___    ___      ____       ___    ___   ___   ___   ___     _____      _____    ____    ___    ___     _____
     |       |      |       |           |      | \   |     | \   |     /     \    /         |        |  \   |        |
     |       |------|       |---        |      |   \ |     |  \  |     |     |   |          |---     |   \  |        |
     |       |      |       |___       _|_    _|_  _\|_   _|_  _\|_    \_____/    \_____    |___    _|_   _\|_       |
------------------------------------------------------------------------------------------------------------------------
''')
name = str(input('What is your name? '))
name = name.capitalize()
print('\nD A Y   1')
x = input('...')
del x
x = input ('BEEEEP     BEEEEEEP      BEEEEEEP')
del x
print(name + " (thinking): " + "Ugh, the alarm. Time to get up, I guess.")
print('To make a choice, use the number next to the choice.')
done = 0
while not done:
	try:
		c = int(input('1. Get out of bed 2. Stay in bed '))
		done = 1
	except:
		print('Please use the numbers.')
if c == 1:
	x = input('You get up, shower, and otherwise get ready for your day.')
	del x
else:
	x = input('You sleep in, and afterwards hurriedly take a shower and get ready, accidentally hitting your eye with your towel.')
	del x

print("As you get into the car, you remember today is when you get a new client.")
print("Apparently, it's a grand theft case. Your client is accused of stealing several million dollars' worth of jewlery.")
x = input("As you turn into the parking lot, you resolve to do your best to provide adequate counsel and preserve their rights.")
del x
print ("...\n" + name + " (thinking): OK, this isn't gonna work.")
print ("Two weeks ago the prosecution gave you the only evidence they had at that point: a video, taken from security footage.")
print ("In the video, the guy has a mask on so it's kinda hard to tell who it is.")
print("But, the problem is that the man who just walked into your office is very clearly the same person, \nfrom the general build down to the slight limp in his right leg.")
x = input("Now, when someone is guilty, they USUALLY tell their lawyers so.")
del x
x = input ("But this guy... heh... this guy was different.")
del x
print('He marched into your office with that little limp of his, sat down like he owned the place, and proceeded to \nrant about how he was innocent and that the jury, prosecution, judge, everyone from the county sheriff \nto the attourney general was an idiot for allowing an innocent man to face criminal charges.')
print("... Unfortunately for you, you're legally required to help him how you can.")
input("Good luck.")
