# Function = a block of code which is executed only when it is called 

def printer(load): #this is a function with positional arguments
    print(load)

load = input("Enter text: ")
printer(load)
printer("Hello")

#return = a function sends a value back to the function caller 
def multiplier(num1, num2):
    return num1*num2

print(multiplier(9,9))

