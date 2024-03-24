# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
'''

num1 =int(input("Enter the 1st number"))
num2 = int(input("Enter the 2nd number"))
final = num1 * num2

if final < 1000:
    print("The result is ", final)
else:
    print("The result is ", num1+num2)

number1 =int(input("Enter the 1st number"))
number2 = int(input("Enter the 2nd number"))
final = number1 * number2

if final < 1000:
    print("The result is ", final)
else:
    print("The result is ", number1+number2)
'''


# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
'''
pre_num = 0
print("Printing current and previous number sum in a range(10)")
for i in range(10):
    print("Current Number", i, "Previous Number", pre_num, "Sum = ",(pre_num + i))
    pre_num = i


'''

# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.
    
'''
str = input("Enter any word")
print("The length of your word is ", len(str))

for i in range(0,len(str)-1,2):
    print("index[", i, "]", str[i])

'''

# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.
'''
char = "pynative"

char_new = char[4:]

print(char_new)

word = "pynative"

new_word = word[2:]
print(new_word)
'''

# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
'''
x = [10,20,30,40,10]
y = [75,65,35,75,30]

print("Given List ", x)
if x[0] == x[-1]:
    print (True)
else:
    print (False)

print("Given List ", y)
if y[0] == y[-1]:
    print(True)
else:
    print(False)
'''
# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5
'''
l = [10,20,33,46,55]
print("Divisible by 5")
for i in l:
    if i % 5==0:
        print(i)

''' 

# Exercise 7: Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.

# str_x = "Emma is good developer. Emma is a writer"

# print(f"Emma appeared {str_x.count("Emma")} times")


# Exercise 8: Print the following pattern

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# for i in range (0,6):
#     for j in range (i):
#         print(i, end = " ")
#     print("\n")

# Exercise 9: Check Palindrome Number


# a = int(input("Enter any number"))
# if a == a.reverse():
#     print("Yes. given number is palindrome number")
# else:
#     print("No. given number is not palindrome number")



# filter odd EnvironmentErrordefine a function input list 
# output = [[1,3,5,7],[2,4,6,8]]

# def filter_odd_even(list):
#     odd = []
#     even = []
#     for i in list:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     output = [odd,even]
#     return output 

# list = [1,2,3,4,5,6,7,8,9,10]

# print(filter_odd_even(list))

# create a new list after performing some transformation

order_amt = [100,200,50,500,100,900,1200,70]
gst_amt = []
for i in order_amt:
    gst_amt.append(i + i*.18)
print(gst_amt)

# list comprehension method
order_amt = [100,200,50,500,100,900,1200,70]
gst_amt = [i + i*.18 for i in order_amt]
print(gst_amt)


# with tuples using index
amt = [(100,5),(200,18),(50,12),(500,18),(400,12),(900,5),(1200,18),(70,12)]

order_gst = []
for i in amt:
    order_gst.append(i[0]+i[0]*i[1]/100)

print(order_gst)

# list comprehension method with tuples
amt = [(100,5),(200,18),(50,12),(500,18),(400,12),(900,5),(1200,18),(70,12)]

gst = [i[0]+i[0]*i[1]/100 for i in amt]
print(gst)

# required output = [(100,5,105)]
amt = [(100,5),(200,18),(50,12),(500,18),(400,12),(900,5),(1200,18),(70,12)]

gst = [(i[0], i[1] , i[0]+i[0]*i[1]/100) for i in amt]
print(gst)

# want to create a nested list

# [[1,1,1,],[2,4,8],[3,9,12]]
nested_list = []
for i in range(1,4):
    nested_list.append([i,i**2,i**3])
print(nested_list)

# using list comprehension
nested = [[i,i**2,i**3] for i in range(1,4)]
print(nested)

