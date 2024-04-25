lst = [12,4221,43532,6,3,2,5,47542,52,4,4,456,245,46,4255,]

uniqueList = list(set(lst))
uniqueList.sort()

k = int(input("Enter k: "))
print(k, "samllest element in list is: ", uniqueList[k-1])