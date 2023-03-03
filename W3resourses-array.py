#1
list = [1, 3, 5, 7, 9]
for i in list:
    print(i)
print("Access 1st 3 items individually")
a=list[:3]
for j in a:
    print(j)

#2
list2=['i',1, 3, 5, 7, 9]
print("Original array = ",list2)
list2.append(11)
print("New array = ",list2)

#3-Reverse order of items
list3=[1, 3, 5, 3, 7, 1, 9, 3]
print("List3 = ",list3)
revlist3=list3[::-1]
print("Reversed List3 = ",revlist3)

#4
from sys import getsizeof
list4 =  [1, 3, 5, 7, 9]
print("List4 = ",list4)
print("Length of list4 = ",len(list4))
b=getsizeof(list4)
print(b)

#5
