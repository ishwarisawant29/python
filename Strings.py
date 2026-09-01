#String 

first_name = "Ishwari"
last_name = "Sawant"

# 1. Concatenation: + operator 
full_name = first_name + " " + last_name
print(full_name)

# 2. .join() method
full_name1= " ".join([first_name, last_name])
print(full_name1)

# 3. (,) operator
print(first_name, last_name)

#4. F-strings (formatted string literals)
full_name3 = f"{first_name} {last_name}"
print(full_name3)


#indexing
college = "Thakur College of Engineering and Technology"
print(college[0])  
print(college[7])
print(college[-1]) #last character
#note: cant reassign a character in a string using indexing as strings are immutable


#slicing
#str[Starting index: Ending index]
college = "Thakur College of Engineering and Technology"
print(college[0:6])  
print(college[:14]) # same as college[0:14]
print(college[7:])  # same as college[7:len(college)]


# string functions
hobby = "Reading Books"
print(len(hobby))               # return length of the string
print(hobby.endswith("s"))      # return boolean values
print(hobby.startswith("R"))    # return boolean values
print(hobby.capitalize())       # capitalize first letter of the string
print(hobby.replace("o", "a"))  # replace a character in the string
print(hobby.find("B"))          # return 1st index of the character in the string
print(hobby.count("o"))         # return number of occurrences of the character in the string
print(hobby.upper())            # convert string to uppercase
print(hobby.lower())            # convert string to lowercase

#practice Questions:
#1. WAP to input user's first name & print its length.
first_Name = input("Enter your first name: ")
print(len(first_Name))

#2. WAP to find the occurrence of '$' in a String.
string = input("Enter a string: ")
print(string.count('$'))

