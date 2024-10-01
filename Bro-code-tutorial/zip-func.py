# zip(*iterables) = aggregate elements from two or more iterables(lists, tuples, dicts)
#                   creates a zip object with paired elements stored in tuples for each element
# note zip object is an iterator like map and filter meaning it will be exhausted after going through
# a loop once

usernames = ["Dude","sigma","punk"] # list
passwords = ("Pw123","Erm897","cybertruck") # tuple

users = zip(usernames, passwords) # users is a zip object
users = dict(users) # casting it into dict

for key,value in users.items():
    print(key, value)

login_dates = ["1",'4','15']
users2 = list(zip(usernames,passwords,login_dates))
print(users2)




