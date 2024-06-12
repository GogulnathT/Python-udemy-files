# slicing string is extracting a substring from a string using indexing 
# indexing[]   slice()
# [start:stop:step] --> indexing
# the stopping index is not inclusive

name = "GogulnathT"
first_name = name[:5]
last_name = name[5:]
step_name = name[::2]
reversed_name = name[::-1]
negative_name = name[:-5]
print(first_name)
print(last_name)
print(step_name)
print(reversed_name)
print(negative_name)

# using the slice() function
# slice(start, stop, step)
website = "www.google.com"
sliced = slice(4,-4,) #this is a slice object
print(website[sliced])
