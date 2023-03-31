shopping_list = ['jam', 'sauce', 'bread']

shopping_list2 = shopping_list
print(id(shopping_list))
print(id(shopping_list2))

# append is a method associated with the list object;
shopping_list.append('eggs')
# it is used using the dot notation
print(shopping_list)
print(shopping_list2)
print(id(shopping_list), id(shopping_list2))

shopping_list2 += ['butter']
print(shopping_list)
print(shopping_list2)
print(id(shopping_list), id(shopping_list2))

# lists are mutable so changing the values in the list once
# will reflect on all the variables bound to the list, here it
# is both shopping_list & shopping_list2
# so multipe names are bound to the one list

shopping_list.clear()
print(shopping_list)
print(shopping_list2)
