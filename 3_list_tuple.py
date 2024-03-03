# lista built in data type that stores set of values
# it can store elements of different types(integers, floats,str etc)


marks = [95,48,74,26,87,58]
print(marks)
print(type(marks)) #type
print(marks[1]) # indexing
print(len(marks)) #length of list 
marks[0] = 100
print(marks)

print(marks[1:3])
marks.append(5) # add at the last of the list 
print(marks)

marks.sort()
marks.sort(reverse=True)
print(marks)

f = ["banana", "litchi", "apple"]

f.sort()
print(f)
marks.reverse()
print(marks)


marks.insert(5,"apple")
print(marks)

marks.remove("apple")
print(marks)

marks.pop(0)
print(marks)



# tuples
# list ka dur ka bhai 

# a built in data type that let us create immutable sequence of value

t = (87,87,45,25,14)
print(t)

print(t[0])
# we cant change the values using indexing 
print(t.index(25))
print(t.index(25))
print(t.index(25))

# write a programme to ask the user to enter names of their 3 fav movies & store them in a list 

# a= input("Enter your first fav movie")
# b= input("Enter your second fav movie")
# c= input("Enter your third fav movie")
# l = []
# l.append(a)
# l.append(b)
# l.append(c)
# print(l)

# write a programe to count the number of students with "A" grade in the following tuple
t = ("c","d","a","a","b","b","a")
t.count("a")

# store the above values in a list & sor them from "A to d"
l = list(t)
l.sort()
print(l)


# this is also the commit