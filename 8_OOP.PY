# OOP IN PYTHON
# to map with real world scenarios, we started using objects in code.
# This is called object oriented programming.


# class & object in python

# __init__ (constructor) 
# all classes have a function caleed __init__(), which is alwways executed when the object is being initiated 

# creating class
'''
class Student:
    def __init__ (self,fullname):
    self.name = fullname
'''
# creating object 
'''
s1 = student("shivam")
print(s1.name)
'''

# class is a blueprint for creating objects
# creating classs
class Student:
    college_name = "ABC College"
    # parameterized constructor
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks 
        print("Adding new student in database")
    def welcome(self):
        print("Welcome students", self.name)
    
# creating object variable (instance)
# s1 = Student("shivam kumar",82)
# print(s1.name)
# print(s1.welcome())

# self parameter is a reference to the current instance (object) of the classs and is used to access variable that belongs to the class


# s2 = Student("Arjun",92)
# print(s2.name, s2.marks)
# print(s2.college_name)

# class & instance attributes 


'''
CREATE STUDENT class THAT TAKE NAME , MARKS OF 3 SUBJECTS AS ARGUMENT IN CONSTRUCTOR.
THEN CREATE A METHOD TO PRINT THE AVG OF ALL 

'''
class Students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    @staticmethod
    def hello():
        print("Hello baccho")
    def avg (self):
        sum =0
        for i in self.marks:
            sum += i
        print("Hi", self.name, "your avg marks is ", sum/3)
s1 = Students("Shivam",[99,98,97])
print(s1.avg())
s1.hello()

# STATIC METHOD
# STATIC METHODS ARE METHOD WHICH DONT USE THE SELF PARAMETER
'''
4 pillars of OOP
1- ABSTRACTION
    Hiding the implementation details of a class and only showing the essential features to the user

2- ENCAPSULATION
    Wrapping data and functin into a single unit(object)

3- INHERITANCE
4- POLYMORPHISM
'''
class Car:
    def __init__(self):
        self.acc= False
        self.brk = False
        self.cluth = False
    def start(self):
        self.cluth = True
        self.acc = True
        print("Car Started")

# car1 = Car()
# car1.start()

'''
create account class with 2 attributes - balance & acc no
create methods for debit , credit & printing balance

'''
class Account:
    def __init__(self,balance, acc):
        self.balance = balance
        self.acc = acc
    def debit(self,amt):
        if self.balance > amt:
            self.amt = amt 
            self.balance = self.balance -amt
            print("Rs",amt,"was debited")
        else:
            print("Insufficient Balance")
        
    def credit(self,amt):
        self.amt = amt
        self.balance += amt 
        print("Rs",amt,"was credited")
    def check_balance (self):
        print("Your total balance is " ,self.balance)
        

a = Account(10000,2145478)
a.credit(16000)
a.check_balance()
a.debit(9782)
a.check_balance()