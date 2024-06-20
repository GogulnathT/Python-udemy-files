#  *args = parameter that will pack all the arguments into a tuple
#          useful so that a function can accept a varying number of arguments 

def add(*args): #here args is just a place holder, it can be anything, '*' is important
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,45,877))