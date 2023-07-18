# SET :
'''
1. SAME AS LISTS BUT SETS DON'T CONTAIN DUPLICATE VALUES
2. SET OF TUPLES IS OK, BUT SET OF LISTS IS IMPOSSIBLE
3. NO MATTER IN WHICH ORDER YOU ENTER, IT PRINTS DEPENDING ON HASH VALUE
4. LOOPING IS NOT POSSIBLE WITH WHILE LOOP IN SETS, BECAUSE WE CAN INDEX SET AS SET[i]
5. IF WE WANT IMMUTABLE SETS THEN WE CAN USE frozenset()
6. OPERATIONS THAT WORK :
        -CONVERSION
        -ALIASING
        -CLONING
        -SEARCHING
        -IDENTITY
        -COMPARISON
        -EMPTINESS
7. WE CANNOT CONCATENATE TWO SETS USING '+'
8. WE CANNOT MERGED TWO SETS USING A = B+C
9. BUILTIN FUNCTIONS
len()
max()
min()
sorted()
sum()
any()
all()

10. SET METHODS
set.add()
.update()
.copy()
.remove()
.discard()
.clear()
'''

a = set() #a is now a set, for 1 item we have to use '()'
print(type(a))


b = {3} #set with 1 item present inside


c={'Rahman',22,'M',True} #can contain values of dissimlar type
print(c)

d= {10,10,10,10} #only one 10 gets stored
print(d)


e = {4,5,1,6,8,10}
f = {5,1,4,8,6,10}
g = {10,8,5,1,4,6}
print(e)
print(f)
print(g) #no matter in which order you save in a set, it prints in the same order which it decides by hash values

set_of_tuples = {(1,2,3),(4,5,6),(7,8,9)} #works
# set_of_lists = {[1,2,3],[4,5,6],[7,8,9]} #error

#LOOPING
for i in set_of_tuples:
    print(i)

anagrams = {'gate','late','slate'}
anagrams.add('fate') #adds one more element to the anagrams
print(anagrams)

locked_Set = frozenset({'Akram','Hafeeza','Parvez','Salman','Rahman'})
print(locked_Set)
#locked_Set.add('Sarfaraz') -> gives error

s = {1,2,3,4,5}
s.update('Rahman')
print(s)

s.remove('R')
print(s)

s.clear()
