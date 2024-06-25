# copyfile() = copies content of a file
# copy() = copyfile() + permission mode + destination can be a directory 
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil
# module used for copying; this is one of the methods for file copying

shutil.copyfile(r"C:\Users\7000031725\Desktop\sample-file.txt.txt",
                r"C:\Users\7000031725\Desktop\sample-file-copied.txt.txt") #src, dst
#the syntax and arguments are same for copy() and copy2()