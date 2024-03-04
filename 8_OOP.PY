# OOP IN PYTHON
# to map with real world scenarios, we started using objects in code.
# This is called object oriented programming.


# class & object in python
# class is a blueprint for creating objects

# creating classs
class Student:
    name = "Shivam Kumar"

# Creating Object (instance)
s1 = Student()
print(s1.name)

class Car:
    color = "blue"

car1 = Car()
print(car1.color)

# __init__ function
# constructor
# the self parameter is a reference to the current instance of the class, and is used to access variable that belongs to the class.
class Student:
    college_name = "ABC College"
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks
    def welcome(self):
        print("Welcome Student ", self.name)
    def get_marks(self):
        return self.marks


s1 = Student("shivam", 87)
print(s1.name)
print(s1.marks)

s2 = Student("shahi",488)
print(s1.name)
print(s2.marks)
print(s2.college_name)

# Class & instance Attributes

# class.attr
# obj.attr
s1.welcome()
print(s1.get_marks())



# create student class that take name & marks of 3 subjects as arguments in constructor. then create a method to print the avaerage 

class Student:
    def __init__ (self,name,marks):
        self.name = name
        self.marks = marks
    @staticmethod
    def hello():
        print("Hello")

    def Avg_marks(self):
        sum = 0
        for val in self.marks:
            sum+= val
        print(f"Hi, {self.name} your avg marks is {sum/3}")
    
s1 = Student("shivam", [87,48,96])
s1.Avg_marks()

# static methods
# static methods dont use the self parameter( work at class level)

# abstraction
# Hiding the implementation details of a class and only showing the essential features to the user

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started")

car1 = Car()
car1.start()

# Create account class with 2 attributes - balance & account no
# create methods for debit, credit & printing the balance

class Account:
    def __init__ (self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self,amt):
        self.balance -= amt
        print (f"{amt} is debited in your account\nCurrent Balance :-{self.get_balance()}")
    
    def credit(self,amt):
        self.balance += amt
        print (f"{amt} is credited in your account\nCurrent Balance :-{self.get_balance()}")
    
    def get_balance(self):
        return self.balance

a = Account(25000,5478658)

print(a.debit(1200))
print(a.credit(16541))

print(a.get_balance())

c= Account(265447,546545465)

c.credit(54782)
c.debit(9874)

print(c.get_balance())


# del keyword
# used to delete object properties or object itself

class Student:
    def __init__(self,name):
        self.name = name

s1=Student("Shivam")
print(s1.name)

del s1
# print(s1.name)

# private(like), attributes & methods

# conceptual implementation in python
# private attibutes & methods are meant to be used only within the class and are not accessible from outside of the class

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # __ create the object into pvt.
    
acc1= Account("12345","987654")

print(acc1.acc_no)
# print(acc1.acc_pass)

class Person:
    __name = "Anno"

    def __hello(self):
        print("Hello person")

    def welcome(self):
        self.__hello()
    

p1 = Person()

print(p1.welcome())

# inheritance 

# when one class(child/derived) derives the properties & methods of another class(parent/base)



class Car:
    @staticmethod
    def start():
        print("Car started")
    def stop():
        print("Car Stopped")

class ToyotaCar(Car):
    def __init__ (self, name):
        self.name = name

class Fortuner(ToyotaCar):
    def __init__ (self,type):
        self.type = type
        
car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Innova")

print(car1.start())

# Types of inheritance
# types
# single inheritance
# multi level inheritance 
# multiple inheritance

