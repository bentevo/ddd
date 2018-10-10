import requests
import json

# asking the user for a subject of an article
user_url = input("What article do you want to read? ").strip().replace(' ', '_')

# lists of the language codes and the display name of the languages for the print statements
language = ["en", "nl", "fr"]
languages = ["English", "Dutch", "French"]

# creating a for loop to display all the different languages.
index = 0
for item in language:
	url = f"https://{item}.wikipedia.org/api/rest_v1/page/summary/{user_url}"

	req = requests.get(url)
	status = req.status_code
	# printing the error message if the status code is not 200 (OK)
	if status is not 200:
		print(f'Something went wrong, please try again. ')
		exit()

	# printing the title, description and extract if they're available
	data = json.loads(req.text)
	print(f'\n{languages[index]}: ')
	if "title" in data:
		title = data["title"]
		print(title)
	if "description" in data:
		description = data["description"]
		print(description)
	if "extract" in data:
		extract = data["extract"]
		print(extract)
	index = index + 1

