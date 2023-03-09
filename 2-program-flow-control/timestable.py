#using nested loops to print the multiplication table
for i in range (1,13):
    for j in range(1,13):
        print('{0:^3} x {1:^3} = {2:^3}'.format(i,j,i*j))
    print('------------------------------------')