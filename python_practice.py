# Write a Python program where:
# Store your age in a variable.
# Store your name in another variable.
# Store your marks in a list.
# Store your details (name and age) in a dictionary.
# Print the data type of each variable using type().
from os import remove


a=21
age=a
b="santosh"
name=b
markes=[90,89,60,89,99]
student={
    "name":"Santosh",
    "age":29
}
print(type(age))
print(type(name))
print(type(markes))
print(type(student))

#2.Create a variable num and store a float value in it.
# Create a variable text and store your name.
# Create a tuple of 3 numbers.
# Create a set with some duplicate values.
# Print:
# The data type of each variable
# The length of the tuple
# The set after duplicates are removed
num=90.98
text="santosh"
markes=(99,89,78)
B={12,12,12}
print(type(num))
print(type(text))
print(type(markes))
print(type(B))
print(len(markes))
print("Set values:",B)

#3.Create a list with 5 numbers,Convert that list into a tuple,Create a set from the list (include some duplicate values in the list,Create a dictionary where,keys are numbers from the tuple,Values are the square of those numbers,Print:The data type of each new variable,The dictionary,The maximum number from the tuple
a=[20,89,98,78]
b=tuple(a)
c=set(a)
D={}
for i in b:
    D[i]=i*i #square of number
print(type(a))
print(type(b))
print(type(c))
print(type(D))
print("Dictionary:",D)
print("maximum value:",max(b))

#4.reate a list with duplicate numbers, convert it into a set, then create a dictionary where each unique number is mapped to its cube, and print the maximum value from the original list.
a=[20,38,98,79,89,20]
b=set(a)
c=tuple(a)
D={}    
for i in b:
    D[i]=i**3 #cube of number

print(type(a))
print(type(b))
print(type(c))
print(type(D))
print("Directory:",D)
print("minimum value:",min(c))
print("sum of list:",sum(a))


a=(20,78,97,78,90)
b=list(a)
b.remove(78)
D={ }
for i in set(b):
    D[i]=i**2 #square of number
    
print("Dictionary:",D)
print("sum of list:",sum(b))


#Operators.
#1.Take two numbers, print their addition, subtraction, multiplication, division, check which number is greater, and print whether both numbers are positive using logical operators.
q=23
w=54
print("Addition:",q+w)
print("Subtraction:",q-w)
print("Multiplication:",q*w)
print("Division:",q/w)
if q>w:
    print("q is greater than w")
elif q<w:
    print("w is greater than q")
else:
    print("both are equal")
if q>0 and w>0:
    print("Both numbers are positive")
else:
    print("one or both numbers are not positive")

#2.Take two numbers, print their addition, subtraction, multiplication, division, check which number is greater, and print whether both numbers are positive using logical operators.
p=1
r=3
t=5
if p>r and p>t:
    print("p is greater")
elif r>p and r>t:
    print("r is greater")
else:
    print("t is greater")
if p==r==t:
    print("all numbers are equal")
else:
    print("all numbers are not equal")
total=p+r+t
if total % 5 == 0:
    print("total is divisible by 5")
else:
    print("total is not divisible by 5")
#Type Conversion & Type Casting (Python)
#1.Take a number from the user, convert it to an integer, check if it is even or odd and greater than 50, then convert it to a string and print its type.
A=input("enter a number:")
B=int(A)
if B%2==0:
    print("Even number")
else:
    print("odd number")

if B>50:
    print("greater than 50")
else:
    print("not greater than 50")
c=str(B)
print("Type after conversion:", type(c))
#3.Take a number from the user, convert it to integer, check whether it is positive, negative, or zero, and then print its square and cube.
Y=input("enter a number:")
Z=int(Y)
if Z>0:
    print("positive number")
elif Z<0:
    print("negative number")
else:
    print("Zero")
print("Square of number:",Z**2)
print("Cube of number:",Z**3)
