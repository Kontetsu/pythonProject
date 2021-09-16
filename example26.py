# Print all animals
animals = ["Dog", "Cat", "Fish"]
for animal in animals:
    print(animal)

# Print all fruits
fruits = ("apple", "pinnaple", "peach")
for fruit in fruits:
    print(fruit)

# Print all car details
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for v in thisdict.values():
    print(v)

animals = ["Dog", "Cat", "Fish"]
fruits = ("apple", "pinnaple", "peach")

thisdict = {  "brand": "Ford",
              "model": "Mustang",
              "year": 1964
              }



for fuit in fruits:
    print("Fruits {}".format(fuit))

for animal in animals:
    print("animal {}".format(animal))

for vehicle in thisdict.values():
    print("vehicle {}".format(vehicle))
