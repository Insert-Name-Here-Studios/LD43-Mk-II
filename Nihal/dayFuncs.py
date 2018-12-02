def day1(corr, name, path):
	input("The prosecution sent you some new evidence they found.")
	print("It's a gun, the same gun that was used in the video to threaten people.")
	print("They also found some witnesses, whose testimony will be said in court tomorrow.")
	print("Given the evidence, prosecution extended a plea bargain: plead guilty, \nand he'll recieve 30 years in prison rather than a life sentence.")
	print("Paris: What should I do?")
	c = input("1. Tell him to accept the plea bargain  2. Tell him to testify in court if he has an alibi  3. Tell him you'll... " + '"take care of it."')
	if '1' in c:
		print("Paris: I guess you're right. I don't have the resources to really pursue this. Please negotiate the plea bargain.")
		print("You managed to get the plea bargain down to 20 years, Paris plead guilty on day 1 in court, and was carted off to prison.")
		print("15 years later, you see Paris once again. He's dressed nicely and eating at a Michelin Star restaurant with a Lamborghini parked in front.")
		print("It was as you thought. He really was guilty, but there's nothing you can do about it now. It appears he got off early for good behavior. Good for him, you think")
		input("\n \n \nT H E   E N D")
		return True
	elif '2' in c:
		print("Paris: I'm innocent. I really am. I'll testify, and rightly so, that I was sitting at home, watching TV at the time the robbery occurred.")
		input(name + ": I believe you. (You don't.) Do you have anybody to support your alibi?")
		print("Paris: No. I live alone and have no other family.")
		input(name + ": Ok. And what was your last name again?")
		print("Paris: Arionas.")
		input(name + ": Ok. I'll talk with you tomorrow. It's getting late.")
		print("Paris: Alright.")
		input("After Paris leaves, you request and look through old marriage records. Just in case. \n" + name + ': That lying little... ' + "He's married! And has been for the past 15 years!")
		print("You glance at your watch. 10:30 PM. You really should be getting home.")
		path += 'M'
		return False
	elif '3' in c:
		print("Paris: Ah. Well, uh, I should get going, so I can claim I didn't know about this. Bye.")
		nc = input("1. Bribe the witnesses.  2. Bribe the prosecution  3. Bribe the jury  4. Don't do anything. ")
		if '1' in nc:
			corr += 25
			print("You've payed off the witnesses. Now they'll, let's say, " + '"forget"' + " certain... unhelpful details.")
			path += 'Wb'
			return False
		elif '2' in nc:
			corr += 20
			print("You've payed off the prosecution. Now they'll, let's say, " + '"lose"' + " certain pieces of evidence.")
			path += 'Pb'
			return False
		elif '3' in nc:
			corr += 45
			print("You've payed off the entire jury. Now they'll, let's say, " + '"change their minds"' + " about the guilt of a certain someone.")
			path += 'Jb'
			return False
		else:
			print("You decide to retain your morals as you decide not to do anything illegal.")
			return False
	else:
		print("Paris: Your silence shows that you don't know what to do. I'll take my business elsewhere.")
		print("He storms out of your office. You stay sitting there, dumbfounded.")
		print("You go home, as without a case you don't have much to do. It doesn't matter anyway. You'll get another tomorrow.")
		input("\n \n \nT H E   E N D")
		return True
