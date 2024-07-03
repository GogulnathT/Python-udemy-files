# walrus operator :=
# new to python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression
# Introduced in python 3.8, the walrus operator, (:=), formally known as the assignment expression operator, 
# offers a way to assign to variables within an expression, including variables that do not exist yet.

# print(happy = True) # this will cause an error as happy was not defined before the print
print(happy := True) # as the walrus operator is used, this wont cause an error

foods = []
while food := input("Enter food item: ") != 'quit': # using walrus op to assin value as part of larger expression
    foods.append(food)