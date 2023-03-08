parrot = 'Norwegian Blue'

for x in parrot:
    print(x, end='')

numbers = '234;23423[424/2467.345>5;53453'

separators = ''
# we are separating the non numeric characters from the string and storing it in separators string
for x in numbers:
    # here x.isnumeric returns true if the char x is numeric, since we want others, we are using not before that
    if not x.isnumeric():
        separators += x
print('\n', separators)
