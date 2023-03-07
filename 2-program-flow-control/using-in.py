parrot = 'Norwegian Blue'
letter = input('Enter the letter : ')

if letter in parrot : #here 'in' is used to check if one string is present in anoter
    print(True) 
else :
    print(False)

#using not in 
activity = input("What would you like to do today?")
if 'cinema' not in activity.casefold() :
    print('But I want to watch cinema')
else :
    print('Sure')