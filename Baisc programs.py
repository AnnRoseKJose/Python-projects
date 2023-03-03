#odd or even
n=int(input("Enter a no. : "))
if n%2==0:
    print("The no is even")
else:
    print("The no is odd")

#WAP to find the given string is palindrome and symmetrical
string = str(input("Enter a string :"))
print(len(string))
half = int(len(string)/2)
print(half)
if len(string)%2==0:
    a = string[:half]
    b = string[half:]
else:
    a = string[:half]
    b = string[half+1:]
if a == b:
    print(string,"String is symmetrical")
else:
    print(string,"String is not symmetrical")
if a==b[::-1]:
    print(string,"String is palindrome")
else:
    print(string,"String is not palindrome")

#Fibanocci series
n=int(input("Enter no of terms : "))
n1=0; n2=1; c=0;
if n<=0:
    print("The Output of your input is",n1)
else:
    print(n1,n2,end=" ")
    for x in range(2,n):
        c=n1+n2
        print(c,end=" ")
        n1=n2
        n2=c
