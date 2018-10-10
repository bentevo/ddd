import requests
import json

user_url = input("What article do you want to read? ").strip().replace(' ', '_')
language = ["en", "nl", "fr"]
languages = ["English", "Dutch", "French"]

index = 0
for item in language:
	url = f"https://{item}.wikipedia.org/api/rest_v1/page/summary/{user_url}"

	req = requests.get(url)
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

