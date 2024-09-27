# reduce() =  apply a function on an iterable and reduce it to a single cumulative value
#             perform function on first two elements and repeats process until 1 value remains
#               eg [4,3,2,1] -> [7,2,1] -> [9,1] -> [10]
#
# reduce(function, iterable)

import functools

letters = ["H",'E','L','L','O']
word = functools.reduce(lambda x, y: x+y,letters)
# here x and y are the first two elements of the iterables on which the func is performed and
# repeated for the rest of the list
print(word)

nums = [5,4,3,2,1]
factorial = functools.reduce(lambda i,j : i*j , nums)
print(factorial)