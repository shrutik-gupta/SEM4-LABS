#List of tuples to list of lists

LoT=  [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
LoL = []
for element in LoT:
    L = list(element)
    LoL.append(L)
print(LoL)
