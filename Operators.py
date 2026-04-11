#Operators

a,b=12,4

#Arithmetic Operators
print("Arithmetic:")
print(a+b,a-b,a*b,a/b,a//b,a%b)

#Comparision Operators
print("\nComparision:")
print(a>b,a==b,a!=b)

#Logical operators
print("\nLogical:")
print(a>5 and b<10)
print(a>b or b<10)
print(not(a>b))

#Assignment Operators
print("\nAssignment:")
c=a
c+=b
print("c+=b:",c)
c*=2
print("c*=2:",c)


"""Arithmetic:
16 8 48 3.0 3 0

Comparision:
True False True

Logical:
True
True
False

Assignment:
c+=b: 16
c*=2: 32"""
