animals = ["Dog", "Cat", "Fish"]
lower_animal = []
fruits = ("apple", "pinnaple", "peach")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

#for anima in animals:
#    lower_animal.append(anima.lower())

print("List of animals ", animals)

for animal in animals:
    fave_animal = input("Enter yor favorite animal from the list: ")
    #print("Animals {}".format(animal))
    if animal == fave_animal:
        print("Your favorite animal Catis :", animal)
        break

#for fruit in fruits:
#   print("Fruits {}".format(fruit))

#for vehicles in thisdict.items():
#    print("Vehicles {} {}".format(vehicles[0], vehicles[1]))

#for k, v in thisdict.items():       # is better
#    print("Vehicles {} {}".format(k, v))