#conditional Statements
#if statement
age = 18
if age >= 18:
    print("You are eligible to vote.")


#if-else statement
age = 17
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


#if-elif-else statement
marks = 85
if marks >= 90:
    print("Grade: A")

elif marks >= 80:
    print("Grade: B")

elif marks >= 70:
    print("Grade: C")

else:
    print("Grade: D")


#nested if statement
age = 20
if age >= 18:
    if age >= 21:
        print("You are eligible to drink alcohol.")
    else:
        print("You are not eligible to drink alcohol.")

else:
    print("You are not eligible to vote or drink alcohol.")




#Practice Questions:
#1. WAP to check if a number entered by the user is odd or even.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")



#2.WAP to find the greatest of 3 numbers entered by the user.
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

if first_number >= second_number and first_number >= third_number:
    print("The first number is the largest.")

elif second_number >= first_number and second_number >= third_number:
    print("The second number is the largest.")

else:
    print("The third number is the largest.")



#3.WAP to check if a number is a multiple of 7
number = int(input("Enter a number: "))
if number%7 ==0:
    print("Multiple of 7.")
else:
    print("Not a multiple of 7.")