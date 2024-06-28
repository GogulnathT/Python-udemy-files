# module = a file containing a python code, may contain functions, classes etc
#          they are used with modular programming i.e separating program into parts

import modules 
import modules as msg # giving the module an alias 
from modules import bye # this is importing specific methods/functions from the module
from modules import * # this is dangerous as it can cause naming error

msg.hello()
bye()

# help("modules") # this built in function will provide the available modules 