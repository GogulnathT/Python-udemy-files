# list comprehensions = a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#
# list = [expression for item in iterable]
# list = [expression for item in iterable if conditional]
# list = [expression (if/else) for item in iterable]

# eg of list com where we are creating a list and defining the range
squares = [i * i for i in range(1,11)]
print(squares)

# eg 2 list comp similar to lambda
students = [100,80,23,44,0,36,90,100,70,50]
# passed_students = list(filter(lambda x : x>=60, students))
passed_students = [i for i in students if i >= 60] # does the same thing as the above line
print(passed_students)
#using else in list comps
passed_students = [i if i >= 60 else 'Failed' for i in students]
print(passed_students)