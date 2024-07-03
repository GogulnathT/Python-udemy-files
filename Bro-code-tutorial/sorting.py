# sort() method = used with lists
# sort() func   = used with iterables

students = ["John","Adam","Kenneth","Don","Hughie"]
students.sort() # sort method works with lists
# print(students)
students.sort(reverse=True) # reverse sorting of lists
# print(students)

# using sort function
students_tuple = ("John","Adam","Kenneth","Don","Hughie")
students_sorted = sorted(students_tuple) # this func takes an iterable(eg.tuple) and returns a list
# print(students_sorted)

students_2d = [("John","F",23),
               ("Adam","A",22),
               ("Kenneth","B",20),
               ("Don","C",24),
               ("Hughie","D",21)]

students_2d.sort() # this will sort the list as per the first column of the tuple
# print(students_2d)

# using the key parameter of sort()
grade = lambda grades : grades[1]
# lambda function is returning the index that needs to be considered for sorting
students_2d.sort(key=grade) # using the key parameter to sort this using the second column
# print(students_2d)
students_2d.sort(key=grade, reverse=True) 
# print(students_2d)

# tuple of tuples, so sort function 
students_2d_tuple = (("John","F",23),
               ("Adam","A",22),
               ("Kenneth","B",20),
               ("Don","C",24),
               ("Hughie","D",21))

sorted_students_2d_tuple = sorted(students_2d_tuple, key= lambda grades : grades[2])
print(sorted_students_2d_tuple)
