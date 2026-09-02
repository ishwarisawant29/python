#tuple 
#creating a tuple using ()
#elements of a tuple can be of any data type
#immutable: we cannot change the elements of a tuple after it is created

tup = (1, 2, 3, "pooja", 4.5, True)
print(tup)
print(tup[0])      # access element using index
print(tup[-1])     # access last element using negative index
print(type(tup))   # check the type of the tuple


#methods of Creating a tuple
#1. using tuple() constructor
tup1 = (1, 2, 3, 4, 5)
print(type(tup1))

#2. using tuple() constructor with a list
list1 = [1, 2, 3, 4, 5]
tup2 = tuple(list1)
print(type(tup2))

#3. using one element tuple
tup3 = (1,)   # note the comma after the element
print(type(tup3))

#tuple methods
marks = (40, 50, 60, 70, 80)

print(marks.index(60))    # returns the index of the first occurrence of the element
print(marks.count(50))    # returns the number of occurrences of the element
print(len(marks))         # returns the number of elements in the tuple


#Practice Questions
#1. WAP to count the number of students with the "A" grade in the following tuple.
grades = ("C", "D", "A", "A", "B", "B", "A")
print(grades.count("A"))

