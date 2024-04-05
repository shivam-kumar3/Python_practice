'''
4 main data structures in python (collection type)

list- [1,2,4,5]
tuple - (1,2,3,4)
set - {1,2,3,4}
dictionary - {"brand":"Apple","model":15,"price":69999}

sequence types - list , tuple, string
non sequence type - set, dict

Mutable :-
list
set
dict

immutable :-
string
tuple


'''
order_df = [1,"2013-07-28 00:00:00.0",11599,"closed"]
order_df.append(100)

order_df[3] = "Completed"
print(order_df[3])
print(order_df)
print(len(order_df))

no = range(1,10)
print(no)

# using range function

order_amt = [100,200,None,"invalid",300,400.5]

sum = 0
for i in order_amt:
    if type(i) == int or type(i) == float:
        sum += i
    else:
        continue
print(sum)

# using while loop function

order_amt = [100,200,None,"invalid",300,400.5]
i = 0 
sum = 0
while i < len(order_amt):
    if type(order_amt[i]) == int or type(order_amt[i]) == float:
        sum += order_amt[i]
    else:
        i += 1
        continue
    i = i+1
print(sum)


# using while true 


order_amt = [100,200,None,"invalid",300,400.5]
i = 0 
sum = 0
while True:
    if type(order_amt[i]) == int or type(order_amt[i]) == float:
        sum += order_amt[i]
    else:
        i += 1
        continue
    i = i+1
    if i == len(order_amt):
        break
print(sum)

# finding index of the item in the list
order_df = [1,"2013-07-28 00:00:00.0",11599,"closed"]

print(123 in order_df)

order = [50,50,40,50,30,50]

print(order.count(50))

order = (50,50,40,50,30,50)

print(order.count(50))
order = [50,50,40,50,30,50]
order.sort()
order.reverse()
print(order)

order = [50,50,40,50,30,50]
order_new = order.copy()
order_new[1] = 325
print(order_new)

customer_id = [102,105,102,103,107,109,110,109]

# finding the list of unique customers

unique_cust = []
for x in customer_id:
    if x in unique_cust:
        continue
    else:
        unique_cust.append(x)

print(unique_cust)

new = set(customer_id)
print(new)