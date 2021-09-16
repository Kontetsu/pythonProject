food = "pica"
#print(food)
food = food + " with cheese"
print(food)

#idx = food.index("e")
#print(idx)

#food = "pica"
#print(food)
#food = food + " with cheese"
#print(food)

#idx = food.find("test")
#print(idx)

#print("compare")
#print(food.find("e") == food.index("e"))

counter = 0
positions = []
positions_others = []
for c in food:
    if c == "e":
        positions.append(counter)
    else:
        positions_others.append(counter)
    counter += 1
print("The letter 'e' is in the following posstion {}".format(positions))
print("The letter 'e' is in the following posstion {}".format(positions_others))

combine = positions + positions_others

combine.sort()
print(combine)

combine.reverse()
print(combine)
