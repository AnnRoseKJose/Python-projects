dict1 = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964,
    "Year": 2022  # duplicate values wil overwrite existing values
}
print(dict1)

# To print brand value
print(dict1["Brand"])
# OR
print(dict1.get("Brand"))

# To print length and type of dict
print(len(dict1))
print(type(dict1))

# To print keys and values separately
keys = dict1.keys()
print(keys)
values = dict1.values()
print(values)

# To add new item
dict1["Colour"] = "Red"  # or dict1.update({"colour" : "red"})
print(dict1)

# to get items
x = dict1.items()  # will return each item in a dictionary, as tuples in a list
print(x)

# Check if Key Exists
if "Size" in dict1:
    print("Yes, 'Size' is the key in dict1")
else:
    print("No, 'Size' is not in dict1")

# To copy dict
dict2 = dict1.copy()
print(dict2)

# remove the item with the specified key name
dict2.pop("Model")
print(dict2)

# remove the last inserted item
dict2.popitem()
print(dict2)

# delete
del dict2["Year"]
print(dict2)

# clear
dict2.clear()
print(dict2)
