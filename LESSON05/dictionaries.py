# Dictionaries..
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")
print(band)
print(band2)
print(type(band))
print(len(band))

# AccessItems...
print(band["vocals"])
print(band.get("guitar"))

# list all keys..
print(band.keys())
print(band2.keys())

# list all values..
print(band.values())
print(band2.values())

# List of key/value pairs as tuples...
print(band.items())

# verify a key exists.
print("guitar" in band)
print("tripod" in band)

# Change values..
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# Remove items.
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())  # tuple.
print(band)

# Delete and clear items
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()  # clear
print(band2)

del band2

# Copy dictionaries.
# band2 = band  # create a reference to
# print("Bad Copy!")
# print(band2)
# print(band)

# band2["drums"] = "Tyron"
# print(band2)

band2 = band.copy()
band2["drums"] = "Tyron"
print("Good Copy!")
print(band)
print(band2)

# Or use a dictionary()
# constructor function...
band3 = dict(band)
print("Good Copy!")
print(band3)

# Nested dictionary..
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])
