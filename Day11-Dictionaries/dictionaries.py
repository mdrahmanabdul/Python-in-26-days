'''
DICTIONARIES :
1.  DIFFERENT KEYS CAN CONTAIN SAME VALUES
2. KEYS MUST BE UNIQUE NOT VALUES
3. KV PAIRS ARE SEPERATED BY ','
4. IF A KV IS REPEATED TWICE THEN ONLY 1 GETS STORED
5. UNLIKE SETS WHICH USE HASHING, HERE THE ORDER IS PRESERVED
6. CAN ACCESS USING THE KEY,AS THEY ARE KEY INDEXED NOT POSITION INDEXED
7. SLICING IS NOT POSSIBLE
8. MUTABLE
9. CANNOT BE CONCATINATED +
10. CANNOT BE MERGED Z=A+B
11. CANNOT BE COMPARED USING >,< 
12. TUPLES CAN BE USED AS KEYS
13. NESTED DICTIONARIES ARE POSSIBLE
14. TWO LISTS CAN BE MERGED TO CREATE A THIRD DICTIONARY BY UNPACKING THE TWO USING **
'''

a = {} #empty dictionary
a2 = {
    'name' : 'Rahman',
    'age' : 22,
    'sex' : 'Male'    
}

print(a2) #whole dict gets printed

print(a2['name']) #prints the value corresponding to that key

# LOOPING
print('*'*125)
#iterating over kv pairs
for k,v in a2.items():
    print(k,v)

print('*'*125)

for k in a2.keys(): #bigger way
    print(k)
print('*'*125)


for k in a2:
    print(k) #shorter way
print('*'*125)


#iterating over values
for v in a2.values():
    print(v)

#iterating with indexes
for i,(k,v) in enumerate(a2.items()):
    print(i,k)

#MUTABLE properties
a2['name'] = "Salman"
print(a2)

del(a2['sex']) #delete a kv
del(a2) #delete whole dict

#BUILT IN FUNCTIONS
'''
len()
max()
min()
sorted()
sum()
any()
all()
reversed()
'''

#METHODS
a = {
    'name' : 'Rahman',
    'age' : 23,
    'Gender' : 'Male',
    'branch' : 'CSE'
}
b= {
    'study'  : 'good'
}

print(a.get('name','Absent')) #prints Rahman as it is present
b.update(a) #adds contents of a in the b
print(b) #print(A U B)

#VARIETIES 
# numbers,strings,tuples can be used as keys
c = {
    (1,2) :'Rahman',
    (3,4) : 'Salman'
}

print(c[(1,2)]) #prints Rahman

contacts ={
    'Rahman' :{'full_name':'Mohammed Abdul Rahman','phone_no':'6300481313','email' : 'rehmanz1446@gmail.com'},
    'Salman' :{'full_name':'Mohammed Salman Hyder','phone_no':'9666972407','email' : 'salmanhyder1446@gmail.com'},
}
print(contacts)

print('_'*150)
d = {**c,**contacts} #unpacking lists in a new list 'd'
print(d)





