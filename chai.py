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
km = int(input("Enter the distance"))

if km <= 3:
    print("chal ke chale jao bhai")
elif km <15:
    print("Bike utha lo")
else:
    print("Gaddi nikalo")