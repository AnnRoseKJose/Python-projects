#1
x="Hello how are you"
r=x[::-1]
print(r)
y=r.split()
print(y)
seperator="."
z=seperator.join(y)
print(z)

#2-to print int and char separately
a=[3,4,'r','g',4,'e']
b=[]
c=[]
a.append(5)
print(a)
for i in a:
    if (type(i)==int):
        b.append(i)
    else:
        c.append(i)
print("Integers = ",b)
print("Characters = ",c)

#3
word = "Good morning"
z=word.split()
print(z)
r=z[::-1]
print(r)
x="".join(r)
print(x)