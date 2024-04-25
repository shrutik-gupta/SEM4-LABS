# find the first non-repeated element in a list

lst = [1,2,3,4,4,5,2,3,1,4,13,3,5,2,1,3]
count_dict={}
lst.sort()
for item in lst:
    if item in count_dict:
        count_dict[item]+=1
    else:
        count_dict[item]=1

for item in lst:
    if count_dict[item]==1:
        print(item)