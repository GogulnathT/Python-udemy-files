# lambda function = function written in 1 line using lambda keyword;
#                   accepts any number of arguments, but only has one expression
#                   (like a shortcut)
#                   (useful if needed for short period of time; throw-away)
#
# syntax for lambda func:
# lambda parameters: expressions

# def double(x):
#     return x*2
# print(double(5))
# above func as lambda func
double = lambda x : x*2
print(double(5))

multiply = lambda x,y : x*y
print(multiply(8,6))

full_name = lambda first_name, last_name : first_name + " " + last_name
print(full_name("Gogulnath","T"))

age_check = lambda age : True if age >= 18 else False # using if-else with lambda func
print(age_check(23))