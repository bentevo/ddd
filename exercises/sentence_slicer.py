sentence = []

# list input
sentence = input("Enter your sentence here. ")

# measuring the lenght of the sentence
length_sentence = len(sentence)

# calculating the middle of the sentence (the 50% between 25% and 75%)
percent_25 = int(length_sentence) * float(0.251)
percent_75 = int(length_sentence) * float(0.751)

# printing the 'new' sentence
print(sentence[round(percent_25):round(percent_75)])

# advanced part:
# splitting the sentence
new_sentence = sentence.split(" ")
new_length = len(new_sentence)

p25 = round(new_length * 0.251)
p75 = round(new_length * 0.751)

new_sentence = new_sentence[p25:p75]

#joining the new sentence
print(" ".join())

