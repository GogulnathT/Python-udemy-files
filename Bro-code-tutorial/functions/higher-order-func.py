# Higher Order function = a function that either :
#                         1. accepts a function as an arg/parameter
#                         or
#                         2. returns a function
#                            (This is possible as funcs are treated as objects in python)

#eg for first scenario
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud) # passing the func loud as a parameter for the func hello

#eg for scenario 2
def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2) # divide variable is calling divisor func and will get dividend as return
print(divide(10)) # divide has the dividend function now, so it can be called