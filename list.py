list1=["apple","banana","orange",9,8]
print(list1)

#index calling#
print(list1[2])

#replace#
list1[2]='cherry'
print(list1)

#append#
list1.append(7)
print(list1)

#insert#
list1.insert(3,10)
print(list1)

#remove#
list1.remove(10)
print(list1)

#delete#
del list1[2]
print(list1)

#clear#
list1.clear()
print(list1)

#sorting
list2=["apple","mango","banana","orange","cherry"]
list2.sort()
print(list2)
list2.sort(reverse=True)
print(list2)