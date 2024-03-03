# write a programme to enter marks of 3 subjects from the user and store them in a dict.start with an empty dict & add one by one. use subject name ad key & marks as value

dict = {}
phy = int(input("Enter the phy marks"))
dict.update({"Phy": phy})
chemistry = int(input("Enter the chemistry marks"))
dict.update({"Chemistry" : chemistry})
maths =int(input("Enter the marks marks"))
dict.update({"Maths" : maths})

print(dict)

print(dict)