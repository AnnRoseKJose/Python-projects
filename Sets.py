set1 = {"apple", "banana", "cherry","apple"} #duplicate are removed
print(set1)

#length and type of set
print(len(set1))
print(type(set1))

#for loop
for x in set1:
    print(x)

#since set is unordered indexing is not possible

#Check if item exists or not
print("orange" in set1)
if "Orange" in set1:
  print("Yes, 'Orange' is in the set1")
else:
    print("No, 'Orange' is not in set1")

#since set is unchangeable and unordered we cannot replace the items else we should convert it to list
list1 = list(set1)
list1[2] = "kiwi"
set1 = set(list1)
print(set1)

#add
set1.add("orange")
print(set1)

#add sets
set2 = {"banana","papaya"}
set1.update(set2)
print(set1)

#add any iterables
list1 = ["mango","pineapple"]
set1.update(list1)
print(set1)

#remove
set1.remove("pineapple")  #If the item to remove does not exist, remove() will raise an error.
print(set1)

#discard
set1.discard("pineapple")  #If the item to remove does not exist, discard() will NOT raise an error.
print(set1)

#pop
x = set1.pop()
print(x)
print(set1) # Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

#clear
set1.clear()
print(set1)

#delete
del set1
