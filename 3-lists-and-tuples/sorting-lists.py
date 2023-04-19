odd = [1,3,5,7,9]
even = [0,2,4,6,8,10]

even.extend(odd) #this method combines two sequences
print(even)

even.sort() #this method sorts the list
print(even)

even.sort(reverse=True) #this makes the list sort in reverse order
print(even)