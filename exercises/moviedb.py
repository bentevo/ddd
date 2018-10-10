import json

with open("movies.json") as f:
	movies = json.load(f)

print("Hello! What would you like to do?")

while True:
	print("Option 1: Filter on the first letter of the movie. ")
	print("Option 2: Filter on the release year of the movie. ")
	print("Option 3: Filter on the duration of the movie. ")
	print("Option 4: Filter on the title of the movie. ")
	print("Option 5: Close the program. ")

	option = input("What option do you want to pick? ")
	option = int(option)

	if option == 1:
		user_letter = input("On what letter do you want to filter the movies? ")

		for movie in movies:
				year = movie["year"]
				title = movie["title"]
				duration = movie["duration"]
				if title[0] == user_letter:
				#	print(movie)
					print(f'{title}, {year}. ')
	elif option == 2:
		user_year = input("From what year do you want to see a movie? ")

		for movie in movies:
				year = movie["year"]
				title = movie["title"]
				duration = movie["duration"]
				if int(user_year) == int(year):
				#	print(movie)
					print(f'{title}, {year}. ')
	elif option == 3:
		user_duration = input("The duration of the movie should be longer than ... minutes. ")

		for movie in movies:
			year = movie["year"]
			title = movie["title"]
			duration = movie["duration"]

			if int(user_duration) <= int(duration):
				print(f'{title}, {year} ({duration} minutes). ')
	elif option == 4:
		user_title = input("What movie are you interested in? ")
		user_title = user_title.strip().title()

		for movie in movies:
			title = movie["title"]
			genres = movie["genres"]
			director = movie["director"]
			duration = movie["duration"]
			actors = movie["actors"]
			if user_title in title:
				print(f"Movie title: {title}")
				print(f"Movie director: {director}")
				print(f"Movie duration: {duration} minutes")
				print(f"Actors: ")
				for actor in actors:
					print(f"     {actor}") 
				print(f"Genres:")
				for genre in genres:
					print(f"     {genre}")
	elif option == 5:
		# closing the file, and giving the user the right feedback.
		print("Goodbye! ")
		exit()
	else: 
		# in case someone entered a number/character that didn't match the given options. 
		print("Something went wrong, please try again! ")
		exit()

