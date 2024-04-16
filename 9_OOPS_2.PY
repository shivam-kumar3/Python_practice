# DEL keyword
'''
Used to delete object properties or object itself
del s1.name
del s1
'''


class Student:
    def __init__(self,name):
        self.name =name

s1= Student("shivam")
print(s1.name)
del s1

# print(s1.name)
'''
PRIVATE (LIKE) ATTRIBUTES & METHODS 
CONCEPTUAL IMPLEMENTATION IN PYTHON
PRIVATE ATTRIBUTES & METHODS ARE MEANT TO BE USED ONLY WITHIN THE CLASS AND ARE NOT ACCESSIBLE FROM OUTSIDE THE CLASS

if we make any any method private that can be only use by the internal methods only 

'''

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # adding 2 underscore before the name will turn it into private attribute

    def reset_pass(self):
        print(self.__acc_pass)

acc= Account("12345", "zaysd")

print(acc.reset_pass())

class Person():
    __name = "Shivam"

    def __hello(self):
        print("Hello user")
    
    def welcome(self): # user can call this method but not the __hello method
        self.__hello()
    
s1= Person()
print(s1.welcome())

'''
INHERITANCE 
When one class (child/derived) derives the properties & methods of another class(parents/base)

'''


class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class Toyota(Car):
    def __init__ (self, name):
        self.name = name

car1 = Toyota("Fortuner")
car2 = Toyota("Prius")

print(car1.start())
print(car1.color)

'''
TYPES OF INHERITANCE 
- SINGLE INHERITANCE
- MULTILEVEL INHERITANCE 
- MULTIPLE INHERITANCE 
'''

class fortuner(Toyota):
    def __init__ (self,type):
        self.type = type

car1 = fortuner("Diesel")
print(car1.stop())


class A:
    varA = "Welcome to class A"

class B:
    VarB = "Welcome to class B"


