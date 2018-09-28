# asking the user for the two names.
name_one = input("What is your name? ")
name_two = input("What is your partner's name? ")

# stripping the two names of extra spaces and capitalisation.
name_one = name_one.lower().strip()
name_two = name_two.lower().strip()

# checking the length of the names
if len(name_one) == len(name_two):
	print("Your name has the same amount of letters as your partner's name! ")
elif len(name_one) > len(name_two):
	print(name_one + " is a longer name than " + name_two + ".")
elif name_one < name_two:
	print(name_two + " is a longer name than " + name_one + ".")

# finding out whether names are equal or not, including the printed text for the compatability 
if name_one == name_two:
	print("You have the same name as your partner! Very compatible, wow. ")
elif name_one > name_two:
	print("Turns out your partner has the superior name.") 
elif name_one < name_two:
	print("You have a longer name than your partner, congratulations, you're superior! ")

# deciding how many characters 
if name_one > name_two:
	print("The difference between your names is " + str(len(name_two) - len(name_one)) + " characters. ")
elif name_one < name_two:
	print("The difference between your names is " + str(len(name_one) - len(name_two)) + " characters. ")

# calculating the difference in characters
difference = abs(len(name_one) - len(name_two))

# calculating the percentages and printing the final message.
if difference == 0:
	print("Wow, turns out you two are a match made in heaven!")
elif difference == 1:
	print("Turns out you two have an 80% match. Surely you two will have a wonderful relationship! ")
elif difference == 2:
	print("There's a 60% match here. Turns out you're a good match, but you might need to look into finding another partner. ")
elif difference == 3:
	print("Turns out you two only match for 40%... Maybe it's time to look for someone else. ")
elif difference == 4:
	print("Turns out you are only a 20% match. It's time to break things up. ")
else:
	print ("Oh goodness, this is a 0% match. Good luck finding something better for you! ")

