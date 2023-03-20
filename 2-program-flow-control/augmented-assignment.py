#augmented assignment is when an assignment operator and binary operator are on the same expression
#eg a = a + 1, its augmented form is a += 1
#augmented assignment is considered efficient(in python) as the variable is being called only once

a = 99

a += 12
print(a)

a *= 34
print(a)

a//=10
print(a)

#augmented assignment can be used for strings as well
str1 = 'Hello'

str1+=' World!!!'
print(str1)
str2 = 'Python'
str1+=str2
print(str1)