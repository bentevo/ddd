# names of friends
names = ['Bente', 'Lobke', 'Veerle']
snacks = []

# creating a for loop to not repeat all lines (incl. name, length of the name, adding the right snack, etc.)
for name in names:
	print("Hi " + name + "!")
	snack = input("What is your favourite snack? ")
	snacks.append(snack)
	name_length = len(name)
	print("Length of the name is: " + str(name_length) + " characters. ")

#adding the index to assign the right snack to the right name
index = 0
for name in names: 
	print(name + "'s favourite snack is: " + snacks[index] + ".")
	index = index + 1
