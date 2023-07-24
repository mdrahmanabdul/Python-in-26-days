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
