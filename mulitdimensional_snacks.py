friends = [ 
    ["Bente"],
    ["Lobke"],
    ["Veerle"]
]

for friend in friends:
    name = friend[0]
    name_length = len(name)
    snack = input(name + ", what is your favourite snack? ")
    friend.append(snack)
    print("The name " + name + " has " + str(name_length) + " characters. ")

for friend in friends:
    print(friend[0] + "'s favourite snack is " + friend[1])
