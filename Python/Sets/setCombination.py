#Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa

set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {6, 7, 8, 10, 11}

missing_set1 = set1 - set2
missing_set2 = set2 - set1

print("Missing in set1:", missing_set1)
print("Missing in set2:", missing_set2)