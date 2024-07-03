# filter() = creates a collection of elements from an iterable for which a function returns true
# syntax:
# filter(function,iterable)

friends = [("Brandon",20),
           ("George",21),
           ("Alex",16),
           ("Brian",23),
           ("Peter",24),
           ("Lois",17)]

age = lambda data: data[1]>=18

drinking_friends = list(filter(age, friends))

print(drinking_friends)
