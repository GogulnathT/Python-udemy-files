# keyword args = arguments preceded by an identifier when we pass them to a function
#                The order of the arguments doesnt matter, unlike positional arguments
#                Python knows the names of the arguments that our function receives 

def sample(first, second, third):
    print(first, second, third)

sample(second = 2, third = 3, first = 1)