#### **.PYTHON\_DAY 1.**



###### 🐍 **Python Basics Notes**

###### 

###### 1️⃣ Introduction to Python

Python is a high-level, interpreted programming language created by

Guido van Rossum in 1991.

It is known for:

• Simple syntax

• Easy readability

• Powerful features

• Beginner-friendly design

Python is used in:

• Web Development

• Data Science

• Machine Learning

• Automation

• Software Development

Official website:

Python



###### 2️⃣ Data Types in Python

Data types define the type of value a variable can store.



🔹 1. Integer (int)

Whole numbers (positive or negative).

x = 10

y = -5



🔹 2. Float (float)

Decimal numbers.

price = 99.99

height = 5.8



🔹 3. String (str)

Text data (written inside quotes).

name = "Anu"

message = 'Hello Python'



🔹 4. Boolean (bool)

Only two values:

• True

• False

is\_student = True

is\_logged\_in = False



🔹 5. Complex (complex)

Numbers with real and imaginary parts.

z = 3 + 4j



###### 3️⃣ Comments in Python

Comments are used to explain code.

They are ignored by Python.



🔹 Single-line Comment

\# This is a comment

print("Hello")



🔹 Multi-line Comment

"""

This is

a multi-line

comment

"""



###### 4️⃣ Types of Operators in Python

Operators are symbols used to perform operations.



🔹 1. Arithmetic Operators

Operator

Meaning

Example

\+

Addition

5 + 2

\-

Subtraction

5 - 2

\*

Multiplication

5 \* 2

/

Division

5 / 2

%

Modulus (remainder)

5 % 2

\*\*

Power

5 \*\* 2

//

Floor division

5 // 2

Example:

a = 10

b = 3



print(a + b)

print(a % b)



🔹 2. Comparison Operators

Used to compare values.

Operator

Meaning

==

Equal

!=

Not equal

>

Greater than

<

Less than

>=

Greater or equal

<=

Less or equal

Example:

print(10 > 5)



🔹 3. Logical Operators

Used with conditions.

Operator

Meaning

and

Both conditions must be true

or

At least one true

not

Reverse the result

Example:

x = 10



print(x > 5 and x < 20)



🔹 4. Assignment Operators

Operator

Example

=

x = 5

+=

x += 2

-=

x -= 2

\*=

x \*= 2

/=

x /= 2

🔹 5. Membership Operators

Operator

Meaning

in

Present in sequence

not in

Not present

Example:

name = "Python"

print("P" in name)



###### 5️⃣ Type Conversion in Python

Type conversion means converting one data type to another.

There are two types:



🔹 1. Implicit Type Conversion (Automatic)

Python automatically converts data type.

x = 10      # int

y = 5.5     # float



result = x + y

print(result)

Output:

15.5

Python automatically converts int to float.



🔹 2. Explicit Type Conversion (Type Casting)

When we manually convert data type using functions.



###### 6️⃣ Type Casting in Python

Type casting functions:

Function

Converts To

int()

Integer

float()

Float

str()

String

bool()

Boolean

🔹 Convert String to Integer

x = "100"

y = int(x)

print(y)



🔹 Convert Integer to String

num = 50

text = str(num)

print(text)



🔹 Convert Float to Integer

price = 99.99

value = int(price)

print(value)

Note:

int() removes decimal part (does not round).



###### 7️⃣ Input in Python

The input() function is used to take user input.



🔹 Basic Input

name = input("Enter your name: ")

print("Hello", name)

Important:

Input always returns string by default.



🔹 Taking Integer Input

age = int(input("Enter your age: "))

print(age)



🔹 Taking Float Input

price = float(input("Enter price: "))

print(price)



🔹 Multiple Inputs in One Line

a, b = map(int, input("Enter two numbers: ").split())

print(a + b)



📌 Final Summary

You learned:

• Introduction to Python

• Data Types (int, float, str, bool, complex)

• Comments (single \& multi-line)

• Types of Operators

• Type Conversion (implicit \& explicit)

• Type Casting

• Input in Python





#### 📝 Practice Questions



1️⃣ Data Types \& Type Checking

Write a Python program that:

• Takes a number as input from the user

• Prints the value

• Prints its data type using type()

👉 Example Output:

Enter a number: 25

Value: 25

Type: <class 'int'>



2️⃣ Operators \& Calculation

Write a program that:

• Takes two numbers as input

• Prints:

o Addition

o Subtraction

o Multiplication

o Division

o Modulus

👉 Example:

Enter first number: 10

Enter second number: 3

Addition: 13

Subtraction: 7

Multiplication: 30

Division: 3.33

Modulus: 1



3️⃣ Type Casting

Write a program where:

• You take age as input (it will be string by default)

• Convert it into integer using type casting

• Add 5 to the age

• Print the updated age

👉 Example:

Enter your age: 20

After 5 years: 25



4️⃣ Logical \& Comparison Operators

Write a program that:

• Takes a number from user

• Checks if the number is:

o Greater than 10

o And less than 50

• Print "Valid Number" if true

• Otherwise print "Invalid Number"







