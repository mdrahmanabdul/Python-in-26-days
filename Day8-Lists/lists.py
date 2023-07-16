nums = [1,2,3,4,5]
print(nums)
print('-'*100)

dis_similar = ['Rahman',22,True,70.2]
print(dis_similar)
print('-'*100)


same_data = [10]*5
print(same_data)
print('-'*100)

# ACCESSING
print(nums)

print(nums[0])

print(nums[0:4])
print('-'*100)


#LOOPING
print('USING FOR LOOP')
animals = ['tiger','lion','crocodile','zebra','cat','dog']
for i in animals:
    print(i)
print('-'*100)

i=0
print('USING WHILE LOOP')
while(i<len(animals)):
    print(animals[i])
    i+=1

'''
PROPERTIES :
    1. MUTABLE
    2. CAN CONCATINATE
    3. MERGABLE
    4. CONVERTIBLE FROM OTHER
    5. ALIAS
    6. CLONING
    7. SEARCHING
    8. IDENTITY
    9. COMPARISON
    10. EMPTINESS
'''

prop_check = [10,20,30,40,50]
#1
prop_check[0] = 'Rahman'
#2
prop_check = prop_check + [60,70,80]
#3
random_list = [100,110,120]
merged_list = prop_check + random_list
#4
chars = list("Rahman")
#5
list_1 = [1,2,3,4,5]
list_2 = list_1 #referred
#6
#cloning / deep copy
list_3 = []
list_3 = list_3+list_1
#7
f = ['A','H','P','S','R']
print('R' in f)
#8
print(list_1 is list_2)
#9
a = [1,2,3,4]
b = [1,2,5]
print(a<b)
#10
full_list =[]
if not full_list:
    print('Empty list')


# BUILT IN FUNCTIONS 
len(list_1)
max(list_1)
min(list_1)
sum(a)
del(a[0])
f.sort(reverse=False)
f.reverse()

#METHODS 
list_1.append(99)
list_1.remove(99)
list_1.pop()
list_1.insert(99,0)
list_1.count(99)
list_1.index(4)

# LIST OF LISTS / 2D LISTS
two_d = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(two_d)