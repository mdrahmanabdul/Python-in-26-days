#lets write and some data from a file
msg1 = 'Rahman is a good coder'
msg2 = 'But he knows only C++'
msg3 = 'But he is now trying to learn Python and Data science'
msg4 = 'First message was a joke :D'

f = open('messages.txt','w') #opening a file
f.write(msg1) #putting data into the file
f.write(msg2)
f.write(msg3)
f.write(msg4)
f.close() #closing the file by vacating the buffer

f = open('messages.txt','r') #opening a file
data = f.read() #reads all the lines present in the file represented by object f into data
print(data)
f.close() #Once the file is closed read/write operation on it are not feasible

#There are two functions that can write data onto the file
f = open('random.txt','w')
msg5 = 'Keep smiling....'
msg6 = 'Good things take time'

f.write(msg5) # -> first way
f.writelines(msg6) # -> second way

# There are four functions for reading data from a file by file object f
'''
data = f.read() #to read entire file content and return a string. If eof is reached then it returns an empty string
data = f.read(3) #to read first 3 characters and return as string
data = f.readline() #to read a line and return as a string
data = f.readlines() #To read all the lines in a file and form a list of lines.

'''

# File opening modes 
'''
'r' - Opens file for reading in text mode
'w' - Opens file for writing in text mode
'a' - Opens file for appending in text mode
'r+' - Opens file for reading and writing in text mode
'w+' - Opens file for writing and reading in text mode
'a+' - Opens file for appending and reading in text mode
'rb' - Opens file for reading in binary mode
'wb' - Opens file for writing in binary mode
'ab' - Opens file for appending in text mode
'rb+' - Opens file for reading and writing in text mode
'wb+' - Opens file for writing and reading in text mode
'ab+' - Opens file for appending and reading in text mode
'''

#Note : While opening a file for writing, if the file is already present then it is overwritten.

#WITH KEYWORD
'''
 - It is always a good practice to close the file once it has been used.
 - It will free up the system resources
 - If you don't close the file then file object will be destroyed and file will be closed by Python's Garbage collection program.
 - If we use the 'with' keyword while opening the file, the file gets closed as soon as it's usage is over.
'''

#program :
with open('messages.txt','r') as f:
    data = f.read()
    print(data)

#MOVING WITHIN THE FILE
'''
- When we are reading a file or writing a file, the next read or write operation is performed from the next
  character/byte as compared to the previous read/write operation
- For example : If we read the first character from a file using f.read(1), next call to f.read(1) will 
  automatically read the second character in the file.
- To move to the desired location we can use the f.seek method
- Syntax : f.seek(offset,reference)

#REFERENCE VALUE :
0 = begening of the file
1 = Current position
2 = End of the file
'''
# f.seek(512,0) -> moves to position 512 from beginning of the file
#f.seek(0,2) -> moves to end of the file

#SERIALIZATION AND DESERIALIZATION
'''
- Compared to strings, reading/writing numbers from/to a file is tedious
- write() writes string to the file and read() returns a string read from a file.
- So, we need to perform conversions while read/write.
'''

#Program
f = open('Numbers.txt','w+')
f.write(str(6300481313)+'\n') #converting the number to a string and then writing to the file
f.write(str(13.45)) #converting the float to a string and writing to the file.
f.seek(0) #moving to the beginning of the file
a = int(f.readline()) #converting to int and storing in 'a'
b = float(f.readline()) #converting to float and storing in 'a'
print(a+a)
print(b+b)

'''
- If we need to read/write more complicated data in the form of tuple, dictionaries etc from/to a file
  it becomes even more difficult.
- We can use .json to do this task.
- json module converts the Python data into appropriate JSON types before writing data to a file. Likewise
  it converts JSON types read from a file into Python data. 
  Converting python data -> JSON types = Serialization
  Converting JSON types -> Python data = Deserialization
'''
#Program : Let's serialize and Deserialize a list
#same thing we can for dict and tuples also.
import json
f = open('Serialization.txt','w+') #opening the file for write and read operations
lst = [10,20,30,40,50,60,70,80,90,100]
json.dump(lst,f) 
f.seek(0)
inlst = json.load(f)
print(inlst)
f.close()

#FILE AND DIRECTORY OPERATIONS
import os 
import shutil
print(f"OS : {os.name}") #prints 'posix'
print(os.getcwd())
print(os.listdir('.')) #prints the current directory
print(os.listdir('..')) #prints the parent of current directory





#NOTE : Serialization of User defined type is skipped because it is rarely used.




