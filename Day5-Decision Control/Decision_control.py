# Assignment
a = 125

if a==125:
    print('Correct')

print('-'*50)    

if(a==125):
    print('Yes a is 125')
else:
    print('No a is not 125')
    
print('-'*50)

if(a!=125):
    print('a is not 125')
elif(a==125):
    print('Correct a is 125')
else:
    print('Loooser')
    
#LOGICAL OPERATORS -> and | or | not
s1=1; s2=2; s3=3;
if(s1==1 and s2==2):
    print('Correct')
elif(s3==3 or s1==99):
    print('s3 is 3')
else:
    print('above two statements are wrong')

a=100;b=150;
print(not(a>b))

# all and any functions which replace and & or
d=11;e=12;f=13;
res = all((d>0,e>f,f>d)) #prints false as e<f
print(res)

res = any((d>e,e>100,f==13)) #prints true as f==13 is true
print(res)

#Taking input using input()
principal = int(input('Enter principal amount '))
time = float(input('Enter time '))
roi = float(input('Enter rate of interest '))
result = (principal*time*roi)/100;
print('Simple interest : {}'.format(result));

