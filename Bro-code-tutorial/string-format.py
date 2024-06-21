# str.format() = optional string method that gives users
#                more control when displaying output

animal = "Lion"
place = "Africa"

print("The {} lives in the {}".format(animal,place))
print("The {1} lives in the {0}".format(animal,place)) #postional argument
print("The {animal1} lives in the {place1}".format(animal1 = "Elephant",place1 = "Asia")) #keyword argument

name = "Tgn"

print("Hello {:10}, have a great day!".format(name)) #default padding is left aligned
print("Hello {:<10}, have a great day!".format(name)) #left
print("Hello {:>10}, have a great day!".format(name)) #right
print("Hello {:^10}, have a great day!".format(name)) #center

pi = 3.14159
number = 10000

print("The value of pi is {0:.2f}".format(pi)) #decimal formatting 
print("The value of num is {:,}".format(number)) #adding commas to value
print("The value of num is {:b}".format(number)) #binary
print("The value of num is {:e}".format(number)) #scientific
print("The value of num is {:o}".format(number)) #octal
print("The value of num is {:x}".format(number)) #hexadecimal