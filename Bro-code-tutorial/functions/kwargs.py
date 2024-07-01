# **kwargs = parameter that will pack all arguments into a dictionary 
#            useful so that a function can accept a varying amount of keyword argument

def hello(**kwargs): #krargs is just a placeholder for the dict

    # print("hello, ",kwargs['first'],kwargs['second']) 
    # #this is the way to access those keyword parameters without loop

    print("Hello,",end=" ")
    for key, value in kwargs.items():
        print(value,end=' ')

hello(first="First", second="second", third='third') #we can add keyword args to this function now 
    