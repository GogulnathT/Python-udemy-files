random = ["randomness"]
choice = ''
choice = input('Do you want to append to the list?(Y/N)')
while choice.casefold() != 'n':
    value = input("Enter the value to be appended : ")
    random.append(value)  # append method used to append to the list
    choice = input('Do you want to append to the list?(Y/N)')

print('The list random contains : ')
print(random)  # this prints the whole list

# iterating over the list with for loop is also possible
for item in random:
    print("{0} - {1}".format(random.index(item), item))
    # here .index() is a list method which returns the index of the item
    # in the list; however it may not be the most efficient way to look up
    # the index of an item in the list incase of large lists
