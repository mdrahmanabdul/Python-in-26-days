'''
OVERVIEW : 
    1. ITERATORS AND ITERABLES
    2. ZIP()
    3. GENERATORS
'''

'''
WHAT ARE ITERABLES ?
 - An Object is called as iterable if it is capable of returning  its members one at a time.
   String, Tuples, List etc are iterables
 - Iterator is an object which is used to iterate over an iterable. iterable provides iterator object
 - iterators are implemented in for loops, comprehensions, generators etc.
'''
print('_'*100)
print('Iterables and Iterators\n')

#programs
for _ in [1,2,3,4,5] : print(_)

'''
WHAT IS ZIP() ?
 - zip() function typically receives multiple iterable objects and returns an iterator of tuples based on them.
'''

print('_'*100)
print('Zip() function\n')

#programs
indexes = [1,2,3,4,5]
names = ['Rahman','Bush','Sultana','Peter','John']

for it in zip(indexes,names):
    print(it[0],it[1])

#What if indexes and names are not same ?
indexes = [1,2,3,4,5]
names = ['Rahman','Bush','Sultana',]
for it in zip(indexes,names): #now as the names are not equal to indexes, only three on them get printed
    print(it[0],it[1])


#We can generate a new list/tuple/set from the iterator returned by zip()
names = ['Rahman','Bush','Sultana','Peter','John']
it = zip(indexes,names)
lst = list(it)
print(lst)

it = zip(indexes,names)
st = set(it) # it is necessary to zip again
print(st) #doesn't print in same order obviously as it is a set

it = zip(indexes,names)
tple = tuple(it) # it is necessary to zip again
print(tple)

#Values can be unzipped from the list into tuples using '*'
it = zip(indexes,names)
lst_2 = list(it)
i,n = zip(*lst_2)
print('Indexes : ',i)
print('Names : ',n)


#ITERATORS
print('_'*100)
print('ITERATORS\n')

#program
for ch in 'Abdul Rahman':
    print(ch)
'''
Here the above for loop calls __iter__() method of str/list. This method returns an iterator object.
The iterator object has a method __next__() which returns the next item in the str/list container.
After we reach the end of the list, next call to __next__() raises StopIteration exception, which tells the 
for loop to terminate.
'''
#Program :
list_3 = [10,20,30,40,50]
i = list_3.__iter__()
print(i.__next__()) #prints 10
print(i.__next__()) #prints(20)
print(i.__next__()) #prints(30)
print(i.__next__()) #prints(40)
print(i.__next__()) #prints(50)
#print(i.__next__()) #will raise StopIteration Exception

#hasattr() -> using this we can check whether an iterator contains both __iter__() and __next__()
string = 'Andrew Tate'
print(hasattr(string,'__next__')) #prints false as the string doesn't have the next attribute

list_4 = [1,23,45,67,90]
it = iter(list_4) #Creating the iterator object 'it' for the iterable 'list_4'
print(hasattr(it,'__next__'))  #prints true as it has __next__()

#GENERATORS
'''
- Generators are very efficient functions that create iterators. They use yield statement instead of return 
whenever they wish to return data from the function.
- It remembers the state of the function and the last statement it had executed when yield was executed.
- Each time next() is called, it resumes where it had left off last time.
'''

#Programs
def AdjAvg(data):
    for i in range(0,len(data)-1):
        yield(data[i]+data[i-1])/2
list_5 = [10,20,30,40,50,60]
for i in AdjAvg(list_5):
    print(i)













