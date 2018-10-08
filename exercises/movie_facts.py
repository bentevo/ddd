movies = {
	"title" : "Harry Potter and the Philosopher's Stone",
	"year" : 2001,
	"duration" : 159,
	"director" : "Chris Columbus",
	"actors" : ["Daniel Radcliffe", "Emma Watson", "Rupert Grint"]
}

for key, value in movies.items():
	if key == "duration":
		print(f"{key} : {value} minutes")
	elif key == "actors":
		print(key + " : " + ", ".join(value))
	else:
		print(f"{key} : {value}")
