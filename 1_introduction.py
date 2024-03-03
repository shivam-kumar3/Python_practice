'''
TimeStamps 
00:00:00 - Introduction
00:02:03 - Variables and Data Types
02:32:16 - Strings and conditional statements
03:27:13 - Lists and Tuples
04:08:03 - Dictionary and Set
05:01:26 - Loops
06:04:25 - Functions and Recursion
07:05:27 - File Input and Output
07:55:27 - OOPS Part 1
08:51:23 - OOPS Part 2
09:59:06 - Mini Project

'''


'''
what is python
python is simple & easy
free & open source
high level language
developed by guido van rossum
portable 
'''
# print is a function in python

print("Hello world") # it will give the output

'''
python character set
letters - A TO Z , a to z
digits - 0 to 9 
special symbols - + / * 
white space - blank space, tab, cariage return, newline, formfeed
other characters - pyton can process all ASCII and unicode characters as a part of data or literals
'''

print("shivam is my name\n my age is 28")

# Vatiables - A variable is a name given to a memory locatin in a program.

name = "Shivam"
age = 28
height = 1.79

print("my name is ", name,"age is", age, "and height is" ,height)

age2 = age

print(age2)

print(type(name))
print(type(age))
print(type(height))

'''
# DATA TYPES
int
string 
float
boolean
None
'''

age = 23
old = False
a = None

print(type(age))
print(type(old))
print(type(a))


'''
keywords
keywords are the reserved words in python

keywords cant be used as a variable name 


'''

# python is a case sensitive language 
# a and A both are two different variables

# practice question
# print sum

a = 2
b = 6
print("the sum of a and b is ",a+b)



# types of tokens
# punctuators
# punctuators are symbols to organise sentence structure in programming
# (),@,[],#

'''
expression execution

# string & numeric values can operate together with *

# string & string can operate with + (concatination)

# numeric values can operate with all arithmetic operators 

#  Arithmetic expression with interger and float with result in float

#  Result of division operator with two integers will be float

#  intger division with float and int will give int displayed as float

'''

# input

# name = input("enter your name")
# age = int(input("Enter your age"))
# height = float(input("Enter your age"))

# print(name)
# print(age)
# print(height)



# practice question
# write a program to input 2 numbers & print their sum

# a = int(input("Enter first number"))
# b = int(input("Enter second number"))

# print("the sum of first and second number is ", a+b)



# write a programe to input side of a square & print its area

# a = float(input("Enter the side ofa sqaure"))
# print("the area of the square is ", a*a)

# write a program to input 2 int number a and b 
# print true if a is great than or equal to b if not print flase

a = int(input("Enter a number"))
b = int(input("Enter another number"))

if a > b or a ==b:
    print (True)
else:
    print (False)