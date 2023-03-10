i = 0
while i < 10:
    print(i, end=' ')
    i += 1

# eg of while using directions
directions = ['north', 'south', 'east', 'west']
choice = ''

while choice not in directions:  # this condition will work as long as the choice is something not in the list
    choice = input('enter the direction : ')
print('you have chosen a valid direction')
