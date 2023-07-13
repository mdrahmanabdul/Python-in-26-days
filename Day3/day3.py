import keyword
print(keyword.kwlist)

print(type(99))
print(type(99.9))
print(type(99+4j))

is_python_good = True
print(type(is_python_good))

print(type('ninety nine'))

#prints a raised to the power of 4
print(3**4)

#perform floor division
print(10//3)

#ASSOCIATIVITY AND PRECEDENCE FOLLOWS (PEMDAS)
# Parenthesis>>exponentiation>>multiplication>>addition>>subtraction

#CONVERSIONS
x = 99.9
x_Converted_to_Int = int(x)
print(x_Converted_to_Int)
print(type(x_Converted_to_Int))
# Int the sameway float() | complex() | bool() will work

#BUILT IN FUNCTIONS
y=2;n=1;

abs(x)
pow(x,2)
min(1,2,5,99,0.1)
max(1,2,5,99,0.1)
divmod(x,2)
#round(x,[0,n])
#bin(x)
#oct(x)
#hex(x)

#BUILT IN MODULES : math, cmath, random, decimal
import math

print(math.pi)
print(math.sqrt(4))
print(math.factorial(6))
print(math.fabs(4.567))
print(math.log(5))
print(math.exp(3))
print(math.trunc(89.21))
print(math.ceil(99))
print(math.modf(56.78))

#math also has trignometic functions like degrees(), radians(), sin(),.....hypot(x,y), asin(x)

# Methods from Random Module
import random
print(random.random()) #prints random values between 0 and 1
print(random.randint(1,6)) #prints random integer between 1 and 6

random.seed(42)
print(random.randint(1,100))

random.seed()
print(random.randint(1,100)) #sets current time as seed for random number generation logic

print(dir(__builtins__))

#PYTHON TYPE JARGON
'''

1. Collection
2.Iterable
3.Ordered Collection
4.Unordered Collection
5.Sequence
6.Immutable
7.Mutable

'''

#Multilining
total_marks = 13 + 14 + 15 + 56 + \
56 + 100
print(total_marks)

