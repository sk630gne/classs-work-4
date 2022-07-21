mylist = [[4,5,3], [6,3,2], [6,9,1]]
nlist = []

sum = 0
for i in mylist:
    for j in i:
        sum += j
    nlist.append(sum)
    sum = 0

print(nlist)
"""
output
[12, 11, 16]
PS C:\Users\Dell\Documents\classwork4> 
"""