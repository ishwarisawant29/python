#Variables and data types in python

name = "Ishwari"    #string()
age = 23            #integer()
height = 5.1        #float()
old = False         #boolean()
a = None            #NoneType()
print(type(name))
print(type(age))
print(type(height))
print(type(old))
print(type(a))

#operators in python

x = 10
y = 5

#arithmetic operators
print(x + y)  # addition
print(x - y)  # subtraction
print(x * y)  # multiplication
print(x / y)  # division
print(x % y)  # modulus
print(x ** y) # exponentiation
print(x // y) # floor division

#relational operators/comparison operators
print(x > y)   # greater than
print(x < y)   # less than
print(x == y)  # equal to
print(x != y)  # not equal to
print(x >= y)  # greater than or equal to
print(x <= y)  # less than or equal to

#logical operators
print(x > 5 and y < 10)  # logical AND
print(x > 5 or y < 10)   # logical OR
print(not(x > 5))        # logical NOT

#Assignment operators
x += 5   # equivalent to x = x + 5
y -= 2   # equivalent to y = y - 2
x *= 3   # equivalent to x = x * 3
y /= 2   # equivalent to y = y / 2

#Type Conversion 
a = 4
b= 6.2
print(a + b)  # addition of int and float(4.0 + 6.2 = 10.2)

#Type Casting
a = int(4.7)  # converting float to int(4)
b = float(5)  # converting int to float(5.0)
print(a)
print(b)

# important to note that type casting can lead to loss of data, converting float to int will truncate the decimal part. 
# string values cannot be converted to int or float directly, they need to be numeric strings.

#input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # converting input string to int
print("Hello, " + name + "! You are " + str(age) + " years old.") #input only returns string.

# Practice Questions
# 1. Write a Program to input 2 numbers & print their sum.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = num1 + num2
print("The sum is", sum)

# 2. WAP to input side of a square & print its area.
side = float(input("Enter the side of the square: "))
area = side * side
area2 = side ** 2
print("The area of the square is:", area)
print("The area of the square is:", area2)

# 3.WAP to input 2 floating point numbers & print their average.
num1 = float(input("Enter the first floating point number: "))
num2 = float(input("Enter the second floating point number: ")) 
average = (num1 + num2) / 2
print("The average is ", average)
