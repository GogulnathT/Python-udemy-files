# exception = events detected during the execution that interrupts the flow of a program

try: #the code inside the try block will have the code which might throw an error that we want to catch
    numerator = int(input('Enter a numerator'))
    denominator = int(input('Enter a denominator'))
    result = numerator/denominator
except ZeroDivisionError as e : #this catches a particular type of exception called zero division error
    print(e) # this variable e will let the users know what the exception is 
    print("Division by zero is not possible!")
except ValueError as e : # this catches error where value that is not supposed to be inputed 
    print(e)
    print("Enter only numbers")
except Exception as e: # this is a general term for catching any exception 
    print(e)
    print("something went wrong")
else: # the else block will be excecuted if the code within the try block does not throw any errors
    print(result)
finally: # this block is always in the end; this block will always execute whether an exception is caught or not
    print("This block will always execute as it is in 'finally:'")