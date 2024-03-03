str1 = "this is the string"
str2 = 'This is also a string with single quote'
str3 = '''this is also a string with 3 quotes'''


str4= "this is a string \nwe are creating it in python"

print(str4)

# concatination
str5 = "shivam" +  " shahi"
print(str5)

a = "shivam"
b = "shahi"

print(a + " " +b)

print(len(a))

# indexing

a = "i will be data scientist this year at any cost"

print(a[5:])
print(a[::-1])

print(a.endswith("t"))
print(a.capitalize())
print(a.upper())
print(a.lower())

print(a.replace("data", "Data"))
print(a.find("data"))
print(a.count("i"))



# write a program to input users first name & print its length

# a = input("Enter your name for the length of your name")
# print(len(a))

# wtite a program to find the occurrence of "$" in a string.

a = "this$$ is the name shivam$$ and for find the$$occurrence in the $$string"

print(a.count("$"))


# conditional statement

# if elif else
'''
if(condition):
    statement 1
elif (condition):
    statement 2
else:
    statement n
'''

# marks = int(input("Enter your marks"))

# if marks >= 90:
#     print(f"You have secured {marks} and your grade is A")
# elif marks >= 80:
#     print(f"You have secured {marks} and your grade is B")
# elif marks >=70:
#     print(f"You have secured {marks} and your grade is C")
# else:
#     print(f"You have secured {marks} and your grade is D")


# write a program to check if a number entered by the user is odd or even

# num = int(input("Enter any number:- "))

# if num %2 == 0:
#     print("The given number is even")
# else:
#     print("The given number is odd")

# write a program to find the greatest of 3 number netered by the user
    
# a= int(input("Enter first number"))
# b= int(input("Enter second number"))
# c= int(input("Enter third number"))

# if a > b and a > c:
#     print("The greatest number among three number is ", a)
# elif b > a and b > c:
#     print("The greatest number among three number is ", b)
# else:
#     print("The greatest number among three number is ", c)


# write a programe to check if a number is multiple of 7 or not
num = int(input("Enter your number"))

if num % 7 == 0:
    print("The number is multiple of 7 ")

else:
    print("The number is not multiple of 7")



