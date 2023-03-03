for i in range(1,10):
    print(i)

#sum upto 10
sum=0
for i in range(10):
  sum=sum+i
  i=i+1
print(sum)

#list in for loop
list=["Hello","Welcome","Hii"]
print(list)
for i in list:
  print(i)
  if i=="Hii":
    print("OK")

#Loop Through the Index Numbers
fruits = ["apple","banana","cherry","kiwi","mango"]
for i in range(len(fruits)):
    print(fruits[i])

#Sort fruits containing letter 'a' into a newlist
newlist=[]
for x in fruits:
    if "a" in x:
        newlist.append(x)  #OR newlist = [x for x in fruits if "a" in x]
print(newlist)

#Condition:Only accept items that are not "apple":
list1=[x for x in fruits if x!="apple"]
print(list1)
