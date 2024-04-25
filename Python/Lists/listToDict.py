keys = [1,2,3,5,12,4]
values = [6,7,8,9,10,11]

dictionary = dict(zip(keys,values))
print(dictionary)

newDict=dict(sorted(dictionary.items()))
print(newDict)

maxVal = max(dictionary.values())
minVal = min(dictionary.values())
print(maxVal, minVal)