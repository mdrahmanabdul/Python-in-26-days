'''
# WHY TUPLES?
 Though list can store dissimilar data it is commmonly used to store similar data
 Though tuples can store similar data it is most commonly used to store dissimilar data
'''

a = () # -> empty tuple
b = (33,) #-> tuple with one item, if ',' is not included it will be treated as int
print(type(b))

c = ('Rahman',23,'M',True) #tuple with dissimilar data type
print('Items in the tuple c : {}\n Data type : {}'.format(c,type(c)))

d = (1,2,3,4) #tuple with similar data types
print(type(d))

e = (3,)*10 # stores 3 ten times
print(e)

f = (50)*5 #because there is no ',' this will be treated as int not tuple
print(f)
print(type(f))

'''
ACCESSING TUPLE ELEMENT
-> Can print the whole tuple directly by print(tuple_name)
-> Can access by index directly tuple_name[index]
-> Can be sliced tuple_name[0:3]
'''

sample = (1,2,3,4,'rahman')
print(sample)
print(sample[4])
print(sample[0:3])

'''
LOOPING THROUGH THE  TUPLE
-> For loop
-> while loop
'''

for i in sample:
    print(i)

for index,i in enumerate(sample):
    print(index,i)

index=0
while(index<len(sample)):
    print(sample[index])
    index+=1

'''
BASIC OPERATIONS 
-> TUPLES are immutable so you cannot change the values 
    sample[0]=99 -> gives error
-> APPEND, REMOVE, INSERT don't work in tuples
-> if TUPLE contains a list, the list can be modified since it is not immutable
'''

sample_2 = ([1,2,3,4],'Rahman',23)
print(sample_2)
sample_2[0][0] = 'Mohammed' #modifying the list which is inside the tuple
print(sample_2)

'''
Same as LISTS built in functions are present in TUPLE
len()
max()
min()
sum()
any()
all()
sorted()
reversed()
'''

'''
METHODS 
count()
index()
'''

'''
VARIETIES IN TUPLES :
-> Tuple of tuples can be created
-> Tuple can be embedded in another tuple
-> Tuple can be unpacked in another tuple
-> LIST of tuple or tuple of lists can be created and we can sort them too
'''
tuple_of_tuples = (("apple", 1), ("banana", 2), ("orange", 3))
embedded_tuple = (1, (2, 3), 4)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = (tuple1, *tuple2)  # Unpacking tuple2 within combined_tuple
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

list_of_tuples = [("apple", 3), ("banana", 2), ("orange", 1)]
list_of_tuples.sort(key=lambda x: x[1])  # Sort based on the second element of each tuple
print(list_of_tuples)  # Output: [("orange", 1), ("banana", 2), ("apple", 3)]

tuple_of_lists = ([1, 2, 3], [4, 5, 6], [7, 8, 9])

from operator import itemgetter
fruits = [("apple", 3), ("banana", 2), ("orange", 1)]
sorted_fruits = sorted(fruits, key=itemgetter(1))
print(sorted_fruits)
# Output: [("orange", 1), ("banana", 2), ("apple", 3)]
