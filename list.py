#list
# create a list using[ ] brackets and separate the elements using commas
#elements of a list can be of any data type
#mutable: we can change the elements of a list after it is created

marks = [90, 80, 70,"pooja", 4.5, True]
print(marks)
print(marks[0])  # access element using index
print(marks[-1]) # access last element using negative index

#slicing
print(marks[0:3])  # access elements from index 0 to 2
print(marks[:3])   # access elements from the beginning to index 2
print(marks[4:])  # access elements from index 1 to the end
print(marks[::2]) # access every 2nd element from the list


#list Methods
list = [1, 2, 3, 4, 5]
list.append(60)  # add an element to the end of the list
print(list)

list.sort()  # sort the list in ascending order 
print(list)

list.sort(reverse=True)  # sort the list in descending order
print(list)

list.reverse()  # reverse the list
print(list)

list.insert(3, 6)  # insert an element at a specific index
print(list)

list.count(3)  # count the number of occurrences of an element in the list
print(list.count(3))

list.copy()  # create a copy of the list
print(list.copy())

list.remove(3)  # remove the first occurrence of the element from the list
print(list)

list.pop(2)  # remove the element at index 2 from the list
print(list)

list.clear()  # remove all elements from the list
print(list)


#Practice Questions
# 1. WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
movie = []
mov_1 = input("enter first movie name ")
mov_2 = input("enter second movie name ")
mov_3 = input("enter third movie name ")

movie.append(mov_1)
movie.append(mov_2)
movie.append(mov_3)
print(movie)


#2. WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

list1 = ["m","a","d","a","m"]
list2 = ["l","e","a","f"]

copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("palindrome")
else:
    print("not a palindrome")

copy_list2 = list2.copy()
copy_list2.reverse()
if (copy_list2 == list2):
    print("palindrome")
else:
    print("not a palindrome")


#3. Store the above values in a list & sort them from "A" to "D".
grades = ["C", "D", "A", "A", "B", "B", "A"]
grades.sort()
print(grades)
