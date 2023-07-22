# SYMBOL TABLE
'''
1. While interpreting our python program, python interpreter creates a symbol table
2. In that symbol table it stores information about each and every identifier
3. The information includes type of the identifier, scope and location in the memory
4. This information enables the interpreter to decide whether the operations of a developer are permissable or not.
5. For example if we are trying to change the values in the tuple using indexing, then the interpreter will not allow us to do that
'''

#NAMESPACES
'''
Two types : 
    1. Local Namespace : An identifier which belongs to an function or method
    2. Global Namespace : An identifier used outside a function belongs to global Namespace
'''
# We can change the local Namespace to global Namespace using global keyword
#Example :
def fun():
    global b
    b='Rahman'
fun()
print(b) #prints Rahman even it belongs to function


global a;
a=45
def some_func():
    b='rahman'
    print(globals()['a']) #returns a dictionary of local identifiers that are accessible from that function or method
    print(locals()['b'])  #returns a dictionary of global identifiers that are accessible from that function or method

some_func()