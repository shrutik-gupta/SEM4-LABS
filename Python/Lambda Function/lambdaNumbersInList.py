"""find the numbers in a given string and store them in a list.
Afterward, display the numbers that are longer than the length of the list in sorted form"""

string = input("Enter desired string: ")
numList = []
for char in string:
    if char.isdigit():
        numList.append(int(char))

print("Numbers found in the string:", numList)
long_numbers = list(filter(lambda x: x > len(numList), numList)) #numlist mai se x>len(numlist) ko filter karke list mai store karo 
print("Numbers longer than the length of the list:", long_numbers)
