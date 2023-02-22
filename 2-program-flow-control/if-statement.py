name = input('Enter your name : ')

#here we are using the keyword int to convert the input data
#to int data type, however if we enter a data type that cannot be 
# converted to int type it will throw an error; replacement field is also being used here and can be used with any string
age = int(input('What is your age, {}? '.format(name))) 

#the type() is a function to find the data type of a variable
print('Your name is {0} and you age is {1}.\nThe type of variable \'age\' is {2}\n'
      .format(name, age, type(age))) 

#if-else condition
if age>=18:
    print('You can drive {0}'.format(name))
    print('Please drive carefully\n')
else:
    print('You cannot drive.\nYou need to wait for {} years\n'.format(18-age))

#same as the above but the conditions are reversed
if age < 18:
    print('You cannot drive.\nYou need to wait for {} years\n'.format(18-age))
else:
    print('You can drive {0}'.format(name))
    print('Please drive carefully\n')    