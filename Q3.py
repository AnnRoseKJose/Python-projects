#WAP to convert GPAs to letter grades according to following table
g = float(input("Enter GPA : "))
if g>=4.0:
    print("Grade = A+")
elif g>=3.7:
    print("Grade = A")
elif g>=3.4:
    print("Grade = A-")
elif g>=3.0:
    print("Grade = B+")
elif g>=2.7:
    print("Grade = B")
elif g>=2.4:
    print("Grade = B-")
elif g>=2.0:
    print("Grade = C+")
elif g>=1.7:
    print("Grade = C")
elif g>=1.4:
    print("Grade = C-")
else:
    print("Grade = F")
