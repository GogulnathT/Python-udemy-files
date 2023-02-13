splitString = "This string uses the \nbackslash character to produce new line "
print(splitString)

tabbedString = "This string uses \tbackslash for tabbing"
print(tabbedString)

# using / to omit single or double quotes
print("he said \"backslash can be used to omit '' or \"\" \" ")

# using / to omit new line in print string with triple quotes
str = """This is a \
split \
string but backslash is used to omit the \
newline"""
print(str)

# a backslash can be used to omit another backslash as well
print("C:\\Users\\Gogulnath")

# using a r(i.e raw) in print function
print(r"This print function uses a r i.e raw in front of it so / wont work")
