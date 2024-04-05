# Dictionary - {"Key" : "Values"} - Mutable 

# we can change the values
# we can add more entries
# we can remove some of the entries 
# keys should be immutable

word_dict = {
    "Intelligent": "The one who is really brilliant", "Rich" : "A person who has lot of money", 
    "Car": "A 4 wheel vehicle ",
    "Three":3,
    4 : "Four",
    (1,2,3) :"Tuple"
}

print(word_dict)
print(type(word_dict))

print(word_dict[4])
print(word_dict.get(5)) #this function give the none output if it doesnt exist
print(word_dict[1,2,3])

# adding new item
word_dict["Bike"] = "2 Wheeler"

print(word_dict)

# upadting the value of existing entries

word_dict["Car"] = "Lamborghini"
print(word_dict)

# converting tuples into dict
order_data = [(101,1000),(102,20000),(103,15000)]

order_data = dict(order_data)
print(order_data)

print(order_data[102])

# getting the all the values 
print(order_data.values())

# getting the all the keys 
print(order_data.keys())

# getting the all the keys and values
print(order_data.items())

# getting the length of the dict

print(len(order_data))

# clearing the dict
order_data.clear()

print(order_data)


cust_data =''' customer_id , customer_fname , customer_lname , add ress , city , state , pincode
11599,Mary,Malone,87Ø8 Indian Horse Highway, Hickory,NC,286Ø1
256, David, Rodriguez, 7605 Tawny Horse Falls, Chicago, IL, 60625
12111, Amber, Franco,8766 ClearOrairie1ine,Santa Cruz,CA,95Ø6Ø
8827, Brian,Wilson,8396 High Corners, San Antonio, TX, 78240
11318,Mary, Henry, 3047 Silent • Embers Maze, Caguas, PR, 0725'''

cust_data =cust_data.split("\n")[1:]

# cust_dict  ={}
# for x in cust_data:
#     cust_dict[x.split(",")[0]] = tuple(x.split(",")[1:])

# print(cust_dict["11599"])

# using dict comprehension

cust_dict = {x.split(",")[0] : tuple(x.split(",")[1:]) for x in cust_data}

print(cust_dict)

# id = input("What is the customer id ")
# name = input("What things you want to get ")

nested_dict = {}

for key, value in cust_dict.items():
    nested_dict[key]= {
        "customer_lfname" :value [0] ,
        "customer Iname" :value [1] ,
        "address" :value [2] ,
        "city"      :value[3] ,
        "state" :value[4] ,
        "ttpincode" : value[5]

    }
# print(nested_dict)

# print(nested_dict.get(id).get(name))


# joining customer data with customer data in dict 

raw_orders_data = ''' 
1, 2013-07-25 00:00:00.0 , 11599, CLOSED
2, 2013-07-25 00:00:00.0 , 256 ,PENDING PAYMENT
3, 2013-07-25 00:00:00.0 , 12111, COMPLETE
4, 2013-07-25 00:00:00.0, 8827 , CLOSED
5, 2013-07-25 00:00:00.0 , 11318 , COMPLETE

'''

orders_data = raw_orders_data.split("\n")

print(orders_data[0])