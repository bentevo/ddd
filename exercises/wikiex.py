import requests

# a function with the URL, getting the data from the wikipage, and the choice between the description and the extract
def api_call (title, value):
	url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
	req = requests.get(url)
	wiki_data = req.json()

	if req.status_code != 200:
	    print(f"We got an error: {req.status_code}")
	    exit()

	if value == "description":
		print(wiki_data["description"])

	if value == "extract":
		print(wiki_data["extract"])

	return title, value


# asking the user for imput
title = input("What article do you want to check out? ").title().strip()
value = input("Do you want to see the description or extract? ").lower().strip()

# printing a newline for the legibility
# priting the value and title and adding in the description or extract
print("\n")
print(f"Here is the {value} for {title}")
api_call(title, value)