age = int(input('Enter your age'))

if age >= 16 and age <= 65:  # condition can also be like (16 <= age <= 65)
    print('You are of legal working age')
else:
    print('You cannot work')

# same condition as above but using 'or'
if age > 65 or age < 16:
    print('You cannot work')
else:
    print('You can work')
