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
print('D A Y   1')
x = input('...')
del x
x = input ('BEEEEP     BEEEEEEP      BEEEEEEP')
del x
print("''Ugh, the alarm. Time to get up, I guess.''")
print('To make a choice, use the number next to the choice.')
done = 0
while not done:
	try:
		c = int(input('1. Get out of bed 2. Stay in bed'))
		done = 1
	except:
		print('Please use the numbers.')
