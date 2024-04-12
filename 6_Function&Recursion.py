# FUNCTION
# BLOCK OF STATEMENTS THAT PERFORM A SPECIFIC TASK

# def function_name():
#     some work

def welcome():
    print("Welcome to the board")

welcome()
welcome()
welcome()

def sum(num1,num2): #parameters
    print(num1+num2)

sum(5,10) #function call;arguments


# avg of 3 numbers

def avg(num1,num2,num3):
    print(num1+num2+num3/3)

avg(5,14,15)

# write a function to print the length of a list
def length(list):
    print(len(list))



l = [1,5,4,8,5,6,9,8,7]

length(l)

# write a function to print the elements of a list in a single line (list is the parameter)

# def single_line(list):
#     print(list, end = " ")

# single_line(l)

# write a function to find the factorial of n (n is the parameter)

def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *=i
    print(fact)

fact(4)

# write a function to convert usd to inr
def convertor(n):
    i = (n*82.85)
    print(f"USD{n} is Rs{i} ")

convertor(100)


# Recursion
# WHEN A FUNCTION CALLS ITSELF REPEATEDLY

# print n to 1 backward 


def show(n):
    if n ==0:
        return
    print(n)
    show(n-1)

show(5)


