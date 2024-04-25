# count the number of even and odd numbers in a series of numbers
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9,10)

oddCounter = 0
evenCounter = 0

for element in numbers:
    if element%2==0:
        evenCounter+=1
    else:
        oddCounter+=1

print("Number of odd elements: ", oddCounter)
print("Number of even elements: ", evenCounter)