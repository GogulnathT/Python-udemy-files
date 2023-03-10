list1 = ['milk', 'eggs', 'rice', 'chicken', 'juice', 'apples']

for item in list1:
    if item == 'rice':
        continue  # using continue will skip the current iteration of the loop
    else:
        print(item)
print()
for item in list1:
    if item == 'chicken':
        print(item)
        break  # using break here will stop the loop
    print(item)
print()

# searching for an item
posi = None  # None is used to define a null value
for index in range(len(list1)):
    if list1[index] == 'juice':
        print('juice found at {0}'.format(index))
        break
print()
# a shortcut to find an item in the list witout loops
if 'chicken' in list1:
    print(list1.index('chicken'))
