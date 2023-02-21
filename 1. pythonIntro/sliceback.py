from turtle import back, backward


letters = 'abcdefghijklmnopqrstuvwxyz'

# here slicing is done backwards as the step value is negative
backwards = letters[25:0:-1]
# however this slicing will only print all the letters upto a but not a as the last index in slicing is
#not included
print(backwards)

backwards = letters[25::-1]  # this will include the last index as well
print(backwards)

# this is the same as line12, this here is called a python idiom / slicing idiom
backwards = letters[::-1]
print(backwards)

print('\nsome common python idioms :')
print(letters[::-1])  # reversing a string

# this is used for getting a certain number of last characters
print(letters[-4:], letters[-1:])

# this is for getting a certain number of characters from the beginning
print(letters[:1])
# incase the string is empty this will return an empty string whereas letters[0] will
# produce error
