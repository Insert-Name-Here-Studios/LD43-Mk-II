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

Gender = None
Gender_ref = None
Name = None
Gender = int(input('''
 What is your Gender press 1 for male 2 for female:
'''
  ))

Name = input('''
What is your name:

'''
)

Name = Name.capitalize()


if Gender == 1:
  Gender_ref = 'Mr.'

if Gender == 2:
  Gender_ref = 'Ms.'

print(Name)



print('''
You are defense laywer who works in a county that just had tax cuts and your salary has been cut.
You are now in dire need of money to pay your monthy bills and your fairly expensive rent.
You enter your office sighing, dejected
You think that "Maybe it would be better just becoming a prosecutor",
But alas you think to yourself "I spent the better part of a decade working this job because I wanted to protect the weak..."
 ''')


print('''Your newest client knocks on your door, you yell in a drowsy voice your speech slurred "You cann coomee innn,"
The client walks through the door and he says in a low voice "''',Gender_ref,Name,'''maybe I should come back later when are ready
You look and see one of the shortest adults you have ver laid your eyes on''')
