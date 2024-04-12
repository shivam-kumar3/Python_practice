# Solve 10 conditional problem in python

'''age group categorization 
# classify a person age group 
child (<13)
teenager (13-19)
adult(20-50)
senior (80+)

'''

    
# age = int(input("Enter your age"))
# if age <13:
#     print("You are child")
# elif age > 13 and age <=19:
#     print("You are teenager")
# elif age >= 20 and age < 50:
#     print("You are adult")
# else:
#     print("You are senior")


'''
Movie ticket pricing
movie tickets are priced based on age :
$8 for children
$12 for adults (18 and above)
$2 discount for everyone on wednesday 


'''

# age = int(input("Enter your age"))
# day = "Wednesday"

# if age <= 18:
#     print("Ticket price is $8")
# else:
#     print("Ticker price is $12")

# price = 8 if age <= 18 else 12

# if day == "Wednesday":
#     price -= 2
# print(price)


'''
GRADE CALCULATOR 
assign a letter grade based on a studens score 
A = 90-100
B = 80 - 89
C = 70 - 79
D = 60-69
F = BELOW 60
'''

# marks = int(input("Enter Your Marks"))

# if marks >= 101:
#     print("Please verify your grades again")
#     exit()

# if marks >= 90:
#     print("A Grade")
# elif marks  >= 80:
#     print("B Grade")
# elif marks >= 70:
#     print("C grade")
# elif marks >= 60:
#     print("D Grade")
# else:
#     print("F Grade")

'''
FRUIT RIPENESS CHECKER 
PROBLEM : 
DETERMINE IF A FRUIT IS RIPE, OVERRIPE OR UNRIPE BASED ON ITS COLOR 
GREEN - UNRIPE
YELLOW - RIPE
BROWN - OVERRIPE

'''
# color = int(input('''choose the color of your fruit 
#               1 - GREEN
#               2 - YELLOW
#               3 - OVERRIPE
#               '''))

# if color == 1:
#     print("Your fruit is unripe")
# elif color == 2:
#     print("Your fruit is ripe")
# elif color == 3:
#     print("Your fruit is overipe")

'''
WEATHER ACTIVITY SUGGESTION
PROBLEM:
suggest an activity based on the weather 
sunny - on for a walk 
rainy - read a book
snowy - build a snowman



'''
# climate = input("Hows the weather")

# if climate.lower() == "sunny":
#     print("Lets go for a walk")
# elif climate.lower() == "rainy":
#     print("Lets have chai and pakoda")
# elif climate.lower() == "snowy":
#     print("bahut thandi hai bhaiya")

'''
TRANSPORT MODE SELECTION
CHOOSE A MODE OF TRANSPORATATION BASED ON THE DISTANCE
<3KM - WALK
3-15KM - BIKE
>15 - CAR

'''
# km = int(input("Enter the distance"))

# if km <= 3:
#     print("chal ke chale jao bhai")
# elif km <15:
#     print("Bike utha lo")
# else:
#     print("Gaddi nikalo")


''' 
password strength checker
<6 character = wwak
6-10 characters = medium
>10 characters = strong


'''
# pas = input("enter your password")

# if len(pas) < 6:
#     print("Weak password")
# elif len(pas) <10:
#     print("Medium password")
# else:
#     print("Strong password")


'''
LEAP YEAR CHECKER 
PROBLEM:
determine if a year is a leap year. (leap year are divisible by 4 but not by 100 unless also division by 400)


'''

# year= int(input("Enter the year"))

# if year % 4 == 0 or year % 400 == 0:
#     print("The year is leap year")

# else:
#     print("The year is not leap year")


#FUNCTION
'''
1- BASIC FUNCTION SYNTAX
    # WRITE A FUNCTION TO CALCULATE AND RETURN THE SQUARE OF A NUMBER
'''
def square(a):
    return (f"the Sqaure of the given number is {a**2}")

print(square(5))

'''
2- Function with multiple parameters
    Create a function that takes two numbers as parameters and returns their sum

'''
def sum(num1,num2):
    return num1 + num2

print(sum(5465,1234))

'''
3- Polymorphism in functions
write a function multiply that multiplies two number but can also accept and multiply strings

'''

def multiply(a,b):
    return a*b

print(multiply(2,3))
print(multiply("a",3))
print(multiply(2,"A"))

'''
4 - FUNCTION RETURNING MULTIPLE VALUES
CREATE A FUNCTION THAT RETURN BOTH THE AREA AND CIRCUMFERENCE OF CIRCLE GIVEN ITS RADIUS 

'''
import math
def circle_stats(radius):
    area = round(math.pi * radius **2,2)
    circum = round(2*math.pi*radius,2)

    return (f"The Area is {area}, The Circumference is {circum}")

print(circle_stats(5))

'''
5- default parameter values
write a function that greets a user, if no name is provided, it should greet with default name

'''

def greet(a="Buddy"):
    return(f"Hello welcome to the board {a}")

print(greet())
print(greet("Rohan"))


'''
6 - lambda function
Create a lambda function to compute the cube of a number

'''

cube = lambda a : a**3

print(cube(5))

'''
7 - function with *args
write a function that takes variable number of arguments and returns their sum
'''

def multisum(*a):
    sum = 0
    for i in a:
        sum = sum +i
    return sum

print(multisum(2,14,5,6,8,7,1))


'''
8 - FUNCTION WITH **KWARGS
Create a function that accepts any number of keywords arguments and print them in the format of  key : value

'''

def key_value(**a):
    for key, values in a.items():
        print(key, values)

print(key_value(marks = [15,12,54,87],name = ["shivam ", "shahi","Rohan","Ram"]))

'''
9 -Generate a funcion with yield 
Write a generator function that yield even numbers up to a specified limit
'''

def all(a):
    for i in range(1,a):
        if i % 2 == 0:
            yield i


for num in all(50):
    print(num)

'''
10- RECURSIVE FUNCTION
CREATE A RECURSIVE NUMBER TO FIND FACTORIAL OF A NUMBER
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))