n = int(input("Enter number till you want your dictionary to be: "))
result={}
for i in range(1,n+1):
    result[i] = i*i
print(result)

sum_of_values=0
sum_of_keys=0

for i in result.values():
    sum_of_values+=i
print(sum_of_values)

for i in result.keys():
    sum_of_keys+=i
print(sum_of_keys)

result.pop(3)
print(result)