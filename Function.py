def sum(a,b):
    c=a+b
    print(c)

sum(4,5)

sum(3.5,4.5)

def pyr(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()

pyr(5)
pyr(3)

#odd or even
def odev(n):
    if n%2==0:
        print("The no is even")
    else:
        print("The no is odd")

odev(67)
odev(34)

#Q1
def list(a):
    l = len(a)
    print("Length of list = ", l)
    f = a[5]
    print("5th element in the list = ", f)
    x = a.count(f)
    print(f, "occurs", x, 'times in list')
    if l == 8 and x == 3:
        print("True")
    else:
        print("False")

a=[19,15,5,7,5,5,4,2]
list(a)

a=[3,5,1,6,5,8,4,5,0]
list(a)

#Q2
#No of heads = 35 no of legs = 94 , find no of chickens and rabbits
def q2(h,l):
    d=0;e=0;r=1;c=0
    d=2*h
    e=l-d
    r=e/2
    c=h-r
    print("No of chickens = ",c)
    print("No of rabbits = ",r)
q2(36,96)
                #OR
def solve(nh,nl):
    ns='No solution!'
    for i in range(nh+1):
        j=nh-i
        if 2*i+4*j == nl:
            print("No of chickens=",i, "No of rabbits=",j)
            break
    else:
            print(ns)

solve(30,111)


