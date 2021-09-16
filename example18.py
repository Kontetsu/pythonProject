# Create and print dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Change value based on key
thisdict["year"] = 2018
print(thisdict)
# Update value
thisdict.update({"year": 2020})
print(thisdict)
# Add value (create new key and value)
thisdict["color"] = "red"
print(thisdict)
# Removing item with specified key name
thisdict.pop("model")
print(thisdict)
# Removing item with specified key name, also possible to remove whole dict!
del thisdict["color"]
print(thisdict)
# Make dictionary empty
thisdict.clear()
print(thisdict)
