import requests 

user_url = input("Please enter your url here. ").strip()

req = requests.get(user_url)
status = req.status_code
headers = req.headers

if status is not 200:
	print(f'Something went wrong, please try again. ')
	exit()

for key, value in headers.items():
	print(f'{key}: {value}')

text = req.text

index = 0
while index < 10:
	line = text.splitlines()[index]
	print(line)
	index = index + 1

