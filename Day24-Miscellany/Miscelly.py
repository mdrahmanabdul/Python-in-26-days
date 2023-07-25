# DOCUMENTATION STRINGS
'''
- It is a good idea to mention a documentation string(often called docstring) below a module, function, class
  or a method definition. It should be the first line below that def and class statement.
- docstring is available in the attribure __doc__ of the module, function, class or method. 
- We can use the help() method to print the functions/class/method documentation systematically
'''

def capitalLetters(msg):
    '''It will display a message in capital letters'''
    print(msg.upper())

def lowerLetter(msg1='',msg2=''):
    '''It will display a message in lower letters
    
    Arguments :
    msg1 -- message that will get displayed in lowercase(default '')
    msg2 -- message that will get displayed in uppercase(default '')
    '''
    print(msg1.lower())
    print(msg2.upper())

capitalLetters('rahman is a good coder')
lowerLetter('UniterStates','Australia')
#help(lowerLetter) #It will print the documentation of lowerLetters function
#help(capitalLetters) #It will print the documentation of capitalLetters function

# COMMAND LINE ARGUMENTS
import sys
print('Number of arguments received = ',len(sys.argv))
print('Arguments received = ',str(sys.argv)) #prints the path of the file from where arguments were received

# COPYING CONTENTS OF A FILE TO ANOTHER
import shutil
def copy_file(source_file, destination_file):
    try:
        # Copy the file from source to destination
        shutil.copy(source_file, destination_file)
        print("File copied successfully!")
    except FileNotFoundError:
        print("Source file not found.")
    except shutil.SameFileError:
        print("Source and destination are the same file.")
    except PermissionError:
        print("Permission denied. Unable to copy the file.")
    except Exception as e:
        print("An error occurred:", str(e))

source_file_path = "/Users/rahman/Desktop/Python/RandomFiles/source.txt"
destination_file_path = "/Users/rahman/Desktop/Python/RandomFiles/target.txt"
#copy_file(source_file_path, destination_file_path)


#BITWISE OPERATORS
'''
In Python, bitwise operators are used to perform operations at the bit level, i.e., on individual bits of binary representations of numbers. These operators are useful when working with low-level data manipulation, bitwise flags, and optimizations.

Python provides the following bitwise operators:

Bitwise AND (&): Performs a bitwise AND operation on each bit of the two operands. T
                 he result will have a 1 only if both corresponding bits are 1.

Bitwise OR (|): Performs a bitwise OR operation on each bit of the two operands. 
                The result will have a 1 if either of the corresponding bits is 1.

Bitwise XOR (^): Performs a bitwise XOR (exclusive OR) operation on each bit of the two operands. 
                 The result will have a 1 if the corresponding bits are different.

Bitwise NOT (~): Performs a bitwise NOT operation on each bit of the operand.
                 It changes 1 to 0 and 0 to 1.

Left Shift (<<): Shifts the bits of the first operand left by the number of positions specified by 
                 the second operand. Zeros are filled in from the right.

Right Shift (>>): Shifts the bits of the first operand right by the number of positions specified by 
                  the second operand. Zeros are filled in from the left for unsigned numbers, and the 
                  sign bit is filled in for signed numbers.
'''
# Bitwise AND
a = 10    # binary: 1010
b = 7     # binary: 0111
result_and = a & b   # binary: 0010 (decimal: 2)
print("Bitwise AND:", result_and)

# Bitwise OR
a = 10    # binary: 1010
b = 7     # binary: 0111
result_or = a | b    # binary: 1111 (decimal: 15)
print("Bitwise OR:", result_or)

# Bitwise XOR
a = 10    # binary: 1010
b = 7     # binary: 0111
result_xor = a ^ b   # binary: 1101 (decimal: 13)
print("Bitwise XOR:", result_xor)

# Bitwise NOT
a = 10    # binary: 1010
result_not = ~a      # binary: -1011 (decimal: -11) [Two's complement representation]
print("Bitwise NOT:", result_not)

# Left Shift
a = 5     # binary: 0101
shifted_left = a << 2   # binary: 010100 (decimal: 20)
print("Left Shift:", shifted_left)

# Right Shift
a = 16    # binary: 10000
shifted_right = a >> 2  # binary: 0001 (decimal: 1)
print("Right Shift:", shifted_right)

#ASSERTIONS
'''
- An assertions allows you to express programatically our assumption about the data at a particular point
  in the execution.
- Assertion performs runtime checks of assumptions.
- Assert statements are very much useful when debugging a program as it halts the program at the point where
  an error occurs. This makes sense as there is no point in continueing the execution if the assumption is no
  longer true.
'''

#PROGRAM without Assertion
num_list = [1,2,3,4,5]
#avg = sum(num_list)/len(num_list) #as we deviding by zero it raised an error and terminates the program
#print(f"avg : {avg}")

#PROGRAM WITH ASSERTION
assert len(num_list) != 0, 'Check denominator, it is zero'
avg = sum(num_list)/len(num_list)

#DECORATORS : 
'''
- Decorators are nothing but functions which take another function as input and modify the function
- Very useful when we want to change the behaviour of large number of functions.
- There are many decorators that are present in Python : @abstractmethod @property @classmethod @staticmethod 
'''

#program :
def greet_the_user(function):
    def modification():
        print("Welcome to SBI")
        function()
        print("Thankyou for using our services")
    return modification

@greet_the_user #We are adding decorator to the 'starter' function
def starter():
    amount = int(input('Enter the amount you want to deposit : '))

starter()

#BYTES Datatype
'''
- Python text is always represented in Unicode characters and is represented by 'str' type.
- Binary data is represented by byte type
- We can create bytes literal using prefix b.
'''
#Program
print(type(b'\xe0\xa4\x85')) #will print bytes