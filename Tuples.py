tuple1 = ("apple", "banana", "cherry", "apple", "cherry")
print(tuple1)

#to print length
print(len(tuple1))

#to print the type
thistuple = ("apple",)
print(type(thistuple))

#index calling
print(tuple1[2])

#ranging all similar to strings

#Check if item exists or not
if "Orange" in tuple1:
  print("Yes, 'Orange' is in the tuple1")
else:
    print("No, 'Orange' is not in tuple1")

#replace tuple value
list1 = list(tuple1)
list1[3] = "kiwi"
tuple1 = tuple(list1)
print(tuple1)

#append
list1 = list(tuple1)
list1.append("orange")
tuple1 = tuple(list1)
print(tuple1)

#add tuple to tuple
y = ("mango",)
tuple1 += y
print(tuple1)

#insert
list1 = list(tuple1)
list1.insert(3,"papaya")
tuple1 = tuple(list1)
print(tuple1)

#remove
list1 = list(tuple1)
list1.remove("cherry")
tuple1 = tuple(list1)
print(tuple1)

#delete a variable
list1 = list(tuple1)
del list1[4]
tuple1 = tuple(list1)
print(tuple1)

#to completetly delte the tuple
#del tuple1
#print(tuple1)

#for loop
tuple2 = ("apple", "banana", "cherry")
for x in tuple2:
  print(x)

#to print length of tuple using for loop
for i in range(len(tuple2)):
    print (len(tuple2[i]))
print(len(tuple2))

#while loop
i = 0
while i < len(tuple2):
  print(tuple2[i])
  i = i + 1



