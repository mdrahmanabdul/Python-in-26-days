import random
'''
THERE ARE TWO TYPES OF FUNCTIONS : 1. BUILT IN FUNCTION : len(), sorted(), min(), max()
                                 : 2. USER DEFINED FUNCTIONS

'''

def printName():
    print('Rahman')

printName() #we are calling the function, we can call it any number of times

'''
GOOD NAMING CONVENTIONS : 
1. ALWAYS USE lowercase letters
2. USE _ TO JOIN TWO WORDS : print_name()
'''

def outer_function():
    a = 20
    print('outer function')
    def inner_function():
        b=30
        print('inner function')

outer_function()
#inner_function() #gives error, we cannot directly call the inner function from outside

print(type(outer_function)) #nested function call

#NOW WE WILL DIVIDE A TASK INTO TWO PARTS 
#1 TO GENERATE A NUMBER 
#2 TO CHECK WHETHER IT IS EVEN OR NOT

def isEven(r):
    if(r%2==0):
        return True
    else:
        print('Number is  {}'.format(r))
        return False

def randomNumber_generator():
    r = random.randint(1,11)
    if isEven(r): #calling a function from a function
        return r
    else :
        return -1
    return r
print(randomNumber_generator())
    
#PARAMETERS OR ARGUMENTS
def sum(a,b,c): #here a,b,c are arguments
    return (a+b+c)

result = sum(5,5,5); #we are passing 5,5,5 as arguments
print(result)


#TYPE OF ARGUMENTS ARE CATEGORIZED INTO 4 TYPES :
#1. POSITIONAL ARGUMENTS
def details(name,age,isMale):
    name.upper() #if age was passed in place of name then .upper() will raise an error
    age+=1
    if (isMale==False):
        isMale=True
    print(name,age,isMale)
    return

details('Rahman',23,False) #here the position of the arguments is very important
#details(23,'Rahman',False) #gives error

#2. KEYWORD ARGUMENTS
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

# Using positional arguments
greet("Alice")  # Output: Hello, Alice!

# Using keyword arguments
greet(message="Hi", name="Bob")  # Output: Hi, Bob!


#3. VARIABLE LENGTH POSITIONAL ARGUMENTS
#4. VARIABLE LENGTH KEYWORD ARGUMENTS

#UNPACKING LISTS/SETS/TUPLES
def print_list(a,b,c,d,e):
    print(a,b,c,d,e)
lst = [10,20,30,40,50]
tupl = (60,70,80,90,100)
s = {1,2,3,4,5}

print_list(*lst) 
print_list(*s)
print_list(*tupl)
