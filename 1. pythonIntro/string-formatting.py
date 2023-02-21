for i in range(1, 13):
    print('No. {0:2} squared is {1:3} and cubed is {2:4}'.format(i, i**2, i**3))
    # here the numbers after the : in the replacement fields indicate the tab spaces for formatting the string

print()

for i in range(1, 13):
    print('No. {0:2} squared is {1:<3} and cubed is {2:^4}'.format(i, i**2, i**3))
    # the < here means to left align the numbers

print()

print('Pi is approximately {0}'.format(22/7))

# here .6f means 6 places after the decimal and it is mentioned without a number for spacing
print('Pi is approximately {0:.6f}'.format(22/7))

# here the number for spacing i.e 12 is mentioned along with precision
print('Pi is approximately {0:12.6f}'.format(22/7))

# here 50 precision spaces are specified
print('Pi is approximately {0:12.50f}'.format(22/7))

print('Pi is approximately {0:52.50f}'.format(22/7))
print('Pi is approximately {0:62.50f}'.format(22/7))

# the max precision is around 51-53 digits after which python just uses 0 to fill up
print('Pi is approximately {0:<72.50f}'.format(22/7))
print('Pi is approximately {0:<72.54f}'.format(22/7))
