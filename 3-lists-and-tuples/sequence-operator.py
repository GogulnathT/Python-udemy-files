# common operatons done in sequence types

even = [0, 2, 4, 6, 8, 10, 12, 14, 16]
odd = [1, 3, 5, 7, 9, 11, 13, 15, 17]

print(max(even))
print(max(odd))
print(min(even))
print(min(odd))

print(even.__len__())
print(len(odd))

s = 'mississippi'
print(s.count('s'))  # string is also a sequence type and
# this returns the no. of times s appears in this string
print(even.count(2))
