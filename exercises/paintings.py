f = open("paintings.csv")
txt_file = open("new_paintings.txt", "w")
paintings = []

for line in f:
	row = line.strip().split(",")
	paintings.append(row) 
	painting = row[0]
	artist = row[1]
	value = row[2]
	feedback = painting + " is a painting by " + artist + ", which was sold for " + value + " million euros. " + "\n"
	#print(feedback)
	#txt_file.write(feedback)
	# making sure the value is displayed in numbers, not text
	#new_value = value + "000000"
	new_value = float(value) * int(1000000)
	new_value = int(new_value)
	new_feedback = painting + " is a painting by " + artist + ", which was sold for " + str(new_value) + " euros." + "\n"
	txt_file.write(new_feedback)

painting = input("What is the name of the painting? ")
artist = input("Who is the artist of the painting? ")
value = int(input("How much is the painting worth in millions? "))	
new_value = str(value * 1000000)

new_row = painting + " is a painting by " + artist + ", which was sold for " + new_value + " euros." + "\n"
txt_file.write(new_row)

f.close()
txt_file.close()