# semi-pyramid with *
for i in range(n):
     for j in range(i + 1):
        print("*", end=" ")
    print()

# half pyramid a using numbers
for i in range(5):
    for j in range(i + 1):
        print(j + 1, end=" ")
    print()

# half pyramid using alphabets
ascii_value = 65
for i in range(5):
    for j in range(i + 1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    ascii_value += 1
    print("")

# inverted half pyramid using *
# r=int(input("Enter no of rows: "))
for i in range(4, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    print()

# 2 inverted half pyramid using 7
for i in range(7, 0, -1):
    for j in range(0, i):
        print("7", end=" ")
    print()

# Inverted half pyramid using numbers
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# full pyramid using *
# r = int(input("Enter number of rows: "))
# k = 0
# for i in range(1,r+1):
#     for space in range(1,(r-i)+1):
#         print(end=" ")
#     while k != (2 * i - 1):
#         print("* ", end="")
#         k += 1
#     k = 0
#     print()
n = 5
for i in range(n):
    for j in range(n - i):
        print("", end=" ")
    for k in range(i + 1):
        print("*", end=" ")
    print()

# inverted-full pyramid using *
n = 5
for i in range(n):
    for j in range(i + 1):
        print("", end=" ")
    for k in range(n - i, 0, -1):
        print("*", end=" ")
    print()

# To print diamond
n = 5
for i in range(n):
    for j in range(n - i):
        print("", end=" ")
    for k in range(i + 1):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i + 1):
        print("", end=" ")
    for k in range(n - i, 0, -1):
        print("*", end=" ")
    print()

# 1 number pattern semi-pyramid
for i in range(7):
    for j in range(i + 1):
        print(j + 1, end=" ")
    print()

# 3
k = 0
for i in range(7, 0, -1):
    k = k + 1
    for j in range(0, i):
        print(k, end=" ")
    print()

# 4
for i in range(7):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# square using *
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()

# square using nos.
for i in range(4):
    for j in range(4):
        print(j + 1, end=" ")
    print()

# 5 (imp*)
n=5
for i in range(5):
    for j in range(i + 1):
        print(i+1, end=" ")
    for k in range(n-i-1, 0, -1):
        print(j+2, end=" ")
        j+=1
    print()
