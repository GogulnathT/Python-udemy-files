import time

print(time.ctime(0)) # convert a time expressed in seconds(0 here) since epoch to a readable string
                     # epoch = beginning of time for the reference of a computer

print(time.time())  # return current seconds since epoch

print(time.ctime(time.time()))

time_object = time.localtime() # this is a time object
print(time_object)

# this converts time object into readable format based on the format we send; refer docs for
# a list of all the available formats
local_time = time.strftime('%B %d %Y %H : %M : %S',time_object) #month date year hour min sec
print(local_time)

print("UTC time : ",time.gmtime()) # prints utc time

time_string = "20 April, 2023"
# converts string representing time into time object
time_object = time.strptime(time_string,"%d %B, %Y")
print(time_object)

# (year, month, day, hours, mins, secs, day of the week, day of the year, dst)
time_tuple = (2024, 4, 20, 4, 20, 0, 0, 0, 0)
time_string1 = time.asctime(time_tuple) # converts a tuple representing time in a format to string
# showing time
print(time_string1)