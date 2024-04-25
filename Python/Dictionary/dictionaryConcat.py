# concatenate the following dictionaries to create a new one

dict1 = {
    "name" : "Shrutik",
    "age" : 18
}

dict2 = {
    "eid" : 101,
    "salary" : 190000
}

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

key = input("Enter key you want to search for: ")
if key in dict3:
    print("Key already present")
else:
    print("Key not present")

for i in dict3.items():
    print(i)