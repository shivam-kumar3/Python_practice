# try:
#     a = input("Enter any world")
#     print( a + 54)
# except TypeError:
#     print("You have entered a number, try with a word")


try:
  print("x")
except:
  print("An exception occurred")



'''
FIND THE SUM OF ALL THE EVEN NUMMBER BETWEEN 1 TO 1000  
'''

sum = 0
for i in range (1,1001):
  if i % 2 == 0:
    sum += i

print("The sum of all the even number between 1 to 1000 is" , sum)