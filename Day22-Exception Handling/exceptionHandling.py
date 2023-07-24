'''
Types of errors : 
    1. Systax Errors : 
        - Something in the program is not according to the language grammer
        - It is reported by Interpreter/Compiler
        - We have to rectify the program
    2. Exceptions :
        - Something unforeseen has happened
        - reported by the Python Runtime
        - We have to Tackle them on the file
'''

#Program : Syntax Error
a = 10
b =20
# sum = a+b+d -> This will raise the following error
'''
StackTrace : 
Traceback (most recent call last):
  File "/home/main.py", line 16, in <module>
    sum = a+b+d
NameError: name 'd' is not defined. Did you mean: 'id'?
'''

#Program : Exception/Runtime Error
a = 100
b = 0
#result = a/b -> This will raise ZeroDivisionError
'''
StackTrace : 
Traceback (most recent call last):
  File "/home/main.py", line 27, in <module>
    result = a/b
ZeroDivisionError: division by zero

Other Examples are : 

1. `BaseException`: The base class for all built-in exceptions.

2. `Exception`: The most common base class for all non-exit exceptions.

3. `StopIteration`: Raised when the `next()` method of an iterator does not point to any object.

4. `GeneratorExit`: Raised when a generator is closed.

5. `SystemExit`: Raised when the `sys.exit()` function is called.

6. `KeyboardInterrupt`: Raised when the user presses Ctrl+C (or other interrupt key).

7. `ImportError`: Raised when an import statement fails.

8. `ModuleNotFoundError`: A subclass of `ImportError`, raised when a module is not found.

9. `IndexError`: Raised when a sequence subscript is out of range.

10. `KeyError`: Raised when a dictionary key is not found.

11. `NameError`: Raised when a variable or name is not found in the local or global scope.

12. `AttributeError`: Raised when an attribute reference or assignment fails.

13. `TypeError`: Raised when an operation or function is applied to an object of inappropriate type.

14. `ValueError`: Raised when an operation or function receives an argument of the right type but an inappropriate value.

15. `RuntimeError`: Raised when an error occurs that doesn't belong to any specific category.

16. `AssertionError`: Raised when an `assert` statement fails.

17. `ZeroDivisionError`: Raised when division or modulo by zero is performed.

18. `FileNotFoundError`: Raised when a file or directory is requested, but it cannot be found.

19. `PermissionError`: Raised when trying to access a resource without sufficient permissions.

20. `IOError`: Raised when an I/O operation (e.g., reading or writing to a file) fails.

21. `NotImplementedError`: Raised when an abstract method that should be overridden in a subclass is not actually overridden.

22. `OverflowError`: Raised when the result of an arithmetic operation is too large to be expressed.

23. `FloatingPointError`: Raised when a floating-point operation fails.

24. `IndentationError`: Raised when there's a problem with indentation.

25. `TabError`: Raised when indentation contains tabs and spaces.

26. `SyntaxError`: Raised when there's a syntax error in the code.

27. `SystemError`: Raised when an internal error in the Python interpreter is detected.

'''

#Dealing with Exceptions using simple Try and catch block
print('_'*100); print('Try and Catch block\n')

try : 
    a = 10
    b = 0
    c = a/b #Here the control stops and jumps to the except block
    print('Result is {}'.format(c))
except ZeroDivisionError :
    print('Please choose Denominator other than 0')
    
'''
Try Block :
 - Nested try blocks are possible 
 - If the exception raised doesn't match with its except block, then it starts searching for others except block.
Except Block : 
 - Order is important : Derived first, base last
 - empty except block is like catchall - It catches all the exceptions
 - exception can be re-raised from any except block
'''

#If you are not confident about which exception may raise, you can pass a tuple of exceptions to the except block


try :
    s = 'Rahman'
    a = 100
    i_to_str = int(s) #will raise ValueError
except(NameError,TypeError,ZeroDivisionError,ValueError):
    print('Cannot convert string to integer')


#Other way is :
try : 
    a = 10
    b = 0
    c = a/b
except ZeroDivisionError:
    print('Please choose valid Denominator')
except ValueError:
    print('Cannot convert string to integer')


'''USER DEFINED EXCEPTIONS''' 
print('_'*100); print('USER DEFINED EXCEPTIONS\n')

class UserDefinedException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# Now, CustomError is a user-defined exception.

def divide(x, y):
    if y == 11:
        raise UserDefinedException("The number 11 is on holiday, So please choose another number.")
    return x / y

try:
    result = divide(121, 11)
except UserDefinedException as ude:
    print(ude.message)

#FINALLY BLOCK
print('_'*100); print('FINALLY BLOCK\n')

'''
- It is optional block
- It always runs no matter what happens in the try catch block
- It is placed after all the except blocks
- Try block must contain either the except block or finally block
- this block is commonly used for releasing external resources like files, network connections or database
  connections, irrespective of whether the use of the resources was successful or not.
'''

#program
try :
    a = []
    a.append(12)
    a.append(13)
    a.append('Rahman')
except :
    print('Some exception has been raised')
finally :
    del a
    print('Thank you !')
    print('Please drop a star for this repo')
    print('All the best')
    







