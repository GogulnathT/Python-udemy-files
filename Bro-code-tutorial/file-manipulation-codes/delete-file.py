import os 
import shutil

path = r"C:\Users\7000031725\Desktop\New folder"

try:
    #os.remove(path) # delete a file
    #os.rmdir(path) # delete an empty folder
    shutil.rmtree(path) # deletes a folder/directory containing files
except FileNotFoundError:
    print("The file was not found")
except PermissionError as e:
    print(e)
except OSError as e:
    print(e)
else:
    print(path,"was deleted")