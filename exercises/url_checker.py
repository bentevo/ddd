import requests 

# enter the user's url
user_url = input("Please enter your url here. ").strip()

# defining the variables 
req = requests.get(user_url)
status = req.status_code
headers = req.headers

# printing the error message if the status code is not 200 (OK)
if status is not 200:
	print(f'Something went wrong, please try again. ')
	exit()

# printing the headers 
for key, value in headers.items():
	print(f'{key}: {value}')

text = req.text

# extra: looping the lines (splitting the text by line) until the index is 10 so it displays the first 10 lines.
index = 0
while index < 10:
	line = text.splitlines()[index]
	print(line)
	index = index + 1
