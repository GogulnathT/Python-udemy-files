import random as r #importing random module and using it as 'r'


choice = ''

while choice.casefold() != 'n':
    number = r.randint(1,100)  # randint is a function(aka method) in the random module which will generate a random integer
    # between two given numbers; a module will have many functions
    print("A random number between 1 and 100: ",number)
    choice = input('Do you want to continue(y/n) : ')
print('You have ended the game!')