lis = [1, 2, 3, 0, 1, 1, 4, 5, 2, 3]
lis2 = []

for i in lis:
    if i not in lis2:
        lis2.append(i)

print(lis2)
"""
output
[1, 2, 3, 0, 4, 5]
PS C:\Users\Dell\Documents\classwork4> 
"""