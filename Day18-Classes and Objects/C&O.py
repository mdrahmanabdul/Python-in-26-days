#creating the class
class Employee:
    #setting the data
    name = "Employee_name"
    role = "Employee_role"
    company_name = "Wipro"
    
    #displaying the data
    def info(self):
        print(f"{self.name} is a {self.role} in {self.company_name}")
        #self is same as 'this' keyword in C++

#creating an object of the class
e1 = Employee()
e1.name = "Peter"
e1.role = "Software Developer"
e1.info()

#creating another instance of class
e2 = Employee()
e2.name = "Nazneen"
e2.role = "Sweeper"
e2.company_name = "GHMC"
e2.info() #objectName.methodName()

# var() and dir()
import math
a=125
s = 'Rahman'
print(vars()) #prints dict of attributes in current module
print(vars(math)) #prints dict of attributes in math module
print(dir()) #prints list of attributes in current module


#vars() and dir() can be used in classes also
class Fruit:
    count=0
    def __init__(self,name='',size=0,color=''):
        self._name = name
        self._size = size
        self._color = color
        Fruit.count+=1
    def display():
        print(Fruit.count)
print('*'*100)
f1 = Fruit('Banana',5,'Yellow')
print(vars(Fruit))
print(dir(Fruit))
print(vars(f1))
print(dir(f1))









