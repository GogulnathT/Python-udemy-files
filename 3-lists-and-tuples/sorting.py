#the sorted() built in function can be used to sort any iterable function
pangram = "The quick brown fox jumps over the lazy fox"
letters = sorted(pangram)
print(letters) #this will print the sorted list as per the alphabetical order

numbers = [2,1,0,2.3,5.5,6.7,1002,22,390,2908.45]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)
#unlike the sort method of iterables, the sorted() function creates a new list
#while sorting the list, so the sorted values are placed in new list

#iterables can also be directly passed to the sorted function
sorted_alphabets = sorted('Greatest of all time')
print(sorted_alphabets)