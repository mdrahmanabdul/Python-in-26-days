# THERE ARE TWO REUSE MECHANISMS THAT ARE PRESENT IN PYTHON:
'''
1. CONTAINERSHIP (COMPOSITION)
2. INHERITANCE
'''

#1. CONTAINERSHIP : A container can contain one or more contained objects apart from other data, thereby reusing
#contained objects.
# Containership has : has-a relationship
# Example : 

class Department: 
    def set_department(self):
        self._id = input('Enter the Department ID : ')
        self._name = input('Enter the Department name : ')
    def show_department(self):
        print('Department ID is : ',self._id)
        print('Department Name is : ',self._name)
class Employee:
    def set_employee(self):
        self._eid = input('Enter employee id : ')
        self._ename = input('Enter employee name : ')
        self._dobj = Department()
        self._dobj.set_department()
    def show_employee(self):
        print('Employee ID : ',self._eid)
        print('Employee name : ',self._ename)
        self._dobj.show_department()

obj = Employee()
obj.set_employee()
obj.show_employee()

#INHERITANCE : It should be used when the two classes have a 'like-a' relationship. For example, a button
#is like a window. So button class can inherit features of an existing class called Window.

#parent class
# parent class
class Parent:
    def __init__(self):
        self._count = 0

    def display(self):
        print('count = ' + str(self._count))

    def incr(self):
        self._count += 1

# derived class
class Child(Parent):
    def __init__(self):
        super().__init__()

    def decr(self):
        self._count -= 1

c = Child()
c.incr()
c.incr()
c.incr()
c.display()
c.decr()
c.display()
c.decr()
c.display()
















