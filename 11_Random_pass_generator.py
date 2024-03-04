# RANDOM PASSWORD GENERATOR

import random
import string

password_len = 12

char_values = string.ascii_letters + string.punctuation + string.digits

password = ""
for i in range(password_len):
    password += random.choice(char_values)
print(f"Your random password is {password}")


# list comprehension [function for i in range(n)]
res= "".join([random.choice(char_values) for i in range (password_len)])
print(res)


2

