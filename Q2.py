#WAP that accepts a list of integers and check the length and 5th element. Return true if length of
# list is 8 and and the 5th element occurs thrice in the said list
list=[19,15,5,7,5,5,4,2]
l = len(list)
print("Length of list = ",l)
f = list[5]
print("5th element in the list = ",f)
x = list.count(f)
print(f,"occurs",x,'times in list')
if l==8 and x==3:
    print("True")
else:
    print("False")