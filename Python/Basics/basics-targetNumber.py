#find all the unique combinations of 3 numbers from a given list ofnumbers, adding up to a target number.

numbers = [1, 2, 3, 4, 5]
target = 10
unique_combinations = set() #will store set of tuples

for i in numbers:
    for j in numbers:
        for k in numbers:
            if i + j + k == target:
                combination = tuple(sorted([i, j, k]))
                unique_combinations.add(combination)

print("Unique combinations:")
for combination in unique_combinations:
    print(combination)
