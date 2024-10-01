# if __name__ == '__main__' --> this is used to check if a module is run directly or indirectly
#
# python has special variables one of which is __name__
# Python will assign the __name__ a value of "__main__" if it is the main module being run or else
# it will be assigned the name of the module if run indirectly(imported and run elsewhere)

# in python modules are programs that can be run on their own or can be imported to other modules
import math

print(__name__)
print(math.__name__) # this will display the module name