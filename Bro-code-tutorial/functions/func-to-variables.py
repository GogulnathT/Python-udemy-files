# Assigning functions to variables

def hello():
    print("Hello")

print(hello) # since no (), this will print the memory address of the hello func
hi = hello # assigning the memory of hello to hi so that it will also work
hi()
