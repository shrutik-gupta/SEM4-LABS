# find the third largest number from a given list of numbers

list1= [21,41,2,55,73,7754,3,3,211,31,3,11,21,86]
uniqueList = list(set(list1)) #made set and removed duplicate elements and then converted back to list
uniqueList.sort()
print(uniqueList)
print("Third largest number is : ", uniqueList[-3])