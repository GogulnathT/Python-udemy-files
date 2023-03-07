day = 'Monday'
temperature = 40
raining = False  # assigning a boolean value to var raining

# when using multiple boolean operators, better to use
if (day == 'Saturday' and temperature > 37) or not raining:
    print('Good day for swimming')  # paranthesis
else:
    print('no swimming')

if 0:  # here 0 eqautes to False in python
    print('true')
else:
    print('false')

if '':  # empty string is also false
    print('true')
else:
    print('false')
