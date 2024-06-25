import os 
#this module is used for file handling related tasks

path = r"C:\Users\7000031725\Desktop\sample-file.txt.txt" # r is added to make it raw string to include '\'

if os.path.exists(path):
    print("The location exists !")
    if os.path.isfile(path):
        print("It is a file")
    elif os.path.isdir(path):
        print("That is a folder")
else:
    print("The location does not exist")