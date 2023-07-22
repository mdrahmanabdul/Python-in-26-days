import functions #importing the functions module that we have created [functions.py] 
                 #it is a user defined module
#we can import multiple modules in moduler_programming.py module
import math
import random

#we can import multiple modules in this way also 
import math,random

#we can import only required functions of a module also
from math import sin,cos,tan 
from random import randint 
from functions import * #to import all the functions we can use '*'


functions.print_details('Rahman',23,'6300481313','rehmanz1446@gmail.com')

print(math.sin(0.5)) #we are using the math module here
print(random.randint(0,10)) # we are making use of the random modules

print(__name__)



# SEARCH SEQUENCE
'''
Let's suppose we are imporing a module called 'my_funs'
    import my_funcs

1. Interpreter first searches for a built-in module called 'my_funcs'
2. if found : 
        uses the built-in module
    else:
        it will start searching directory list given by the variable sys.path
'''

import sys
for p in sys.path:
    print(p) #prints list of directories in sys.path
    
def main():
    print('Main program')
    
if __name__ == '__main__':
    main() #will run only if it is in the main module.
           #we cannot run this function in other modules by simply importing its .py file.

#Like we use folders to organise our files in our OS
#we can do the same using packages
#Here pakage.file_name lets us import everything from the directory

import pkg.my_funcs as f
f.func1()
f.func2()












