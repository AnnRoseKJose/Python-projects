string = str(input("Enter a string :"))
print(len(string))
half = int(len(string)/2)
print(half)
if len(string)%2==0:
    a=string[:half]
    b=string[half:]
else:
    a=string[:half]
    b=string[half+1:]
if a==b:
    print(string,"string is symmetrical")
else:
    print(string,"string is not symmetrical")
if a==b[::-1]:
    print(string,"string is palindrome")
else:
    print(string,"string is not palindrome")
