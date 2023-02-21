# this type of string formatting was used in python2 and is now deprecated
# so using this should be avoided


age = 22
print('My age is %d years' % age)
major = 'years'
minor = 'months'
print('My age is %d %s and %d %s' % (age, major, 4, minor))
print('pi is approx %f' % (22/7))
# formatting i.e field width and precision is mentioned here
print('pi is approx %40.30f' % (22/7))
