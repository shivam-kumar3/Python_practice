# FILE I/O IN PYTHON
# PYTHON CAN BE USED TO PERFORM OPERATION ON A FILE (READ & WRITE DATA)


# TYPES OF ALL FILES
# 1- TEXT FILES: .TXT,.DOCX,.LOG ETC
# 2- BINARY FILES - .MP4, .MOV, .PNG,.JPEG ETC


# WE HAVE TO OPEN A FILE BEFORE READING OR WRITING 

# F = OPEN("FILE NAME", "MODE("r" / "w")") # read or write

# data = f.read()
# f.close()

f = open("file.txt","r")
data = f.read()
print(data)
f.close()


f = open("file.txt","r")
data = f.read(5)
print(data)
f.close()


f = open("file.txt","r")
data = f.readline()
print(data)
f.close()


f = open("file.txt","r")
data = f.readline()
print(data)
data2= f.readline()
print(data2)
f.close()


# writing to a file 

# "w" - delete all the thing and replace it with new one
# "a" - append the new text at the last

f = open("file.txt", "w")
f.write("this is the new line")
f.close()

f= open("file.txt","a")
f.write("this is the line written by the append method")
f.close()


f= open("newfile.txt","w")
f.write("this file is created using the file command")

f= open("newfile.txt" ,"r+")
f.write("new file")

f= open("newfile.txt" ,"w+")
f.write("we can write the things at the starting using r+ mode by overwriting the old file ")

# with syntax

with open("file.txt","r") as f:
    data= f.read()
    print(data)

with open("file.txt","w") as f:
    f.write("new data")
    print(f)

# deleting the file 
# using the os module 

# module (like a code library) is a file written by another programmer that generally has a function we can use.UserWarning

# import os
# os.remove("filename")
    
import os 

# os.remove("file.txt")

# create a new file "practice.txt" using python. add the following data in it.
'''
hi everyone
we are learning file I/O
using java 
I like porgramming in java

'''
with open("practice.txt", "w") as f:
    f.write('''
hi everyone
we are learning file I/O
using java 
I like porgramming in java
''')
    print(f)

with open("practice.txt", "r") as f:
    data = f.read()

    new_data = data.replace("java", "python")
    print(new_data)

with open("practice.txt" ,"w") as f:
    f.write(new_data)


# search if word learning is exist or not
def check_for_word()
    word = "learning"
    with open("practice.txt","r") as f:
        data = f.read()
        if data.find(word) != -1:
            print("found")
        else:
            print("not found")

# WAF TO FIND IN WHICH LINE OF THE FILE DOES THE WORD "LEARNING"