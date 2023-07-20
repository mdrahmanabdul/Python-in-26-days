# calling the function itself(recursion) ten times until i becomes 10.

def func(i):
    if(i==10): #this is the base condition
        return
    else:
        i+=1
        print(i)
        func(i) #making the recursive call

func(0)

'''
WHEN WE HAVE TO USE RECURSION :
    1. WHEN PROBLEM CAN BE DIVIDED INTO SUB-PROBLEMS
    2. WHEN PROBLEM REQUIRES UNKNOWN NUMBER OF LOOPS
'''

def factorial(num):
    if num==1:
        return 1
    else:
        p = num*factorial(num-1)
    return p

num = int(input('Enter a number : '))
ans = factorial(num)
print('Factorial of {} is {}'.format(num,ans))

def generate(n):
    lol = [[] for i in range(n**n)]
    pos=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                t=[i,j,k]
                lol[pos]=t
                pos+=1
    return pos
print(generate(3)) #prints 27 as 27 unique combinations can be made using 3 numbers

'''
TYPES OF RECURSION
    We don't get the result until each and every function sends back the result in HEAD RECURSION. 
    Local variables have to be stored in the memory before making next recursive calls
    Too many recursive calls may raise an error (Default recursion limit : 10**4)
    setrecursionlimit() in sys module permits us to set the recursion limit
1. HEAD RECURSION :
2. TAIL RECURSION
'''

def headRec(n):
    if n==0:
        return
    else:
        headRec(n-1) #calling the recursive function first and then calling the other processes
        print(n)
headRec(5)

def tailRec(n):
    if n==11:
        return
    else:
        print(n)
        tailRec(n+1)
tailRec(1)

