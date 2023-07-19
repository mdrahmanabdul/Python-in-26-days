
'''
1. LOOPING / ITERATING OVER ITEMS AND ASSIGNING THEM TO LIST, SET OR DICTIONARY.
2. WE CAN ASSIGN TO TUPLES AS IT IS IMMUTABLE
3. COMPREHENSIONS CONTAIN AN EXPRESSION FOLLOWED BY A FOR CLAUSE OR IF-ELSE CLAUSE OR BOTH.
4. MULTIPLE FOR LOOPS CAN BE USED
'''
import random
a = [random.randint(10,100) for n in range(20)]
print(a) #20 numbers get printed

b = [(x,x**2,x**3) for x in range(1,10)]
print(b) #prints number, square of a number and cube of a number

even_numbers = [num for num in range(10,40) if num%2==0]
print(even_numbers) #prints even numbers between 10 and 40

nums = [num for num in even_numbers if num>10 and num<20]
print(nums) #prints even numbers between 10 and 20

alphabets = ['!'if alphabets in 'aeiou' else alphabets for alphabets in 'Technical']
print(alphabets)

twoD_array = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
flattened_arr = [*twoD_array[0],*twoD_array[1],*twoD_array[2]]
print(flattened_arr)

#set comprehension
squares = {number**2 for number in range(10)} #will not store in order because it is not indexed using position. It is indexed using hash values
print(squares) #prints squares of number in the range of 0 to 10

unique_combinations_of_123 = [(i,j,k) for i in [1,2,3] for j in [1,2,3] for k in [1,2,3] if i!=j and j!=k and k!=i]
print(unique_combinations_of_123) #prints all the unique combinations of 1,2,3

#dictionary comprehension
d ={
    'a':1,
    'b':2,
    'c':3,
    'd':4
}
d1 = {k:v**3 for (k,v) in d.items()} #cubes all the values for a key k in the dictionary
print(d1)