# create a new list after performating some transformations

order_amt = [100,200,50,500,400,900,1200,70]
gst = []

for x in order_amt:
     gst.append(x+x*.18)
print(gst)

# using list comprehension 

gst = [x+x*.18 for x in order_amt] # condition then where it need to apply
print(gst)

# in tuples
order_amt = [(100,5),(200,18),(50,12),(500,18),(400,12),(900,5),(100,18),(70,12)]
sum = []
for i in order_amt:
    sum.append(i[0] + i[0] * i[1]/100)
print(sum)

# using list comprehension 
order_amt = [(100,5),(200,18),(50,12),(500,18),(400,12),(900,5),(100,18),(70,12)]

gst = [i[0] + i[0] * i[1]/100 for i in order_amt]
print(gst)

# get the list in tuple with the current amt , gst percentage then final amt

order_amt = [(100,5),(200,18),(50,12),(500,18),(400,12),(900,5),(100,18),(70,12)]
sum = []
for i in order_amt:
    sum.append((i[0],i[1],i[0] + i[0] * i[1]/100) )
print(sum)

# using list comprehension

order_amt = [(100,5),(200,18),(50,12),(500,18),(400,12),(900,5),(100,18),(70,12)]

final = [(i[0],i[1],i[0] + i[0] * i[1]/100) for i in order_amt]
print(final)

# NESTED LIST 
# [[1,1,1],[2,4,8],[3,9,27]]
n=[]

for i in range(1,4):
    n.append([i,i**2,i**3])

print(n)

# using list comprehension

n = [[i,i**2,i**3] for i in range(1,4)]
print(n)

# no nested list (flattended list)
all = []
for i in n:
    for j in i:
        all.append(j)
print(all)

# using list comprehension
all = [j for i in n for j in i]
print(all)

# FILTER USING STATUS
orders_list = [
    [101,"2023-07-25 00:00:00.0",11599,"CLOSED"],
    [102,"2023-07-25 00:00:00.0",256,"PENDING"],
    [103,"2023-07-25 00:00:00.0",12111,"COMPLETE"]
]
com = []
for i in orders_list:
     if i[3] == "CLOSED":
        com.append(i)
print(com)

# using list comprehension 
com = [i for i in orders_list if i[3] == "CLOSED"]
print(com)

# unpacking 

order = [101,"2023-07-25 00:00:00.0",11599,"CLOSED"]

order_id , order_date, customer_id , status = order

print(order_id)

# make a list of 100

l = list(range(1,100))
print(l)

customer = [1,"Shivam", "Shahi", "XXXXXXXX", "xxxxxxxxxx", "Ag COlony", "bihar", "IND", 800023]

print(customer[0:2]+customer[4:])

# merge 2 list 
order = [101,"2023-07-25 00:00:00.0",11599,"CLOSED"]
customer = [1,"Shivam", "Shahi", "XXXXXXXX", "xxxxxxxxxx", "Ag COlony", "bihar", "IND", 800023]

order.extend(customer)
print(order)


# enumerate

order = [101,"2023-07-25 00:00:00.0",11599,"CLOSED"]
for index, element in enumerate(order):
    # print(f"Index {index}, Element {element}")
    print(index,element)

input_list = ["Hello","hello", "I", "AM","AM","shivam","shivam"]
input_set = set(input_list)
result = []

for i in input_set:
    result.append((i, input_list.count(i)))

print(result)

result = [(i, input_list.count(i)) for i in input_set]
print(result)

# ASSINGMENT 1 :Find the count of each order status

order = ['CLOSED', 'PENDING_PAYMENT', 'COMPLETE', 'CLOSED', 'COMPLETE', 'COMPLETE', 'COMPLETE', 'PROCESSING', 'PENDING_PAYMENT', 'PENDING_PAYMENT']

order_set = set(order)
print(order_set)

result = []
for i in order_set:
    result.append((i,order.count(i)))
print(result)


orders= [    
    [1, 100, 'success'],
    [2, 200, 'pending'],
    [3, 150, 'success'],
    [4, 300, 'failed'],
    [5, 400, 'success'],
    [6, 250, 'pending'],
    [7, 350, 'failed'],
    [8, 450, 'success'],
    [9, 500, 'pending'],
    [10, 600, 'failed']
]
# output :
# success: 4
# pending: 3
# failed: 3

status_count = {'success': 0, 'pending': 0, 'failed': 0}

for i in orders:
    status = i[2]
    status_count[status] += 1

for status, count in status_count.items():
    print(f"{status}: {count}")

