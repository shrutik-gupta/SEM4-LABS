#remove duplicates from the dictionary

dictionary = {"name":"shrutik", "age":18, "ename":"shrutik", "eid": 310}
unique_dict = {}
for key, value in dictionary.items():
    if value not in unique_dict.values():
        unique_dict[key] = value

print(unique_dict)

count=0
for key in dictionary.keys():
    count+=1
if count==0:
    print("Empty dictionary")
else:
    print("Non empty dictionary")