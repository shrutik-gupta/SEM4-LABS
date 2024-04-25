set1 = {1,2,3,4,5}
set2= {4,5,6,7,8}

list1 = [1,2,3,4,5]
list2= [4,5,6,7,8]

print(set1.union(set2))
print(set1.intersection(set2))

result=[]
def union(list1,list2):
    for element in list1:
        if element not in result:
            result.append(element)
    for element in list2:
        if element not in result:
            result.append(element)
    print(result)

result2=[]
def intersection(list1,list2):
    for element in list1:
        if element in list2:
            result2.append(element)
    print(result2)
    
union(list1,list2)
intersection(list1,list2)