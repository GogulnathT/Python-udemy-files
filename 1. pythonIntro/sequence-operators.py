string1 = 'He is '
string2 = 'eating '
string3 = 'dosa'

# here the + operator is used to concatenate the strings
print(string1 + string2 + string3)

print('He is ' 'eating ' 'dosa')  # this is same as line5

print(string3 * 5)  # string multiplications

# string operators also have operator precedance
print('Pizza' * (5+4))
print('Pizza' * 5 + '4', '\n')

# 'in' operator can be used to check is a string is a substring of another string
today = 'friday'
print('fri' in today)
print('day' in 'friday')
print('thur' in today)
print('mon' in 'friday')
