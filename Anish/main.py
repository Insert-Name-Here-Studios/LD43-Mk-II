from random import randrange



print(
'''
------------------------------------------------------------------------------------------------------------------------
   _____    ___    ___      ____       ___    ___   ___   ___   ___     _____      _____    ____    ___    ___     _____
     |       |      |       |           |      | \   |     | \   |     /     \    /         |        |  \   |        |
     |       |------|       |---        |      |   \ |     |  \  |     |     |   |          |---     |   \  |        |
     |       |      |       |___       _|_    _|_  _\|_   _|_  _\|_    \_____/    \_____    |___    _|_   _\|_       |
------------------------------------------------------------------------------------------------------------------------
''')
Actions =None
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
You are defense laywer who works in a county that just had tax cuts and your salary has been cut.d
You are now in dire need of money to pay your monthy bills and your fairly expensive rent.
You enter your office sighing, dejected
You think that "Maybe it would be better just becoming a prosecutor",
But alas you think to yourself "I spent the better part of a decade working this job because I wanted to protect the weak..."
 ''')


print('''Your newest client knocks on your door, you yell in a drowsy voice your speech slurred "You cann coomee innn,"
The client walks through the door and he says in a low voice "''',Gender_ref,Name,'''Maybe I should come back later when are ready
and then he bursts out laughing.
This is a new for you as most clients are always scared or fearfull, none are carefree and you are slightly confused.
You check the case file and you find that he has been accused of grand theft...''')

print( ''' You think to yourself "Its been a long month maybe iu should refuse this case and go for a easier one"''')
RorD1 = int(input('Choose 1 for rejecting the case Choose 2 for accepting the case,'))
RorD1R = randrange(0,4)
if RorD1 != 1 or RorD1 != 2 or RorD1 != 3:
    RorD1 = RorD1R
if RorD1 == 1:
    print("The man smile and murmurs something and pulls out a knife and slits your throat")
    print('''




    GAME OVER''')
elif RorD1 == 2:
    print('''The man shakes your hand says thank you so much my name is marsello,You ask the man "Whats next any confessions for me,"" and he says no I'm innocent''')
    print('''You tell the man "lets see the evidence against you", you find that there is one peice of evidence against this man
    You find that there is one video of the robbery and the man looks exactly this man and you can just tell it is him.
    ''')
input = int(input('''Press 1 to tell the marsello that you think he is guilty and he should to take a plea bargainself.
Press 2 to tell him that he was safe and you will fight for him:''')

if input == 1:
    print('''Insert ''')
if input == 2:
    print('''Insert ''')
