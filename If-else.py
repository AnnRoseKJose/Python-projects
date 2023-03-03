#if
a = 40
b = 30
if (a>b):
    print(a ,"is greater than",b)

#if-elif
a = 33
b = 33
if (a>b):
    print("a is greater than b")
elif a == b:
    print("a is equal to b")

#if-else
a = 33
b = 43
if (a>b):
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("b is greater than a")

#To check age eligibility
age = int(input("Enter the age : "))
if (age>18):
    print("Eligible for vote")
else:
    print("Not eligible for vote")

#To check greatest of 3 nos.
a = int(input("Enter the a : "))
b = int(input("Enter the b : "))
c = int(input("Enter the c : "))
if (a>b and a>c):
    print("a is gratest")
elif (b>a and b>c):
    print("b is greatest")
else:
    print("c is greatest")

#Nested if
x = int(input("Enter the no : "))
if (x > 10):
  print(x,"is above 10")
  if (x > 20):
    print("and also above 20!")
  else:
    print("but not above 20.")