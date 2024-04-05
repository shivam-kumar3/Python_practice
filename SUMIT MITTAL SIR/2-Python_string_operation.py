bigdata_fee = 800
azure_fee = 600
bigdata_enroll = 60
azure_enroll = 40

'''arithmetic operations
/
*
+
-
%
//

precedence is left to right 
* / 
+ - 
'''

total = bigdata_fee * bigdata_enroll + azure_fee *azure_enroll

print(f'Total Revenue is {total}')


# finding avg order price 
# avg order price = total sale / total copy sold

avg_price = (bigdata_fee * bigdata_enroll + azure_fee *azure_enroll) / (bigdata_enroll+azure_enroll)

print(avg_price)

print((5+3)*8)
print(5+3*8)

print(15%4)

print(15//4)
print(15/4)

# calculation is happend from left to right in python

print( 2 ** 2 ** 3)

# increasing big daata fee by 50

bigdata_fee +=50
bigdata_fee = bigdata_fee +50

print(bigdata_fee)

import math
# ceiling function
total_fee= -200.154

print(math.ceil(total_fee)) #next number (higher value)
print(math.floor(total_fee)) #previour number (lower value)
print(math.fabs(total_fee)) #convert the number into postive value

# conditional statements 
# if else
'''
marks = int(input("Enter the marks: "))
if marks >= 35:
    if marks > 80:
        print("A grade")
    else:
        print("You passed but you didnt secure A grade")
else:
    print("Fail")


marks = int(input("Enter the marks: "))
if marks >= 80:
    print("A Grade")
elif marks > 35:
    print("Passed")
else:
    print("Fail")
'''

'''
take 2 input 
age > 18
crime record = no 
eligible
'''

# age = int(input("Enter your age:- "))
# crime_record = input("Enter yes or no:- ")

# if age > 18 and crime_record.lower() == "no":
#     print("Yes you can vote")

# else:
#     print("You cant vote")

# name = "Shivam Shahi"

# print("Shivam" not in name)

# working with strings

# what is the string 
# a sequence of characters

name = 'shivam"s training \nis really good'
print(name)

# string related operations 

# concatination 
# first_name = input("First Name ")
# last_name = input("Last Name ")

# print(first_name+" "+last_name)

# indexing - helps to get a particular character
# slicing - help to get a slice 

order_status = "completed order"

# string is immutable you cannot make any changes

print(order_status[12])

# slicing 

print(order_status[:7])

print(order_status[10:])

# print everything after the space

index = order_status.find(" ")
print(order_status[index:])

# print the first word
index = order_status.find(" ")
print(order_status[0:index])
print(order_status[1:9])

# reverse a string 

print(order_status[::-1])

# finding a character
# if  not found this return -1

print(order_status.find("s"))
print(order_status.endswith("order"))
print(order_status.capitalize())
print(order_status.upper())
print(order_status.lower())

print(order_status.replace("completed", "completedddd"))

'''
# DATA STRUCTURES
SEQUENCE IS IMPORTANT 
LIST [1,5,6,8]
TUPLE (4,5,6,8)
RANGE (0,9)
STR "SHIVAM"

SEQUENCE IS NOT IMPORTANT 
DICTIONARY 
SET {"CRICKET", "HOCKEY", "BASKETBALL"}

'''

order_df = "1,2013-07-28 00:..:00.0,11599,closed"
order_df = order_df.split(",")

print(order_df)

