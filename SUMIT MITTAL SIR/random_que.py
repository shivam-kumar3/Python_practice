students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
lower = []

for i in students:
    for j in i:
        lower.append(j)
        
print(lower[0:4])