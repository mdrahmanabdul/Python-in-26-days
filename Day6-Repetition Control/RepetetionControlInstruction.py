# WHILE LOOP
a=0
while a<11:
    a=a+1;
    print(a)

#WHILE ELSE LOOP
r=30;
while r>10:
    r=r-1;
    print(r)
else:
    print('r has become {}'.format(r))

#FOR LOOP
#ITERATING IN A LIST
lst = (1,2,3,4,5,6,7,8,9,10)
for i in lst:
    print(i)
    
#ITERATING THROUGH AN ARRAY OF INTEGERS
import array
my_arr = array.array("i",[99,98,97,96,95]);
for it in my_arr:
    print(it)
else:
    print("Array got printed")

#ITERATING OVER A STRING
for char in 'Rahman':
    print(char)

#RANGE
for i in range(1,10,2):
    print(i,i*i,i*i*i)
    
#BREAK AND CONTINUE
for i in range(0,100):
    if i==10:
        print(i)
        break
    else:
        continue
