#1
list1=[1,2,3,4,5]
print(list1)
sum = 0
for i in list1:
    sum+=i
    i+=1
print("Sum = ",sum)

#2-multiply all items in a list
list2=[1,2,3,4,5]
mul=1
for i in list2:
    mul*=i
    i+=1
print("Product = ",mul)

#3-Largest no in list
list3 = [5,3,9,6,7,4]
list3.sort(reverse=True)
print("Largest no in list3 = ",list3[0])
         #OR
max=list3[0]
for i in list3:
    if i>max:
        max=i
        i+=1
print("Largest no in list3 = ",max)

#4 Smallest no in list
list4 = [5,3,9,6,7,4]
list4.sort()
print("Smallest no in list4 = ",list4[0])
        #OR
min=list4[0]
for i in list4:
    if i<min:
        min=i
        i+=1
print("Smallest no in list4 = ",min)

#5
list5 =  ['abc', 'xyz', 'aba', '1221']
l=len(list5)
print("Length of list5 is = ",l)
n=0
for i in list5:
    if len(i)>2 and i[0]==i[-1]:
        n+=1
print("No of strings with  first and last character same = ",n)

#
def last(n): return n[-1]
def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

#7


def fun(a):

    a.sort()
    print("sorted list = ", a)
    set7 = set(a)
    print(set7)
    list7 = tuple(set7)
    print(list7)
    L = list(list7)
    print(L)

a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
fun(a)

#8




