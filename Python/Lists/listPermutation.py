def permutations(lst):
    if len(lst) == 0:
        return [[]]  # Base case: empty list has one permutation, an empty list itself
    elif len(lst) == 1:
        return [lst]  # Base case: list with one element has one permutation, the list itself
    else:
        result = []
        for i in range(len(lst)):
            first_element = lst[i]
            remaining_elements = lst[:i] + lst[i+1:]
            for p in permutations(remaining_elements):
                result.append([first_element] + p)
        return result

# Test the function
my_list = [1, 2, 3]
print("Permutations of", my_list, "are:")
for perm in permutations(my_list):
    print(perm)
