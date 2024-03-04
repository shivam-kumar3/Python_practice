# loops are used to repeat instructions.
# while loops

# while condition:
    # some work need to be done

# i =1

# while i < 100:
#     print(i)
#     i +=1
# print("Loop ended as it satified the condition")


# quesiton
# print numbers from 1 to 100

# i = 1
# while i <=100:
#     print(i)
#     i +=1

# print numbers from 100 to 1
    
# i = 100
# while i >=1:
#     print(i)
#     i -=1

# print the multiplication table of a number n asked by the user 
    
# n = int(input("Enter the number of your choice"))

# i = 1
# while i <=10:
#     print(f'{n} x  {i} = {n*i}')
#     i +=1

# print the elements of the following list using a loop:
# n = [1,4,9,16,25,36,49,64,81,100]

# index = 0
# while index < len(n):
#     print(n[index])
#     index +=1

# search of a number x in this tuple using loop:

t= (1,4,9,16,25,36,49,64,81,100)

x= 36
i = 0
while i <len(t):
    if t[i] == x:
        print("found at index ", i)
    i +=1
