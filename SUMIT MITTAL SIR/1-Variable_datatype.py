'''
PYTHON FOR DATA FOLKS 
THIS COURSE BE ENOUGH TO CRACK INTERVIEWS
+PYTHON IS IN GREAT DEMAND 
-SUPER EASY TO LEARN
-A REALLY A GOOD SUPPORT FOR ML AND AI APPLICATION
-IN PYSPARK WE USE PYTHON

'''

print("Hello Data Scientist ")
print("Hello World")

# variables in python 
# variables are immutables in python 

course_fee = 800
course_fee = 850
print(course_fee)

instructor_name = "Shivam Kumar"
course_fee = 800
course_rating =  4.95
is_starting_soon = True
Total_income = None

'''
5 main simple datatypes
- Int
- Float
- bool 
- String
- None

'''
print(type(instructor_name))
print(type(course_fee))
print(type(course_rating))
print(type(is_starting_soon))
print(type(Total_income))

# increase the course fee by 50
course_fee = course_fee + course_fee * .1

print(course_fee)


# manual type casting 

'''
in big data world 
you might read the data from a text file 


'''
instructor_name = "Shivam Kumar"
course_fee = "800"
course_rating =  "4.95"
is_starting_soon = "True"
Total_income = "None"


print(type(course_fee))

course_fee = int(course_fee) + int(course_fee) * .1

# string concatination and formating

first_name= "Shivam"
last_name= "Kumar"

print("=========" * 6)
print(f'My first name is {first_name} and my last name is {last_name}')
print("=========" * 6)

salary = int(input("What is your current salary "))
hike = int(input("what is the hike percentage "))

new_salary = salary + (salary * hike/100)
print(f'The new salary after the hike is {new_salary}')

'''
what we have learnt:
- INTRODUCTION
- INSTALLING PYTHON 3 
- OUR FIRST PROGRAM
- VARIABLE
- DATA TYPES
- TYPE ERRORS ARE CAUGHT AT RUNTIME
- TYPECASTING
- STRING CONCATENATION & FORMATING 
- HOW TO TAKE INPUT FROM THE USER


'''