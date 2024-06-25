# the with open statement is used to open the file; unlike just open, here the file is closed 

try:
    with open(r"C:\Users\7000031725\OneDrive - Sony\words.txt") as file:
        print(file.read())
except FileNotFoundError as e :
    print(e)


#print(file.closed) #used to check if the file is closed or not 
