age = 22

# print('His age is ' + age)
# this will cause type error as age is int and cannot be concatenated with string

print(f"His age is {age} years")
# here mentioning f before the string makes it a string literal and now we can use variables of
# other types inside the quotes

# another eg
name = 'Gogulnath'
print(name + f'\'s age is {age} years')
# f-string type is used here also after the operator

# another eg
# using {} to directly insert an expression within a f-string
print(f'Pi is approximately {22/7 : .10f}')
pi = 22/7
# mentioning both precision and field width
print(f'Pi is approximately {pi:12.18f}')
