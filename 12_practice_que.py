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