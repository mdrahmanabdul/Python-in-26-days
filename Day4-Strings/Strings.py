
# We can use any of the below to declare and initialize strings
str0 = 'Rahman'
str1 = '''Rahman'''
str2 = "Rahman"
str3 = """Rahman"""

# If we want to include the ' or "" in between a string we can do that by using \
str = 'Rahman said that \'HE IS GOING TO USA\''
print(str)

# Accessing the string elements
# -5 -4 -3 -2 -1
#  A  B  C  D  E
#  0  1  2  3  4
str = "ABCDEF"
print(str[0])
print(str[1])

# Substrings
sub_str = str[0:4]
print(sub_str)
print('Substring : '+str[-6:])

#Properties 

#1. We cannot mutate a string 
#str[0]= 'R' #gives error -> TypeError: 'str' object does not support item assignment

#2. We can concat them
big_string = str + sub_str;
print(big_string)

#3. String can be replicated while printing
print('_'*10)

#4. Check for presence of a character/substring in a string
print('ahm' in 'Rahman')

# BUILT IN functions
msg = 'Wise man said that peace comes with lot of goodbyes'
print(len(msg))
print(type(msg))
print(id(msg))
print(msg.upper())

#Content test functions
numeric_str = '456'
alpha_str = 'Rahman'
alphaNumeric_str = 'Rahman23'

print(alpha_str.isalpha())
print(numeric_str.isdigit())
print(alphaNumeric_str.isalnum())
print(alpha_str.isdigit())

# Search and replace
print(str.find('a',0,5))
sentence = 'Good boy hates procrastination'
index = sentence.find("boy")
print(index)

sentence = sentence.replace("boy","girl")
print(sentence)

# Trimming
str = "   Rahman    is a    alpha man"
str = str.lstrip()
print(str)

str = "Salman is a beta man       "
str = str.rstrip()
print(str)

str = "    Hafeeza      is a     wonder woman         "
str = str.strip()
print(str)

str = "Rahman,23"
left,right = str.split(',')
print(left+"  "+right)

sentence = "I love apples and sun"
parts = sentence.partition("and")
print(parts)

print("--".join(sentence))

#String conversions
str_x = 'akramuddin is a great man'
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.title())
print(str.swapcase())

#Type conversions
a = 235
#string_a = str(a)
#print(string_a) As we have used the 'str' as an identifier earlier it will give an error
# NOTE =  Try commenting out the remaining code to see the output of this function

str_x = "6300"
int_str = int(str_x)
print(type(int_str))

float_x = float(str_x)
print(type(float_x))

print(chr(65))
print(ord('A'))

#String comparisons
s1 = "Rahman"
s2 = "Salman"
s3 = "Bombay"
s4 = "bombay"
s5 = "Bombay"

print(s1==s2)
print(s3==s5)

print(len(s1)) #Length of the string
print(max(s1)) #Biggest character of the string


