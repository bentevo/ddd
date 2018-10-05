# the words that are not correct are listed in the 'wrong' list, and the words are an empty list for the user to add
wrong = ["apples", "cheese", "fries", "banana", "kangaroo", "quick", "triangle", "manatee"]
words = [] 

# input sentence.
sentence = input("Hello! Please enter your sentence here. ")

# splitting the sentence into words
list(sentence)
words = sentence.split(" ")

# creating a forloop to make sure all words are checked for the wrong words through an if-statement.
# within the if-statement the wrong words are replaced by the correct words.
# the basic assignment is still in the code, but hidden through the #
index = 0 
for word in words:
	#print(words[index])
	if words[index] in wrong:
		#print("Error")
		if words[index] == "apples":
			words[index] = "oranges"
		elif words[index] == "cheese":
			words[index] = "milk"
		elif words[index] == "fries":
			words [index] = "potatoes"
		elif words[index] == "banana":
			words[index] = "coconut"
		elif words[index] == "kangaroo":
			words [index] = "bear"
		elif words[index] == "quick":
			words[index] = "slow"
		elif words[index] == "triangle":
			words [index] = "square"
		elif words[index] == "manatee":
			words[index] = "seal"
		else:
			words[index] = words[index]
	else: 
		#print("No problem.")
		" "
	index = index + 1

# joining all the words back together into a proper sentence.
words = " ".join(words)

# priting the new and corrected statement back to the user.
print("The correct sentence is: " + words)
