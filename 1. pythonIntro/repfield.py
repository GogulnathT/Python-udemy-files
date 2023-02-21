age = 22
print('Age is ' + str(age) + ' years')
# 'str' is used to coerce the age which is int into a string

# replacement fields can be used instead of str to achieve same output as line2
print('Age is {0} years'.format(age))  # here the {0} is the replacement field

# another eg
print('There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}'
      .format(31, 'Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec'))

print('There are {} days in {}, {}, {}, {}, {}, {} and {}'
      .format(31, 'Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec'))

# when using replacement fields, the index number is important for the order and not the actual order
print('Jan:{2} Feb:{0} Mar:{1}'.format(28, 30, 31))
