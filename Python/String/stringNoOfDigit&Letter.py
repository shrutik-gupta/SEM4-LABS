str = input("Enter a string: ")
num_letters=0
num_digits=0
for char in str:
    if char.isdigit():
        num_digits += 1
    elif char.isalpha():
        num_letters += 1

print(num_digits, num_letters)