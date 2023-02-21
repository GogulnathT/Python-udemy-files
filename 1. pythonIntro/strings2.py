from tkinter import N


text = 'Ironman is a marvel superhero'

print(text)
# print(text[4])
# print(text[5:11])
# print(text[-4])

name = 'Gogulnath'
print(name[1:6:2])  # here the 2 stands for step
print(name[1:6])
print(name[:6])
print(name[3:])

print(name[-4:-2])  # using negative indexes for slicing
print(name[-4:7])   # this is the same as the above print

numbers = '0,232,226,676,349,453'
# this splice will only print the commas starting from the index 1 and every fourth char
print(numbers[1::4])
# which is a comma
