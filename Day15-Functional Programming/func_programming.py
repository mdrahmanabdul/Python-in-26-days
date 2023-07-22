# HIGHER ORDER FUNCTIONS : FUNCTIONS WHICH TAKE OTHER FUNCTIONS AS PARAMETERS

# map(function,iterable)

list_1 = [1,2,3,4,5]

def cube(x):
    return x*x

cube_list = list(map(cube,list_1))
print(cube_list)

#same thing we can do without defining external functions.
#we can use lambda
cube_list_2 = list(map(lambda x:x*x,list_1))
print(cube_list_2) #returns the same output as above

#filter(condition,iterable)
def greaterThan8(x):
    return x>8
list_2 = [6,7,8,9,10]
new_list = list(filter(greaterThan8,list_2))
print(new_list) #prints 9,10 as they are only greater than 8 in the tuple

# Example -2
list_3 = ('R','A','H','3','5','M','A','N','99')
#lets separate alphabets from the above list and store them in new list alphabets
alphabets = list(filter(str.isalpha,list_3))
print(alphabets) #removes numbers from the list_3

from functools import reduce
#reduce(condition,iterable)

def summation(x,y):
    return x+y
    
list_4 = [1,2,34,4,5]

result = reduce(summation,list_4)
print(result) #prints 46

#using lambda function
result = reduce(lambda x,y : x*y,list_4)
print(result) #prints 1360






