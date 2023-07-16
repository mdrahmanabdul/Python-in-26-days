# input()
name = input('Enter your name : ')
#print(name)

# .split()
firstName,middleName,lastName = input('Enter your name : ').split()
print(firstName)
print(middleName)
print(lastName)

details = input('Enter name,age,sex').split()
name = details[0]
age = details[1]
sex = details[2]

#OUTPUT 
print(name,age,sex,sep=',',end='!')

#FORMAT
print('\nName : {}\n Age : {}\n Sex : {}'.format(name,age,sex))

