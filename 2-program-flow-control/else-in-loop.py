#using else with loop
nums = [1,12,32,45,60]

for i in nums :
    if i % 8 == 0 :
        #the list contains a number div by 8
        print("This list is unacceptable!")
        break
else:
    print('This list is fine !!')
#here an else is used with loop; it is a rare condition and usually it
#should be avoided; here the else block will be executed only if the
#for loop runs through all the iteration and doesnt break in-between
