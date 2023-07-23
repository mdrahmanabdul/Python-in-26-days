'''
Overview of what we are going to learn today : 
    1. Ideal naming conventions for identifiers
    2. Calling a function and method
    3. Operator Overloading
    4. Type Conversion
'''

for _ in [10,20,30,40] : print(_)

print('_'*100)
print('NAMING CONVENTIONS\n')


'''

1. Ideal naming conventions for identifiers :
    - All the variables and functions that doen't belong to a class -> Start them with lowerCase alphabets
    - Variables that need not be used again, i.e variables that we use one time only - Use _
    - While naming a class use uppercase alphabet - ex:Employee, Person etc
    - Private : Identifiers which we want should be accessed only from within the class only in which they are declared start with two __ Ex: __name,__age,__get_errors()
    - Protected : Identifiers which we want should be accessed within the class and from the derived class should be declared using single _
    - Public : identifiers which we want should be accessed from anywhere, we have to declare them using lowerCase alphabets at the start : Ex : display(), name etc
    - Language defined special names should start and end with '__' Ex : __init__, __add__
    - Unlike Java and C++ we don't have public, private and protected so we have to follow the above conventions.
'''

#Program 
class Employee: 
    def __privateFunc(self):
        print('Private function')
    def _protectedFunc(self):
        print('Protected funtion')
    def publicFunc(self):
        print('Public function')
    
   
def display(): #function that doeesn't belong to any class (global function)
    for _ in [1,2,3,4,5]:print(_) #for temporary stored values we use _
    print('Function that doen\'t belong to any class')

e1 = Employee()
e1._Employee__privateFunc() #name mangling
e1._protectedFunc() #will raise error if called from outside the class(not recommended, but possible)
e1.publicFunc()
display()


print('_'*100)
print('OPERATOR OVERLOADING\n')


# OPERATOR OVERLOADING
'''

Operator overloading in Python refers to the ability to define custom behavior for built-in operators 
when they are applied to objects of user-defined classes. Python allows you to redefine the behavior of 
operators by providing special methods in your class. These special methods are also called magic methods
or dunder methods (short for "double underscore" methods) because they are surrounded by double underscores 
on both sides of their names.

For example, consider the + operator. When used with built-in types like integers or strings, it performs
addition. However, when used with objects of user-defined classes, you can define how the + operator behaves
for those objects.

Here's a list of some common magic methods for operator overloading:

__add__(self, other): Defines behavior for the addition operator +.
__sub__(self, other): Defines behavior for the subtraction operator -.
__mul__(self, other): Defines behavior for the multiplication operator *.
__truediv__(self, other): Defines behavior for the division operator /.
__floordiv__(self, other): Defines behavior for the floor division operator //.
__mod__(self, other): Defines behavior for the modulus operator %.
__pow__(self, other[, modulo]): Defines behavior for the exponentiation operator **.
__lt__(self, other): Defines behavior for the less-than operator <.
__le__(self, other): Defines behavior for the less-than or equal-to operator <=.
__eq__(self, other): Defines behavior for the equality operator ==.
__ne__(self, other): Defines behavior for the not-equal-to operator !=.
__gt__(self, other): Defines behavior for the greater-than operator >.
__ge__(self, other): Defines behavior for the greater-than or equal-to operator >=.
'''
# Program 
'''
Since Complex is a user-defined class, Python doesn't know how to add objects of this class. We can teach
it how to do it, by overloading the '+' operator as shown below.
'''
class Complex:
    def __init__(self,r=0.0,i=0.0):
        self.__real = r
        self.__imag = i
    def __add__(self,other):
        z=Complex()
        z.__real = self.__real + other.__real
        z.__imag = self.__imag+other.__imag
        return z
    def __sub__(self,other):
        z=Complex()
        z.__real=self.__real-other.__real
        z.__imag=self.__imag-other.__imag
        return z
    def display(self):
        print(self.__real,self.__imag)

c1 = Complex(1.1,0.2)
c2 = Complex(1.1,0.2)
c3 = c1+c2
c3.display()
'''

In Python, you can overload several operators using special magic methods (dunder methods). Here's a list of the most commonly overloaded operators:

Arithmetic Operators:

__add__(self, other): +
__sub__(self, other): -
__mul__(self, other): *
__truediv__(self, other): /
__floordiv__(self, other): //
__mod__(self, other): %
__pow__(self, other[, modulo]): **
Comparison Operators:

__lt__(self, other): <
__le__(self, other): <=
__eq__(self, other): ==
__ne__(self, other): !=
__gt__(self, other): >
__ge__(self, other): >=
Bitwise Operators:

__and__(self, other): &
__or__(self, other): |
__xor__(self, other): ^
__lshift__(self, other): <<
__rshift__(self, other): >>
Augmented Assignment Operators:

__iadd__(self, other): +=
__isub__(self, other): -=
__imul__(self, other): *=
__itruediv__(self, other): /=
__ifloordiv__(self, other): //=
__imod__(self, other): %=
__ipow__(self, other[, modulo]): **=
__iand__(self, other): &=
__ior__(self, other): |=
__ixor__(self, other): ^=
__ilshift__(self, other): <<=
__irshift__(self, other): >>=
Unary Operators:

__neg__(self): -
__pos__(self): +
__abs__(self): abs()
__invert__(self): ~
Container Operators:

__len__(self): len()
__getitem__(self, key): self[key]
__setitem__(self, key, value): self[key] = value
__delitem__(self, key): del self[key]
__iter__(self): iter()
__contains__(self, item): in
Callable Objects:

__call__(self[, args...]): Call operator ()
Context Managers (with statement):

__enter__(self): Enter a context
__exit__(self, exc_type, exc_value, traceback): Exit a context

These special methods allow you to customize the behavior of your custom objects when they interact with 
Python operators or are used in various built-in functions. By overloading these operators, you can make
your objects work seamlessly with the Python language and provide a more intuitive and expressive interface 
for users of your classes.
'''

print('_'*100)
print('OBJECT\n')


#OBJECT
'''
In python every thing is an object. This includes int, float,bool, complex, string, list, tuple, set, dictionary
function, class, method and module.

Note : When we say x=20, a nameless object of type int gets created. Address of the object is stored in x. Now
x is called as reference to the int object.
'''
#Program : 
x=108
y=108
print(f" x : {x}, y : {y}")
x=789
print(f" x : {x}, y : {y}")
# in the above program x and y are refering to the same object but changing one doesn't change the other
'''
Some objects are mutable[list] and some are immutable[string,tuple]. Also all objects have some attributes and
methods
'''

#STRUCTURE
print('_'*100)
print('STRUCTURE')


'''
- If we wish to keep dissimilar but related data together we can use structure
- In Python there is no built-in structure data type.
- But we can create that using a class that is merely a collection of attributes(not methods)
- Unlike C++ and Java, Python permits us to delete/add/modify these attributes to a class/object dynamically
'''
#Program
class Bird:
    pass
b = Bird()
 #Let us now create few attributes dynamically
b.name = 'Pigeon'
b.color = 'White'
b.animalType = 'Vertebrate'

#Modify
b.color = 'Black'

#delete
del b.animalType
'''
In the above program we havde added three attributes, modified one attribute and deleted one attribute, all
on the fly, i.e.after creation of Bird object
'''

#TYPE CONVERSION
'''
We can print the type using the type()
We can print the address using the id()
'''
print('_'*100)
print('TYPE CONVERSION\n')

a = 23
b = 'Rahman'
c = True
d = 99.45
e = [1,2,3,4,5]
f = (6,7,8,9,10)
g = {
    'name' : 'Rahman',
    'age' : 22,
    'email' : 'rehmanz1446@gmail.com'
}
h = {'a','e','i','o','u'}
i = 4+5j

print(type(a),id(a))
print(type(b),id(b))
print(type(c),id(c))
print(type(d),id(d))
print(type(e),id(e))
print(type(f),id(f))
print(type(g),id(g))
print(type(h),id(h))
print(type(i),id(i))

#Converting type of a variable
a = 100
print(f"Before type conversion : {type(a)}")
a = str(a)
print(f"After type conversion : {type(a)}")