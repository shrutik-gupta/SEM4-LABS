# compute the sum of all the elements of each tuple stored inside a list of tuples.

LoT = [(1, 2), (2, 3), (3, 4)]
newList = []

for tuple in LoT:
    result = 0  # Reset result for each tuple
    for element in tuple:
        result = result + element
    newList.append(result)

print(newList)
