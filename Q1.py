#WAP to find list of integers with exactly two occurence of 19 and atleast three occurence of 5
list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):                         # iterating till the range
            ele = int(input())
            list.append(ele)                   # adding the element
print(list)
x=list.count(19)
print("No. of 19 = ",x)
y=list.count(5)
print("No. of 5 = ",y)
if x==2 and y>=3:
    print("True")
else:
    print("False")

